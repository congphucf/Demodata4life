<template lang="pug">
Page.dashboard( full-width style="position: relative; padding: 0; background-color: white;")
  Box(style="background-image: url(/bg-head.png); background-repeat: no-repeat; background-size: 150%;  margin-top: -20px; margin: 0; background-position: center top")
    Box.header(style="display: flex; margin-left: 7%;").middle
      img(
        src = "/huy-hieu-cong-an-nhan.png"
        style="margin-left: 50px; margin-top: 20px;"
        height="120px"
      )
      Box(style="display: flex; flex-direction: column; align-items: center; justify-content: center;")
        Text( variant="heading3xl" as="h1" style="font-size: 35px; color: #d71920; font-family: 'UTM-Alexander', sans-serif; ")  CỔNG TRA CỨU 
        Text(  variant="heading3xl" as="h1" style="font-size: 35px; color: #d71920; font-family: 'UTM-Alexander', sans-serif;") THÔNG TIN DÂN CƯ
    Box.search(style="position: relative;background-image: url(/sen.png); margin-top: -20px; background-size: 100%; height: 370px;")
      Box(style="margin-top:-25px; position: absolute; left: 50%; transform: translateX(-50%); display: flex; background-color: red; z-index: 20; width: 80vw; justify-content: space-between;")
        Box.filter(style="width: 25%;" @click="handleAction('so_dinh_danh')" :class="{ 'selected': identifier_type ==='so_dinh_danh'}")
          Text(as='h2' variant="headingMd" style="color: white; padding: 15px; font-size: 17px;") Tìm kiếm bằng số định danh
        Box.filter(style="width: 25%;" @click="handleAction('bien_so')" :class="{ 'selected': identifier_type === 'bien_so' }")
          Text(as='h2' variant="headingMd" style="color: white; padding: 15px; font-size: 17px;") Tìm kiếm bằng biển số xe
        Box.filter(style="width: 25%;" @click="handleAction('ma_so_bhyt')" :class="{ 'selected': identifier_type === 'ma_so_bhyt' }")
          Text(as='h2' variant="headingMd" style="color: white; padding: 15px; font-size: 17px;") Tìm kiếm bằng mã BHYT
        Box.filter(style="width: 25%;" @click="handleAction('hinh_anh')" :class="{ 'selected': identifier_type === 'hinh_anh' }")
          Text(as='h2' variant="headingMd" style="color: white; padding: 15px; font-size: 17px;") Tìm kiếm bằng hình ảnh
      Box.search-egnie(style=" height: 370px; ")
        Layout(style="margin-top: 55px;display: flex; justify-content: center; align-items: center;")
          LayoutSection(variant="oneHalf" style="margin-top: 55px; display: flex; justify-content: center; align-items: center;")
            Box
              Text(as='h2' variant="headingMd" style="margin: 2px; margin-bottom: 10px ;font-size: 20px; color: #d71920; font-family: 'UTM-Alexander', sans-serif; ") 6 Điều bác hồ dạy công an nhân dân
              Text(as='h2' variant="headingMd" style="margin: 2px; font-size: 17px; color: #d71920; font-family: 'UTM-Alexander', sans-serif; ") Đối với tự mình, phải cần, kiệm, liêm, chính
              Text(as='h2' variant="headingMd" style="margin: 2px;font-size: 17px; color: #d71920; font-family: 'UTM-Alexander', sans-serif; ") Đối với đồng sự, phải thân ái giúp đỡ
              Text(as='h2' variant="headingMd" style="margin: 2px;font-size: 17px; color: #d71920; font-family: 'UTM-Alexander', sans-serif; ") Đối với Chính phủ, phải tuyệt đối trung thành
              Text(as='h2' variant="headingMd" style="margin: 2px;font-size: 17px; color: #d71920; font-family: 'UTM-Alexander', sans-serif; ") Đối với nhân dân, phải kính trọng, lễ phép
              Text(as='h2' variant="headingMd" style="margin: 2px;font-size: 17px; color: #d71920; font-family: 'UTM-Alexander', sans-serif; ") Đối với công việc, phải tận tụy
              Text(as='h2' variant="headingMd" style="margin: 2px;font-size: 17px; color: #d71920; font-family: 'UTM-Alexander', sans-serif; ") Đối với địch, phải cương quyết, khôn khéo.

          LayoutSection(variant="oneHalf")
            Box.search-bar(style="display: flex; align-items: center; background-color: white; height: 50px; border: 1px solid #f0e3af; border-radius: 5px; padding: 5px; margin-right: 50px; width: 60%; display: flex; justify-content: space-between;")
              input.search-input(v-if="identifier_type !== 'hinh_anh'" type="text" v-model="key" placeholder="Nhập từ khoá tìm kiếm" style="flex: 1; border: none; font-size: 16px; outline: none; ")
              Box(v-else)
                input#fileInput(type="file" @change="handleImageUpload" style="display: none;")
                label.custom-file-button(for="fileInput" style="padding: 10px; background-color: #d80000; color: #ddd; font-weight: bold; border-radius: 10px; margin-right: 20px;") Chọn tệp
                span.custom-file-text(v-if="imageName") {{ imageName }}
                span.custom-file-text(v-else) Không có tệp nào được chọn
              div.search-button(@click="handleSearch" style="background-color: #d80000; border: none; width: 40px; height: 40px; border-radius: 5px; display: flex; align-items: center; justify-content: center; cursor: pointer;") 
                img(
                  src="/search.png"
                  width="80%"
                )

      Box.maincontent(v-if="personInfor!=null" style="width: 80%; margin-left: 10%; padding: 30px; min-height: 200px;")  
        Text(as='h2' variant="headingLg" style="margin-bottom: 20px;") Đã tìm được người phù hợp
        Box(style="margin-bottom: 0")
          Box( @click="toggleExpand(-1)" style="cursor: pointer; padding: 10px; background: #f5f5f5; border: 1px solid #ddd; border-radius: 10px; display: flex; justify-content: space-between; margin-bottom: 20px;")
            Text(v-if= "personInfor.Person" as = "h2"  variant="headingLg" ) 
              img(src="/cccd.png" alt="icon" style=" height: 20px; margin-right: 8px;")
              |Thông tin cá nhân
            Box
              img(v-if="expandedBoxes.includes(-1)" src="/angle-down.png" height="20px")
              img(v-else src="/angle-right.png" height="20px")
          
          Card(v-if="expandedBoxes.includes(-1)")
            Layout
              LayoutSection(variant="oneThird")
                Text(style="padding: 7px; font-size: 15px;")
                  strong Họ và tên: 
                  | {{ personInfor.Person.ho_va_ten }}
                Text(style="padding: 7px; font-size: 15px;")
                  strong Ngày sinh: 
                  | {{ personInfor.Person.ngay_sinh }}
                Text(style="padding: 7px; font-size: 15px;")
                  strong Quốc tịch: 
                  | {{ personInfor.Person.quoc_tich }}

              LayoutSection(variant="oneThird")
                Text(style="padding: 7px; font-size: 15px;")
                  strong Giới tính: 
                  | {{ personInfor.Person.gioi_tinh }}
                Text(style="padding: 7px; font-size: 15px;")
                  strong Nhóm máu: 
                  | {{ personInfor.Person.nhom_mau }}
                Text(style="padding: 7px; font-size: 15px;")
                  strong Tình trạng hôn nhân: 
                  | {{ personInfor.Person.tinh_trang_hon_nhan }}

              LayoutSection(variant="oneThird")
                Text(style="padding: 7px; font-size: 15px;")
                  strong Dân tộc: 
                  | {{ personInfor.Person.dan_toc }}
                Text(style="padding: 7px; font-size: 15px;")
                  strong Tôn giáo: 
                  | {{ personInfor.Person.ton_giao }}
                Text(style="padding: 7px; font-size: 15px;")
                  strong Số định danh cá nhân: 
                  | {{ personInfor.Person.so_dinh_danh }}

            Layout
              LayoutSection(variant="oneHalf")
                Text(style="padding: 7px; font-size: 15px;")
                  strong Quê quán: 
                  | {{ personInfor.Person.que_quan_huyen }}, {{ personInfor.Person.que_quan_tinh }}, {{ personInfor.Person.que_quan_xa }}
                Text(style="padding: 7px; font-size: 15px;")
                  strong Nơi thường trú: 
                  | {{ personInfor.Person.noi_thuong_tru_huyen }}, {{ personInfor.Person.noi_thuong_tru_tinh }}, {{ personInfor.Person.noi_thuong_tru_xa }}
                Text(style="padding: 7px; font-size: 15px;")
                  strong Quốc tịch cha: 
                  | {{ personInfor.Person.quoc_tich_cha }}
                Text(style="padding: 7px; font-size: 15px;")
                  strong Số định danh cá nhân của cha: 
                  | {{ personInfor.Person.so_ddcn_cha }}
                Text(style="padding: 7px; font-size: 15px;")
                  strong Quốc tịch vợ/chồng: 
                  | {{ personInfor.Person.quoc_tich_vo_chong }}
                Text(style="padding: 7px; font-size: 15px;")
                  strong Số định danh cá nhân của vợ/chồng: 
                  | {{ personInfor.Person.so_ddcn_vo_chong }}

              LayoutSection(variant="oneHalf")
                Text(style="padding: 7px; font-size: 15px;")
                  strong Nơi khai sinh: 
                  | {{ personInfor.Person.noi_khai_sinh_huyen }}, {{ personInfor.Person.noi_khai_sinh_tinh }}, {{ personInfor.Person.noi_khai_sinh_xa }}
                Text(style="padding: 7px; font-size: 15px;")
                  strong Nơi ở hiện tại: 
                  | {{ personInfor.Person.noi_o_hien_tai_huyen }}, {{ personInfor.Person.noi_o_hien_tai_tinh }}, {{ personInfor.Person.noi_o_hien_tai_xa }}
                Text(style="padding: 7px; font-size: 15px;")
                  strong Quốc tịch mẹ: 
                  | {{ personInfor.Person.quoc_tich_me }}
                Text(style="padding: 7px; font-size: 15px;")
                  strong Số định danh cá nhân của mẹ: 
                  | {{ personInfor.Person.so_ddcn_me }}
                Text(style="padding: 7px; font-size: 15px;")
                  strong Quan hệ với chủ hộ: 
                  | {{ personInfor.Person.quan_he_voi_chu_ho }}
                Text(style="padding: 7px; font-size: 15px;")
                  strong Số định danh cá nhân của chủ hộ: 
                  | {{ personInfor.Person.so_ddcn_chu_ho }}

        Box(v-for="(tag, tagIndex) in tagAttributes" :key="tagIndex" style="margin-bottom: 20px;")
          
          Box(v-if="personInfor[tag.tag.name]" @click="toggleExpand(tagIndex)" style="cursor: pointer; padding: 10px; background: #f5f5f5; border: 1px solid #ddd; border-radius: 10px; display: flex; justify-content: space-between; margin-bottom: 20px;")
            Text(as="h2" variant="headingLg" style="font-weight: 600; font-family: 'Roboto Bold', sans-serif; display: flex; align-items: center;")
              img(src="/icon-tt.png" alt="icon" style="width: 20px; margin-right: 8px;")
              | {{ tag.tag.vietnamese }}
            Box
              img(v-if="expandedBoxes.includes(tagIndex)" src="/angle-down.png" height="20px")
              img(v-else src="/angle-right.png" height="20px")
              
          
          transition(name="fade")
            Box(v-if="expandedBoxes.includes(tagIndex)")
              Grid(:columns="{ xs: 1, sm: 1, md: 2, lg: 2, xl: 3 }")
                Card(v-for="(item, index) in personInfor[tag.tag.name]" :key="index")
                  div(v-for="(attribute, attributeIndex) in tag.attributes" :key="attributeIndex")
                    Text(variant="bodyLg" as="p" style="padding: 7px; font-size: 15px;") 
                      strong {{ attribute.vietnamese }}: 
                      | {{ item[attribute.name] }}
      Box.search(style="position: relative;background-image: url(/bg-bca-footer-1.png); background-size: 100%; height: 200px; background-position: center; margin-top: 100px; ")   
        
