# 2_practice.py

"""
Day 1 - 5교시: 문자열 메서드
Practice (강사와 함께 실습)

학습 목표:
- CSV 데이터 파싱하기
- 데이터 정제하기
- 텍스트 치환하기
"""

# ============================================
# 실습 1: CSV 데이터 파싱
# ============================================

# 쉼표로 구분된 상품 데이터
product_data = "노트북,1500000,삼성,10"

# 쉼표를 기준으로 데이터 분리
parts = product_data.split(",")

# 분리된 데이터 확인
print(parts)  # 출력: ['노트북', '1500000', '삼성', '10']

# 각 부분 추출 (인덱싱 활용)
product_name = parts[0]
price = parts[1]
brand = parts[2]
stock = parts[3]

# 결과 출력
print("상품명:", product_name)  # 출력: 상품명: 노트북
print("가격:", price)  # 출력: 가격: 1500000
print("브랜드:", brand)  # 출력: 브랜드: 삼성
print("재고:", stock)  # 출력: 재고: 10


# ============================================
# 실습 2: 데이터 정제 (strip + lower)
# ============================================

# 사용자가 입력한 이메일 (공백과 대문자 포함)
user_email = "  ADMIN@COMPANY.COM  "

# 공백 제거
cleaned_email = user_email.strip()
print(cleaned_email)  # 출력: ADMIN@COMPANY.COM

# 소문자로 변환
final_email = cleaned_email.lower()
print(final_email)  # 출력: admin@company.com

# 한 줄로 처리 (메서드 체이닝)
result_email = user_email.strip().lower()
print(result_email)  # 출력: admin@company.com


# ============================================
# 실습 3: 텍스트 치환 (replace)
# ============================================

# 게시글 내용에서 금지어를 순화어로 변경
post_content = "이 상품은 짱이에요! 완전 짱입니다!"

# '짱'을 '좋은'으로 변경
filtered_content = post_content.replace("짱", "좋은")
print(filtered_content)  # 출력: 이 상품은 좋은이에요! 완전 좋은입니다!

# 파일 경로에서 역슬래시를 슬래시로 변경
windows_path = "C:\\Users\\Documents\\file.txt"
unix_path = windows_path.replace("\\", "/")
print(unix_path)  # 출력: C:/Users/Documents/file.txt
