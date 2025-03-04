r1_template_en = """According to the given document inside <document>, extract the following information:
- Personal or Business Name
- Address
- Phone Number
- Email Address
- Contract price number
- Company registration number
- Date of Birth
- Passport Number
- Citizen identification number (CCCD)
- Personal or business tax code 
- License plate number
- Social insurance number
- Bank account number
- Bank service provider

<document>
 {document}
</document>

Return the extracted information in a JSON format, if any field is not found, return "N/A" for that field.

Example: 
<document>
ABC Company Limited has business registration code 0101234567, address at 123 XYZ Street, Hoan Kiem District, Hanoi.
Mr. Nguyen Van A, born on January 1, 1990, has CCCD 0123456789, phone number 0912345678, email vana@gmail.com, and personal tax code 8012345678.
Mr. A signed a contract worth 10,000,000 VND with the company. Mr. A's motorbike has license plate number 29A1-12345. Mr. A's social insurance number is 1234567890.
Mr. A's bank account number is 00112233445566, Vietcombank.
</document>

Output: 
{{
    "Name" : {{"Personal" : "Nguyen Van A", "Business": "ABC Company Limited"}}, 
    "Address" : "123 XYZ Street, Hoan Kiem District, Hanoi",
    "Phone number" : "0912345678",
    "Email" : "vana@gmail.com",
    "CCCD" : "0123456789",
    "Passport number" : "N/A",
    "Contract price number": "10,000,000",
    "Business registration code": "0101234567",
    "Date of birth: "01/01/1990",
    "Tax code": {{"Personal": "8012345678", "Business": "N/A"}}
    "License plate number": "29A1-12345",
    "Social insurance number": "1234567890",
    "Bank information" : {{"Bank account number": "00112233445566", "Bank service provider": "Vietcombank"}}
}}
"""

r1_template_vi = """Dựa vào văn bản bên trong <document>, trích xuất các thông tin sau:
- Tên riêng (cá nhân hoặc doanh nghiệp)
- Địa chỉ 
- Số điện thoại
- Địa chỉ email
- Giá tiền hợp đồng
- Mã số đăng ký doanh nghiệp
- Ngày sinh 
- Số passport
- Số căn cước công dân (CCCD)
- Mã số thuế (cá nhân hoặc doanh nghiệp)
- Biển số xe
- Mã số bảo hiểm xã hội
- Số tài khoản ngân hàng
- Thông tin về ngân hàng

<document>
 {document}
</document>

Trả về dữ liệu thu được dưới dạng JSON, nếu có trường thông tin này không tồn tại thì điển null.

Ví dụ
<document>
Công ty TNHH ABC có mã số đăng ký doanh nghiệp là 0101234567, địa chỉ tại số 123 đường XYZ, quận Hoàn Kiếm, Hà Nội. Ông Nguyễn Văn A, sinh ngày 01/01/1990, có CCCD 0123456789, số điện thoại 0912345678, email vana@gmail.com, và mã số thuế cá nhân 8012345678. Ông A ký hợp đồng trị giá 10.000.000 VNĐ với công ty. Xe máy của ông A có biển số 29A1-12345. Số bảo hiểm xã hội của ông A là 1234567890. Số tài khoản ngân hàng của ông A là 00112233445566, ngân hàng Vietcombank.
</document>

Output: 
{{
    "Tên riêng" : {{"Cá nhân" : "Nguyen Van A", "Doanh nghiệp": "Công ty TNHH ABC"}}, 
    "Địa chỉ" : "123 đường XYZ, quận Hoàn Kiếm, Hà Nội",
    "Số điện thoại" : "0912345678",
    "Email" : "vana@gmail.com",
    "Căn cước công dân (CCCD)" : "0123456789",
    "Số passport" : "N/A",
    "Giá tiền hợp đồng": "10,000,000",
    "Mã đăng ký doanh nghiệp" : "0101234567",
    "Ngày sinh": "01/01/1990",
    "Mã số thuế": {{"Cá nhân": "8012345678", "Doanh nghiệp": "N/A"}}
    "Biển số xe": "29A1-12345",
    "Số bảo hiểm xã hội": "1234567890",
    "Thông tin ngân hàng" : {{"Số tài khoản": "00112233445566", "Ngân hàng": "Vietcombank"}}
}}
"""

qwen25_system_prompt_en = """You are an AI data extraction assistant. Your task is to analyze a given document and extract specific structured information. Follow these steps strictly:
1. Verification:
- First, check whether each piece of information is explicitly stated in the document.
- If a data point is not found, do not infer or assume missing details.
- Clearly  mark missing information as "null" in the output.
2. Extraction:
Extract the following information from the document:
- Personal or Business Name
- Address
- Phone Number
- Email Address
- Contract price number
- Company registration number
- Date of Birth
- Passport Number
- Citizen identification number (CCCD)
- Personal or business tax code 
- License plate number
- Social insurance number
- Bank account number
- Bank service provider
3. Formatting:
Return the extracted information in the following JSON format, without any additional text:
{{
    "Name" : {{"Personal" : "Nguyen Van A", "Business": "ABC Company Limited"}}, 
    "Address" : "123 XYZ Street, Hoan Kiem District, Hanoi",
    "Phone number" : "0912345678",
    "Email" : "vana@gmail.com",
    "CCCD" : "0123456789",
    "Passport number" : "N/A",
    "Contract price number": "10,000,000",
    "Business registration code": "0101234567",
    "Date of birth: "01/01/1990",
    "Tax code": {{"Personal": "8012345678", "Business": "N/A"}}
    "License plate number": "29A1-12345",
    "Social insurance number": "1234567890",
    "Bank information" : {{"Bank account number": "00112233445566", "Bank service provider": "Vietcombank"}}
}}
"""

qwen25_template_en = """According to the given document below, extract information.
Document: {document}`
"""
test_case_en = """Sales contract No. 20231201 between Gia Khang Electronics Company Limited, Tax code 0312345678, address 12 Nguyen Hue, District 1, Ho Chi Minh City, and Mr. Tran Van Binh, date of birth July 15, 1985, CCCD 079123456789, phone number 0901234567, email vanbinh@gmail.com. The contract value is 50,000,000 VND. Mr. Binh paid through bank account 190387654321, Techcombank."""

test_case_vi = """Hợp đồng mua bán số 20231201 giữa Công ty TNHH Điện tử Gia Khang, MST 0312345678, địa chỉ 12 Nguyễn Huệ, Quận 1, TP.HCM, và ông Trần Văn Bình, sinh ngày 15/07/1985, CCCD 079123456789, số điện thoại 0901234567, email vanbinh@gmail.com. Giá trị hợp đồng là 50.000.000 VNĐ. Ông Bình thanh toán qua tài khoản ngân hàng 190387654321, ngân hàng Techcombank."""

test_result_check_en = {
    "Name" : {"Personal" : "Nguyen Van A", "Business": "ABC Company Limited"}, 
    "Address" : "123 XYZ Street, Hoan Kiem District, Hanoi",
    "Phone number" : "0912345678",
    "Email" : "vana@gmail.com",
    "CCCD" : "0123456789",
    "Passport number" : "N/A",
    "Contract price number": "10,000,000",
    "Business registration code": "0101234567",
    "Date of birth": "01/01/1990",
    "Tax code": {"Personal": "8012345678", "Business": "N/A"},
    "License plate number": "29A1-12345",
    "Social insurance number": "1234567890",
    "Bank information" : {"Bank account number": "00112233445566", "Bank service provider": "Vietcombank"}
}