</template>

<script setup lang="ts">
import { Layout, LayoutSection } from '@ownego/polaris-vue';
import {ref} from 'vue';
import axios from 'axios';

const tagAttributes = [
  { tag: {name:"CallLog", vietnamese: "Lich sử cuộc gọi"}, attributes: [
    { name: "thoi_diem_bat_dau", vietnamese: "Thời điểm bắt đầu" },
    { name: "id_bts_nguoi_goi", vietnamese: "ID BTS người gọi" },
    { name: "so_dien_thoai_nguoi_nhan", vietnamese: "Số điện thoại người nhận" },
    { name: "id_bts_nguoi_nhan", vietnamese: "ID BTS người nhận" },
    { name: "so_dien_thoai_nguoi_goi", vietnamese: "Số điện thoại người gọi" },
    { name: "thoi_gian_goi", vietnamese: "Thời gian gọi" }
  ]},
  { tag: {name: "CreditScore", vietnamese: "Lịch sử tín dụng"}, attributes: [
    { name: "so_cccd", vietnamese: "Số CCCD" },
    { name: "ho_va_ten", vietnamese: "Họ và tên" },
    { name: "no_xau_vnd", vietnamese: "Nợ xấu (VND)" },
    { name: "ma_so_thong_tin_tin_dung", vietnamese: "Mã số thông tin tín dụng" },
    { name: "so_tien_cham_thanh_toan", vietnamese: "Số tiền chậm thanh toán" },
    { name: "dia_chi", vietnamese: "Địa chỉ" },
    { name: "ngay_bao_cao_gan_nhat", vietnamese: "Ngày báo cáo gần nhất" },
    { name: "loai_no", vietnamese: "Loại nợ" },
    { name: "has_credit_info", vietnamese: "Có thông tin tín dụng" },
    { name: "tong_du_no_the_tin_dung", vietnamese: "Tổng dư nợ thẻ tín dụng" },
    { name: "to_chuc_tin_dung", vietnamese: "Tổ chức tín dụng" },
    { name: "tong_du_no_vnd", vietnamese: "Tổng dư nợ (VND)" }
  ]},
  { tag: {name: "DriveLicense", vietnamese: "Bằng lái xe"}, attributes: [
    { name: "so_cccd", vietnamese: "Số CCCD" },
    { name: "ngay_het_han", vietnamese: "Ngày hết hạn" },
    { name: "ngay_hieu_luc", vietnamese: "Ngày hiệu lực" },
    { name: "ngay_sinh", vietnamese: "Ngày sinh" },
    { name: "loai_bang", vietnamese: "Loại bằng" }
  ]},
  { tag: {name: "Ecommerce", vietnamese: "Thương mại điên tử"}, attributes: [
    { name: "so_cccd", vietnamese: "Số CCCD" },
    { name: "dia_chi_giao_hang", vietnamese: "Địa chỉ giao hàng" },
    { name: "loai_hang", vietnamese: "Loại hàng" },
    { name: "so_dien_thoai_cua_hang", vietnamese: "Số điện thoại cửa hàng" },
    { name: "ma_so_thue_cua_hang", vietnamese: "Mã số thuế cửa hàng" },
    { name: "so_dien_thoai_nguoi_mua", vietnamese: "Số điện thoại người mua" },
    { name: "dia_chi_cua_hang", vietnamese: "Địa chỉ cửa hàng" },
    { name: "san_thuong_mai_dien_tu", vietnamese: "Sàn thương mại điện tử" },
    { name: "hinh_thuc_thanh_toan", vietnamese: "Hình thức thanh toán" },
    { name: "tong_tien", vietnamese: "Tổng tiền" }
  ]},
  { tag: {name: "Education" , vietnamese: "Giáo dục"}, attributes: [
    { name: "so_cccd", vietnamese: "Số CCCD" },
    { name: "ma_don_vi_dao_tao", vietnamese: "Mã đơn vị đào tạo" },
    { name: "bang_cap", vietnamese: "Bằng cấp" },
    { name: "NGAY_SINH", vietnamese: "Ngày sinh" },
    { name: "ten_don_vi_dao_tao", vietnamese: "Tên đơn vị đào tạo" },
    { name: "thoi_diem_bat_dau", vietnamese: "Thời điểm bắt đầu" },
    { name: "thoi_diem_ket_thuc", vietnamese: "Thời điểm kết thúc" }
  ]},
  { tag: {name:"InsuranceCard", vietnamese: "Bảo hiển y tế"}, attributes: [
    { name: "ma_dkkcb", vietnamese: "Mã DKKB" },
    { name: "ngay_het_hieu_luc", vietnamese: "Ngày hết hiệu lực" },
    { name: "ten_don_vi_mua_bhyt", vietnamese: "Tên đơn vị mua BHYT" },
    { name: "ngay_bat_dau_hieu_luc", vietnamese: "Ngày bắt đầu hiệu lực" },
    { name: "ten_dkkcb", vietnamese: "Tên DKKB" },
    { name: "ma_don_vi_mua_bhyt", vietnamese: "Mã đơn vị mua BHYT" },
    { name: "so_cccd", vietnamese: "Số CCCD" },
    { name: "ma_so_bhyt", vietnamese: "Mã số BHYT" }
  ]},
  { tag: {name: "LandUseRightsCertificate" , vietnamese: "Giấy chứng nhận quyền sử dụng đất"}, attributes: [
    { name: "so_cccd", vietnamese: "Số CCCD" },
    { name: "ma_so_giay_chung_nhat_qsd", vietnamese: "Mã số giấy chứng nhận QSD" },
    { name: "dien_tich", vietnamese: "Diện tích" },
    { name: "dia_chi_thua_dat", vietnamese: "Địa chỉ thửa đất" },
    { name: "ho_va_ten", vietnamese: "Họ và tên" }
  ]},

  { tag: {name:"PersonalIncomeTax", vietnamese: "Thuế thu nhập cá nhân"}, attributes: [
    { name: "so_cccd", vietnamese: "Số CCCD" },
    { name: "ten_to_chuc_tra_thu_nhap", vietnamese: "Tên tổ chức trả thu nhập" },
    { name: "so_nguoi_phu_thuoc", vietnamese: "Số người phụ thuộc" },
    { name: "so_tien_giam_tru", vietnamese: "Số tiền giảm trừ" },
    { name: "tu_thien_nhan_dao_khuyen_hoc", vietnamese: "Từ thiện nhân đạo khuyến học" },
    { name: "quy_huu_tri_tu_nguyen", vietnamese: "Quỹ hưu trí tự nguyện" },
    { name: "thu_nhap_chiu_thue", vietnamese: "Thu nhập chịu thuế" },
    { name: "ma_so_thue_to_chuc_tra_thu_nhap", vietnamese: "Mã số thuế tổ chức trả thu nhập" },
    { name: "bao_hiem_duoc_tru", vietnamese: "Bảo hiểm được trừ" },
    { name: "ma_so_thue", vietnamese: "Mã số thuế" },
    { name: "nam_tinh_thue", vietnamese: "Năm tính thuế" },
    { name: "so_tien_khau_tru", vietnamese: "Số tiền khấu trừ" }
  ]},
  { tag: {name:"PhoneSubscription", vietnamese: "Số điện thoại"}, attributes: [
    { name: "so_cccd", vietnamese: "Số CCCD" },
    { name: "dia_chi", vietnamese: "Địa chỉ" },
    { name: "so_dien_thoai", vietnamese: "Số điện thoại" },
    { name: "loai_hinh", vietnamese: "Loại hình" },
    { name: "thoi_diem_dang_ky", vietnamese: "Thời điểm đăng ký" }
  ]},
  { tag: {name: "SMSLog" , vietnamese: "Lịch sử tin nhắn"}, attributes: [
    { name: "thoi_diem_bat_dau", vietnamese: "Thời điểm bắt đầu" },
    { name: "id_bts_nguoi_goi", vietnamese: "ID BTS người gọi" },
    { name: "so_sms", vietnamese: "Số SMS" },
    { name: "so_dien_thoai_nguoi_nhan", vietnamese: "Số điện thoại người nhận" },
    { name: "id_bts_nguoi_nhan", vietnamese: "ID BTS người nhận" },
    { name: "so_dien_thoai_nguoi_goi", vietnamese: "Số điện thoại người gọi" }
  ]},
  { tag: {name: "SocialInsurance", vietnamese: "Bảo hiểm xã hội"}, attributes: [
    { name: "so_cccd", vietnamese: "Số CCCD" },
    { name: "thoi_diem_bat_dau", vietnamese: "Thời điểm bắt đầu" },
    { name: "thoi_diem_ket_thuc", vietnamese: "Thời điểm kết thúc" },
    { name: "ma_so_bhxh", vietnamese: "Mã số BHXH" },
    { name: "tien_luong_dong_bao_hiem", vietnamese: "Tiền lương đóng bảo hiểm" },
    { name: "nghe_nghiep", vietnamese: "Nghề nghiệp" },
    { name: "ten_don_vi", vietnamese: "Tên đơn vị" },
    { name: "ma_don_vi", vietnamese: "Mã đơn vị" },
    { name: "he_so_luong", vietnamese: "Hệ số lương" }
  ]},
  { tag: "TrafficViolation", attributes: [
    { name: "ngay_vi_pham", vietnamese: "Ngày vi phạm" },
    { name: "loai_vi_pham", vietnamese: "Loại vi phạm" },
    { name: "bien_so", vietnamese: "Biển số" },
    { name: "tinh_trang_nop", vietnamese: "Tình trạng nộp" },
    { name: "so_tien_nop", vietnamese: "Số tiền nộp" }
  ]},
  { tag: {name:"VehicleRegistration" , vietnamese: "GIấy đăng ký phương tiện"}, attributes: [
    { name: "so_cccd", vietnamese: "Số CCCD" },
    { name: "loai_bang", vietnamese: "Loại bằng" },
    { name: "so_may", vietnamese: "Số máy" },
    { name: "bien_so", vietnamese: "Biển số" },
    { name: "hang_xe", vietnamese: "Hãng xe" },
    { name: "dung_tich_xi_lanh", vietnamese: "Dung tích xi lanh" },
    { name: "thoi_diem_dang_ky", vietnamese: "Thời điểm đăng ký" },
    { name: "so_khung", vietnamese: "Số khung" }
  ]},
  { tag: {name: "ViolationRisk", vietnamese: "Rủi ro vi phạm"}, attributes: [
    { name: "ho_va_ten", vietnamese: "Họ và tên" },
    { name: "nguy_co_vi_pham", vietnamese: "Nguy cơ vi phạm" },
    { name: "so_dinh_danh", vietnamese: "Số định danh" },
    { name: "address", vietnamese: "Địa chỉ" }
  ]},
  { tag: {name: "latePaymentSocialInsurance",vietnamese: "Chậm đóng bảo hiểm xã hội"}, attributes: [
    { name: "so_cccd", vietnamese: "Số CCCD" },
    { name: "tong_thoi_gian_tham_gia_bhxh", vietnamese: "Tổng thời gian tham gia BHXH" },
    { name: "tong_thoi_gian_cham_dong", vietnamese: "Tổng thời gian chậm đóng" },
    { name: "ma_so_bhxh", vietnamese: "Mã số BHXH" }
  ]}

  
];
const identifier_type = ref("so_dinh_danh")
const key = ref("");
const personInfor = ref(null);

