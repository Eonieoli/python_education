# 3_exercise_solution.py

"""
Day 1 - 5교시: 문자열 메서드
Exercise - CSV 데이터 처리 (정답)
"""

# ============================================
# 주어진 데이터
# ============================================

user_data = "  KIM@EXAMPLE.COM  , 김철수 ,  SEOUL  , 010-1234-5678"


# ============================================
# 정답 코드
# ============================================

# 1. 쉼표로 데이터 분리
parts = user_data.split(",")

# 2. 각 부분 추출
email_raw = parts[0]
name_raw = parts[1]
city_raw = parts[2]
phone_raw = parts[3]

# 3. 이메일 정제 (공백 제거 + 소문자)
email = email_raw.strip().lower()

# 4. 이름 정제 (공백 제거)
name = name_raw.strip()

# 5. 도시명 정제 (공백 제거 + 대문자)
city = city_raw.strip().upper()

# 6. 전화번호 정제 (공백 제거 + 하이픈 제거)
phone = phone_raw.strip().replace("-", "")

# 결과 출력
print("이메일:", email)  # 출력: 이메일: kim@example.com
print("이름:", name)  # 출력: 이름: 김철수
print("도시:", city)  # 출력: 도시: SEOUL
print("전화번호:", phone)  # 출력: 전화번호: 01012345678
