from flask import Flask
from flask_cors import CORS
from backend.searching import app as searching


app = Flask(__name__)
CORS(app, supports_credentials=True, allow_headers=["Content-Type"])

@app.route('/')
def home():
    return 'Hello from Main Route'

app.register_blueprint(searching, url_prefix='/router1')

if __name__ == '__main__':
    app.run(port=5002) 