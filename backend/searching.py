from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import Blueprint
import streamlit as st
from neo4j import GraphDatabase
from qdrant_client import QdrantClient
import json
import cv2
import torch
import numpy as np
import os
from facenet_pytorch import InceptionResnetV1, MTCNN
import pandas as pd

uri = "bolt://localhost:7687"
username = "neo4j"
password = "12345678"
driver = GraphDatabase.driver(uri, auth=(username, password))

qdrant_client = QdrantClient(
    url="https://108a5241-04bf-4d9e-9c98-d1deeeefcb3e.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="zpt50bX6nRJoxsj0C9nMQfPtdUL71s2GmJcrYOLvYOlt-5yWBAydzg",
)

model = InceptionResnetV1(pretrained='vggface2').eval()
mtcnn = MTCNN(image_size=160, margin=0)

def find_related_nodes_by_person(tx, identifier, identifier_type):
    """
    Truy vấn tất cả các node liên quan đến người dùng dựa trên identifier và identifier_type.
    identifier_type có thể là 'so_dinh_danh', 'ma_so_bhyt', hoặc 'bien_so'.
    """
    if identifier_type == "so_dinh_danh":
        query = """
        MATCH (p:Person {so_dinh_danh: $identifier})-[r]-(connected)
        RETURN p AS NodeGoc, type(r) AS LoaiQuanHe, connected AS NodeKetNoi
        """
        print(query)
    elif identifier_type == "ma_so_bhyt":
        query = """
        MATCH (p:Person)-[:HAS_INSURANCE_CARD]->(i:InsuranceCard {ma_so_bhyt: $identifier})-[r]-(connected)
        WITH p, type(r) AS LoaiQuanHe, connected
        MATCH (p)-[r]-(related)
        RETURN p AS NodeGoc, LoaiQuanHe, related AS NodeKetNoi
        """
    elif identifier_type == "bien_so":
        query = """
        MATCH (p:Person)-[:HAS_VEHICLE_REGISTRATION]->(v:VehicleRegistration {bien_so: $identifier})-[r]-(connected)
        WITH p, type(r) AS LoaiQuanHe, connected
        MATCH (p)-[r]-(related)
        RETURN p AS NodeGoc, LoaiQuanHe, related AS NodeKetNoi
        """
    else:
        raise ValueError("identifier_type không hợp lệ")

    result = tx.run(query, identifier=identifier)
    node_goc = None
    related_nodes = []
    
    for record in result:
        if node_goc is None:
            node_goc = record["NodeGoc"]
        related_nodes.append({
            "LoaiQuanHe": record["LoaiQuanHe"],
            "NodeKetNoi": record["NodeKetNoi"]
        })
    
    return node_goc, related_nodes

def recognition(img):
    if img is None:
        print("Error: Could not load the image. Check the file path.")
    faces, _ = mtcnn.detect(img)
    if faces is not None:
        print(len(faces))
        for face in faces:
            bbox = list(map(int,face.tolist()))
            face_img = img[bbox[1]:bbox[1] + bbox[3], bbox[0]:bbox[0] + bbox[2]]
            face_img = cv2.resize(face_img, (160, 160))
            face_img = np.transpose(face_img, (2, 0, 1))
            face_img = torch.tensor(face_img, dtype=torch.float32)
            face_img = (face_img - 127.5) / 128.0  
            face_img = face_img.unsqueeze(0) 
            embedding = model(face_img).detach()
            embedding_array = embedding.numpy().tolist()

            results = qdrant_client.query_points(
                collection_name="Face_recognition",
                query=embedding_array[0],
                limit=1
            )
            
            first_point = results.points[0]
            score = first_point.score
            id = first_point.id
            if (score<=0.4):
                name = "Unknown"
            else:
                name = first_point.payload['name']
    return id, name


app = Blueprint('router1', __name__)
CORS(app, supports_credentials=True, allow_headers=["Content-Type"])

@app.route('/getinformation', methods=['POST'])
def receive_data():

    try:
        # # Nhận dữ liệu từ request
        # data_received = request.get_json()

        # print(data_received)
        # params = data_received.get('params', {})

        # identifier_type = params.get('identifier_type')
        identifier_type = request.form.get('identifier_type')
        identifier = request.form.get('identifier')
        if identifier_type == 'hinh_anh':
            file = request.files['identifier']
            if not file:
                return jsonify({'error': 'No image file provided'}), 400
           
            identifier_type = 'so_dinh_danh'
            img_array = np.frombuffer(file.read(), dtype=np.uint8)
            image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            id, name = recognition(img=image)
            identifier = str(id)
            print(identifier)
        else:
            identifier = request.form.get('identifier')

        node_groups = {}

        
        with driver.session(database="Data4life") as session:
            try:
                node, related_nodes = session.execute_read(find_related_nodes_by_person, identifier, identifier_type)
                
                if related_nodes:
                    for item in related_nodes:
                        node_label = list(item["NodeKetNoi"].labels)[0] if item["NodeKetNoi"].labels else "Không có label"
                        
                        if node_label not in node_groups:
                            node_groups[node_label] = []
                        node_groups[node_label].append(item)
            
            except Exception as e:
                print(f"Lỗi khi tìm kiếm trong Neo4j: {e}")
    
        # Chuyển node_groups thành chuỗi JSON
        respone = {}
        respone["Person"]={}
        for key, value in node.items():
            respone["Person"][key] = value

        tags = [
            "CallLog", "CreditScore", "DriveLicense", 
            "Ecommerce", "Education", "InsuranceCard", "LandUseRightsCertificate", 
            "PersonIncomeTax", "PhoneSubscription", "SMSLog", 
            "SocialInsurance", "TrafficViolation", "VehicleRegistration", 
            "ViolationRisk", "latePaymentSocialInsurance"
        ]
        for tag in tags:
            respone[tag] = ""
        for label, items in node_groups.items():
            respone[label] = {}
            for index, item in enumerate(items):
                respone[label][index]={}
                for key, value in item["NodeKetNoi"].items():
                    respone[label][index][key]  = value
                    st.write(f" - **{key}:** {value}")

        # Trả về phản hồi hợp lệ dưới dạng JSON
        return jsonify(respone)

    except Exception as e:
        print(f"Lỗi chung trong quá trình xử lý dữ liệu: {e}")
        # Trả về thông báo lỗi
        return jsonify({"error": "Lỗi khi xử lý dữ liệu"}), 500
