# 1_basic.py

"""
Day 1 - 5교시: 문자열 메서드
Basic (강사 시연용)

학습 목표:
- 메서드 개념 이해
- upper(), lower() 사용법
- strip()으로 공백 제거
- split()으로 문자열 분리
- replace()로 문자열 교체
"""

# ============================================
# 1. upper()와 lower() - 대소문자 변환
# ============================================

# 메서드는 .을 사용해서 호출합니다
name = "Python Programming"

# 모두 대문자로 변환
upper_name = name.upper()
print(upper_name)  # 출력: PYTHON PROGRAMMING

# 모두 소문자로 변환
lower_name = name.lower()
print(lower_name)  # 출력: python programming

# 원본은 변경되지 않습니다 (불변성)
print(name)  # 출력: Python Programming


# ============================================
# 2. strip() - 공백 제거
# ============================================

# 사용자 입력에는 공백이 많이 들어옵니다
user_input = "   hello world   "
print(user_input)  # 출력:    hello world   

# 양쪽 공백 제거
cleaned = user_input.strip()
print(cleaned)  # 출력: hello world

# 실전 예제: 이메일 주소 정제
email = "  user@example.com  "
clean_email = email.strip()
print(clean_email)  # 출력: user@example.com


# ============================================
# 3. split() - 문자열 분리
# ============================================

# 쉼표로 구분된 데이터 (CSV 형식)
data = "사과,바나나,딸기"

# 쉼표를 기준으로 분리 (리스트로 반환되지만 아직 안 배움)
parts = data.split(",")
print(parts)  # 출력: ['사과', '바나나', '딸기']

# 공백을 기준으로 분리
sentence = "Hello Python World"
words = sentence.split(" ")
print(words)  # 출력: ['Hello', 'Python', 'World']

# split() 괄호 안이 비어있으면 공백 기준
words2 = sentence.split()
print(words2)  # 출력: ['Hello', 'Python', 'World']


# ============================================
# 4. replace() - 문자열 교체
# ============================================

# 특정 문자열을 다른 문자열로 바꿉니다
message = "Hello World"

# World를 Python으로 교체
new_message = message.replace("World", "Python")
print(new_message)  # 출력: Hello Python

# 공백을 빈 문자열로 교체 (공백 제거)
no_space = message.replace(" ", "")
print(no_space)  # 출력: HelloWorld

# 실전 예제: 전화번호 형식 변경
phone = "010-1234-5678"
phone_no_dash = phone.replace("-", "")
print(phone_no_dash)  # 출력: 01012345678


# ============================================
# 5. 실전 예제 - 복합 활용
# ============================================

# 사용자 데이터 정제
user_data = "  HONG GIL DONG  "

# 1단계: 공백 제거
step1 = user_data.strip()
print(step1)  # 출력: HONG GIL DONG

# 2단계: 소문자 변환
step2 = step1.lower()
print(step2)  # 출력: hong gil dong

# 한 줄로 연결 (메서드 체이닝)
result = user_data.strip().lower()
print(result)  # 출력: hong gil dong


# CSV 데이터 처리 예제
csv_line = "김철수,30,서울,developer"

# 쉼표로 분리
data_parts = csv_line.split(",")
print(data_parts)  # 출력: ['김철수', '30', '서울', 'developer']

# 직업을 대문자로 변경하고 싶다면
job = data_parts[3]  # 인덱싱으로 직업 추출
job_upper = job.upper()
print(job_upper)  # 출력: DEVELOPER
