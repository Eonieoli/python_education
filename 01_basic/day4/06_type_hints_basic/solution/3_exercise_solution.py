# 3_exercise_solution.py

"""
Day 4 - 6교시: 타입 힌트 (1) - 기본 타입
Exercise - 타입 힌트가 있는 계산기 함수 작성 (정답)
"""

# ============================================
# Exercise 1: 계산기 함수들 (정답)
# ============================================

def multiply(a: int, b: int) -> int:
    """두 숫자를 곱합니다"""
    return a * b


def divide(a: float, b: float) -> float:
    """첫 번째 숫자를 두 번째 숫자로 나눕니다"""
    return a / b


def power(base: int, exponent: int) -> int:
    """base의 exponent 제곱을 계산합니다"""
    return base ** exponent


# 테스트 코드
print(f"5 × 3 = {multiply(5, 3)}")  # 출력: 5 × 3 = 15
print(f"10 ÷ 2 = {divide(10, 2)}")  # 출력: 10 ÷ 2 = 5.0
print(f"2^3 = {power(2, 3)}")  # 출력: 2^3 = 8


# ============================================
# Exercise 2: 문자열 처리 함수들 (정답)
# ============================================

def repeat_string(text: str, count: int) -> str:
    """문자열을 count만큼 반복합니다"""
    return text * count


def get_length(text: str) -> int:
    """문자열의 길이를 반환합니다"""
    return len(text)


def is_long_text(text: str, min_length: int) -> bool:
    """문자열이 최소 길이 이상인지 확인합니다"""
    return len(text) >= min_length


# 테스트 코드
print(repeat_string("안녕", 3))  # 출력: 안녕안녕안녕
print(f"길이: {get_length('Hello')}")  # 출력: 길이: 5
print(is_long_text("Python", 5))  # 출력: True


# ============================================
# Exercise 3: 실전 함수 (정답)
# ============================================

def calculate_discount_price(original_price: int, discount_rate: float, is_member: bool) -> float:
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
