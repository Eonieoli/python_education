# 3_exercise.py

"""
Day 4 - 6교시: 타입 힌트 (1) - 기본 타입
Exercise - 타입 힌트가 있는 계산기 함수 작성

문제:
다양한 계산 기능을 가진 함수들을 작성하되, 
모든 함수에 적절한 타입 힌트를 추가하세요.

요구사항:
1. 모든 매개변수와 반환 타입에 타입 힌트 추가
2. 각 함수는 실행 가능해야 함
3. 주석으로 함수의 역할 설명
"""

# ============================================
# Exercise 1: 계산기 함수들
# ============================================

# TODO: 아래 함수들에 타입 힌트를 추가하세요

def multiply(a, b):
    """두 숫자를 곱합니다"""
    return a * b


def divide(a, b):
    """첫 번째 숫자를 두 번째 숫자로 나눕니다"""
    return a / b


def power(base, exponent):
    """base의 exponent 제곱을 계산합니다"""
    return base ** exponent


# 테스트 코드
print(f"5 × 3 = {multiply(5, 3)}")  # 출력: 5 × 3 = 15
print(f"10 ÷ 2 = {divide(10, 2)}")  # 출력: 10 ÷ 2 = 5.0
print(f"2^3 = {power(2, 3)}")  # 출력: 2^3 = 8


# ============================================
# Exercise 2: 문자열 처리 함수들
# ============================================

# TODO: 아래 함수들에 타입 힌트를 추가하세요

def repeat_string(text, count):
    """문자열을 count만큼 반복합니다"""
    return text * count


def get_length(text):
    """문자열의 길이를 반환합니다"""
    return len(text)


def is_long_text(text, min_length):
    """문자열이 최소 길이 이상인지 확인합니다"""
    return len(text) >= min_length


# 테스트 코드
print(repeat_string("안녕", 3))  # 출력: 안녕안녕안녕
print(f"길이: {get_length('Hello')}")  # 출력: 길이: 5
print(is_long_text("Python", 5))  # 출력: True


# ============================================
# Exercise 3: 실전 함수 (선택적)
# ============================================

# TODO: 아래 함수에 타입 힌트를 추가하세요
# 힌트: 모든 타입을 잘 생각해보세요!

def calculate_discount_price(original_price, discount_rate, is_member):
    """
    원가에 할인율을 적용하고, 회원이면 추가 5% 할인
    
    original_price: 원래 가격 (정수)
    discount_rate: 할인율 (소수, 예: 0.2는 20%)
    is_member: 회원 여부 (불리언)
    반환: 최종 가격 (실수)
    """
    # 기본 할인 적용
    price = original_price * (1 - discount_rate)
    
    # 회원이면 추가 5% 할인
    if is_member:
        price = price * 0.95
    
    return price


# 테스트 코드
price1 = calculate_discount_price(100000, 0.2, True)
print(f"회원 할인가: {price1}원")  # 출력: 회원 할인가: 76000.0원

price2 = calculate_discount_price(100000, 0.2, False)
print(f"일반 할인가: {price2}원")  # 출력: 일반 할인가: 80000.0원
