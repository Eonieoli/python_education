# 3_advanced_solution.py

"""
Day 1 - 8교시: 종합 실습
🔴 도전 Problem - 데이터 처리 프로그램 (정답)
"""

# ============================================
# 정답 코드
# ============================================

# 1. CSV 데이터 입력받기
data = input("CSV 데이터를 입력하세요 (이름,나이,이메일): ")

# 2. 데이터 분리하기 (쉼표로 분리)
parts = data.split(',')
name_raw = parts[0]      # 첫 번째 항목
age_raw = parts[1]       # 두 번째 항목
email_raw = parts[2]     # 세 번째 항목

# 3. 이름 정제하기
name_clean = name_raw.strip()             # 공백 제거
name_parts = name_clean.split()           # 공백으로 분리
first_name = name_parts[0][0].upper() + name_parts[0][1:].lower()   # 첫 단어
last_name = name_parts[1][0].upper() + name_parts[1][1:].lower()    # 두 번째 단어
full_name = first_name + " " + last_name  # 두 단어 합치기

# 4. 나이 정제하기
age_clean = int(age_raw.strip())

# 5. 이메일 정제하기
email_clean = email_raw.strip().lower()

# 6. 결과 출력
print("========================================")
print("        데이터 처리 결과")
print("========================================")
print(f"원본: {data}")
print("----------------------------------------")
print(f"이름: {full_name}")
print(f"나이: {age_clean}세")
print(f"이메일: {email_clean}")
print("========================================")