const image = ref(null);
const imageName = ref("");

const handleAction = (identifier_choose) => {
  identifier_type.value = identifier_choose;
  console.log(identifier_type.value)
  key.value = "";
  personInfor.value = null;
}
const expandedBoxes = ref([]);

// Function to toggle box expansion
const toggleExpand = (index) => {
  if (expandedBoxes.value.includes(index)) {
    // Remove index if already expanded
    expandedBoxes.value = expandedBoxes.value.filter((i) => i !== index);
  } else {
    // Add index to expanded list
    expandedBoxes.value.push(index);
  }
};

function handleImageUpload(event) {
  const file = event.target.files[0];
  if (file) {
    // Create a URL for the uploaded image
    image.value = file;
    imageName.value = file.name; 
    console.log('Selected image:', image.value);
  }
 else {
    imageName.value = "Không có tệp nào được chọn";
  }
}

const handleSearch = async () => {
  const identifierType = identifier_type.value; // Loại identifier, ở đây là 'so_dinh_danh'
  var identifier;
  personInfor.value = null;
  if (identifierType!='hinh_anh'){
    identifier = key.value;
  }
  else{
    identifier = image.value;
  }

  try {
    let formData = new FormData();

    if (identifierType !== 'hinh_anh') {
      formData.append('identifier', key.value); // Gửi chuỗi
    } else {
      if (!image.value) {
        console.error('No image selected.');
        return;
      }
      formData.append('identifier', image.value); // Gửi file ảnh
    }

    formData.append('identifier_type', identifierType);

    const response = await axios.post('http://localhost:5002/router1/getinformation', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    personInfor.value = response.data;
    console.log('Dữ liệu nhận được từ backend:', personInfor.value);
  } catch (error) {
    console.error('Có lỗi xảy ra khi gửi yêu cầu:', error);
  }
};



</script>

<style lang="scss">
.middle{
  align-items: center;
}

.search{
  background-color: white;
  height: 100px;
  position: relative; 
  z-index: 10;
}

.card {
  width: 300px;
  background-color: #f0f0f0;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;

  .card-header {
    background-color: #d32f2f;
    color: white;
    padding: 16px;
    font-size: 18px;
    font-weight: bold;
    display: flex;
    align-items: center;

    .icon {
      margin-right: 8px;
    }
  }

  .card-content {
    padding: 16px;
    font-size: 16px;
    color: #333;
  }

  .card-footer {
    background-color: #f0f0f0;
    padding: 8px;
    text-align: center;

    .btn {
      padding: 8px 16px;
      background-color: #d32f2f;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;

      &:hover {
        background-color: #b71c1c;
      }
    }
  }
}

.search-bar {
  display: flex;
  align-items: center;
  background-color: #fffbe3; // Màu nền thanh tìm kiếm
  height: 50px;
  border: 1px solid #f0e3af;
  border-radius: 5px;
  padding: 5px;

  .search-input {
    flex: 1; // Đảm bảo input chiếm toàn bộ chiều ngang còn lại
    border: none;
    padding: 0 10px;
    font-size: 16px;
    outline: none; // Loại bỏ đường viền khi click
  }

  .advanced-search {
    margin: 0 10px;
    font-size: 16px;
    color: #1a1a1a; // Màu chữ
    cursor: pointer;
  }

  .search-button {
    background-color: #d80000; // Màu nền nút
    border: none;
    width: 40px;
    height: 40px;
    border-radius: 5px; // Bo góc
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;

    .fa-search {
      color: white; // Màu biểu tượng
      font-size: 18px;
    }
  }
}

.filter{
  display: flex;
  justify-content: center;
  align-items: center;

}
.filter:hover{
    background-color: #8c2525;
  }
.selected {
  background-color: #8c2525 !important;
  color: white; /* Màu chữ khi chọn */
}
.search-button:hover{
  background-color: #8c2525 !important;
}
.custom-file-button:hover{
  background-color: #8c2525 !important;
}

</style>