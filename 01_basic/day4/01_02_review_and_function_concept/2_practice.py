# 2_practice.py

"""
Day 4 - 2교시: 함수 기본
Practice (강사와 함께 실습)

학습 목표:
- 계산 함수 만들기
- 문자열 처리 함수 만들기
- 여러 값 반환하는 함수 만들기 (튜플 언패킹!)
"""

# ============================================
# 실습 1: 첫 함수 만들기 (처음부터 끝까지 타이핑!)
# ============================================

# 인사 함수 정의 - 이름을 받아서 인사말 반환
def greet(name):
    return f"안녕하세요, {name}님!"

# 함수 호출
message = greet("홍길동")
print(message)  # 출력: 안녕하세요, 홍길동님!

message = greet("김철수")
print(message)  # 출력: 안녕하세요, 김철수님!


# ============================================
# 실습 2: 계산 함수 만들기 (TODO)
# ============================================

# TODO: 두 숫자를 더하는 함수 add를 작성하세요
# 힌트: def add(a, b): return a + b
def add(a, b):
    return a + b

result = add(10, 20)
print(f"10 + 20 = {result}")  # 출력: 10 + 20 = 30


# TODO: 두 숫자를 곱하는 함수 multiply를 작성하세요
# 힌트: def multiply(a, b): return a * b
def multiply(a, b):
    return a * b

result = multiply(5, 7)
print(f"5 × 7 = {result}")  # 출력: 5 × 7 = 35


# ============================================
# 실습 3: 문자열 처리 함수 만들기 (TODO)
# ============================================

# TODO: 문자열을 대문자로 변환하는 함수 to_upper를 작성하세요
# 힌트: def to_upper(text): return text.upper()
def to_upper(text):
    return text.upper()

result = to_upper("hello")
print(result)  # 출력: HELLO


# TODO: 문자열 길이를 반환하는 함수 get_length를 작성하세요
# 힌트: def get_length(text): return len(text)
def get_length(text):
    return len(text)

result = get_length("Python")
print(f"'Python'의 길이: {result}")  # 출력: 'Python'의 길이: 6


# ============================================
# 실습 4: 여러 값 반환하기 ⭐ (TODO)
# ============================================
# Day 2에서 배운 튜플 언패킹을 활용합니다!

# TODO: 직사각형의 넓이와 둘레를 함께 반환하는 함수를 작성하세요
# 힌트: 
#   def calculate_rectangle(width, height):
#       area = width * height
#       perimeter = 2 * (width + height)
#       return area, perimeter  # 두 개 반환!

def calculate_rectangle(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter  # 튜플로 반환!

# 언패킹으로 두 값을 각각 받기
rect_area, rect_perimeter = calculate_rectangle(5, 3)
print(f"넓이: {rect_area}")  # 출력: 넓이: 15
print(f"둘레: {rect_perimeter}")  # 출력: 둘레: 16


# TODO: 이름과 나이를 받아서 인사말과 성인 여부를 반환하는 함수를 작성하세요
# 힌트:
#   def greet_with_age(name, age):
#       message = f"안녕하세요, {name}님!"
#       is_adult = age >= 18
#       return message, is_adult

def greet_with_age(name, age):
    message = f"안녕하세요, {name}님!"
    is_adult = age >= 18
    return message, is_adult  # 두 개 반환!

# 언패킹으로 받기
greeting, adult_status = greet_with_age("홍길동", 25)
print(greeting)  # 출력: 안녕하세요, 홍길동님!
print(f"성인 여부: {adult_status}")  # 출력: 성인 여부: True

greeting, adult_status = greet_with_age("김영희", 15)
print(greeting)  # 출력: 안녕하세요, 김영희님!
print(f"성인 여부: {adult_status}")  # 출력: 성인 여부: False
