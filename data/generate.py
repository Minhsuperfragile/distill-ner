import random
from typing import *
import re
import os
from SimplerLLM.language.llm import LLM, LLMProvider
from dotenv import load_dotenv
load_dotenv()

class InfoGenerator:
    def __init__(self, 
                first_names: Iterable[LiteralString] = None, 
                middle_names: Iterable[LiteralString] = None, 
                last_names: Iterable[LiteralString] = None,
                year_range: Tuple[int, int] = None,
                company_types_sets: Iterable[LiteralString] = None,
                company_field_sets: Iterable[LiteralString] = None,
                street_sets: Iterable[LiteralString] = None,
                city_sets: Iterable[LiteralString] = None,
                district_sets: Iterable[LiteralString] = None,
                phuong_sets: Iterable[LiteralString] = None,
                bank_sets: Iterable[LiteralString] = None,
                ):
        self.first_names = first_names or ["Nguyễn", "Trần", "Lê", "Phạm", "Ngô", "Hoàng", "Huỳnh", "Phan", "Vũ", "Võ", "Đặng", "Bùi", "Đỗ", "Hồ", "Dương", "Lý"]
        self.middle_names = middle_names or ["Anh", "Bình", "Chí", "Quang", "Trung", "Đức", "Thanh", "Trường", "Ngọc", "Tài", "Nghĩa", "Ái", "Ánh", "Thị", "Văn", "Khánh"]
        self.last_names = last_names or ["Dũng", "Hà", "Minh", "Anh", "Quốc", "Cường", "Linh", "Thúy", "Thắng", "Thành", "Tâm", "Hưng", "Dương", "Vân", "Chi", "Huyền"]
        self.year_range = year_range or (2000, 2025)
        self.company_type_sets = company_types_sets or ["Công ty TNHH", "Công ty Cổ phần", "Công ty liên doanh", "Công ty", "Doanh nghiệp" , "Hợp tác xã", "Công ty TNHH 1 thành viên"]
        self.company_field_sets = company_field_sets or ["Xây dựng", "Giáo dục", "Thực phẩm", "Du lịch", "An ninh", "Kế toán", "Dịch vụ", "Công nghệ", "Phân phối", "Thời trang", "Điện tử"]
        self.street_sets = street_sets or ["Đường Hoàng Ngân", "Phố Phan Kế Bính", "Đường Khuất Duy Tiến", "Khu đô thị Dịch Vọng", "Phố Mai Dịch", "Đường Mễ Trì", "KDT Văn Phú", "KDT Xa La", "Làng Quốc Tế Thăng Long", "Làng Lụa Vạn Phúc"]
        self.district_sets = district_sets or ["Quận Cầu Giấy", "Huyện Chương Mỹ", "Quận Hà Đông", "Huyện Cát Hải", "Huyện Bạch Long Vĩ", "Quận 1", "Quận 7", "Quận 10", "Huyện Hòa Vang"]
        self.phuong_sets = phuong_sets or ["Phường An Phú", "Phường Bình Thạnh", "Phường Phúc Đồng", "Phường Quang Trung", "Phường Tân Định", "Phường Xuân Phương", "Phường Yên Hòa"]
        self.city_sets = city_sets or ["Hà Nội", "TP Hồ Chí Minh", "Đà Nẵng", "Hải Phòng"]
        self.bank_sets = bank_sets or ["VietcomBank", "TechcomBank", "BIDV", "ACB", "MBBank", "VietinBank", "Sacombank", "ShinhanBank", "TPBank"]

    def random_digits_seq(self, length:int ) -> str:
        return ''.join(random.choices('0123456789', k=length))

    def random_day(self) -> str:
        return f"{random.randint(1, 30)}"

    def random_month(self) -> str:
        return f"{random.randint(1, 12)}"

    def random_year(self, year_range: Tuple[int,int]= None) -> str:
        return str(random.randint(*self.year_range)) if (year_range is None) else str(random.randint(*year_range))

    def random_person_name(self) -> str:
        return f"{random.choice(self.first_names)} {random.choice(self.middle_names)} {random.choice(self.last_names)}"

    def random_company_name(self) -> str:
        return f"{random.choice(self.company_type_sets)} {random.choice(self.company_field_sets)} {random.choice(self.middle_names)} {random.choice(self.last_names)}"

    def random_price(self) -> str:
        return f"{random.randint(10, 999)},000,000 VND"

    def random_phone_number(self) -> str:
        return f'0{self.random_digits_seq(9)}'

    def random_email(self) -> str:
        domains = ["gmail.com", "yahoo.com", "hotmail.com"]
        name = f'{random.choice(self.middle_names)}{random.choice(self.last_names)}'
        name = self.to_non_accent_vietnamese(name)
        return f'{name}@{random.choice(domains)}'

    def to_non_accent_vietnamese(self,text):
        text = re.sub(r'A|Á|À|Ã|Ạ|Â|Ấ|Ầ|Ẫ|Ậ|Ă|Ắ|Ằ|Ẵ|Ặ', 'A', text)
        text = re.sub(r'a|à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ', 'a', text)
        text = re.sub(r'E|É|È|Ẽ|Ẹ|Ê|Ế|Ề|Ễ|Ệ', 'E', text)
        text = re.sub(r'e|è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ', 'e', text)
        text = re.sub(r'I|Í|Ì|Ĩ|Ị', 'I', text)
        text = re.sub(r'i|ì|í|ị|ỉ|ĩ', 'i', text)
        text = re.sub(r'O|Ó|Ò|Õ|Ọ|Ô|Ố|Ồ|Ỗ|Ộ|Ơ|Ớ|Ờ|Ỡ|Ợ', 'O', text)
        text = re.sub(r'o|ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ', 'o', text)
        text = re.sub(r'U|Ú|Ù|Ũ|Ụ|Ư|Ứ|Ừ|Ữ|Ự', 'U', text)
        text = re.sub(r'u|ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ', 'u', text)
        text = re.sub(r'Y|Ý|Ỳ|Ỹ|Ỵ', 'Y', text)
        text = re.sub(r'y|ỳ|ý|ỵ|ỷ|ỹ', 'y', text)
        text = re.sub(r'Đ', 'D', text)
        text = re.sub(r'đ', 'd', text)
        return text
    
    def random_date_of_birth(self, age_range: tuple) -> str:
        year = self.random_year(year_range= age_range)
        month = self.random_month()
        day = self.random_day()
        return f"{day}/{month}/{year}"

    def random_passport(self) -> str:
        start_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        passport_number = "".join(self.random_digits_seq(length=7))
        return f"{start_letter}{passport_number}"

    def random_cccd(self) -> str :
        return f'0{self.random_digits_seq(length=11)}'

    def random_business_number(self) -> str:
        return f'{self.random_digits_seq(length=10)}'
    
    def random_tax_code(self) -> str:
        return f'{self.random_digits_seq(length=10)}'

    def random_plate_number(self) -> str:
        return f'{self.random_digits_seq(length=2)}{random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}-{self.random_digits_seq(length=5)}'

    def random_social_insurance(self) -> str:
        return f'{self.random_digits_seq(length=10)}'
    
    def random_bank_name(self) -> str:
        return f'{random.choice(self.bank_sets)}'
    
    def random_bank_number(self) -> str: 
        return f'{self.random_digits_seq(length=8)}'
    
    def gemini_fill_the_rest(self, blank_text: str) -> str: 
        assert "GEMINI_API_KEY" in os.environ, "Please set GEMINI_API_KEY environment variable"
        gemini = LLM.create(
            provider=LLMProvider.GEMINI,
            model_name='gemini-1.5-flash'
        )

        gemini_response = gemini.generate_response(
            prompt=f"Điền vào chỗ trống thông tin ngẫu nhiên sao cho phù hợp với ngữ cảnh của văn bản:\n{blank_text}",
            max_tokens=400000,
        )

        return gemini_response

class AnnotationGenerator:
    def __init__(self):
        pass

if __name__ == "__main__":
    gen = InfoGenerator()
        
    for _ in range(10):
        print(gen.random_bank_name(), gen.random_bank_number())