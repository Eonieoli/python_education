# 1_basic.py

"""
Day 4 - 6교시: 타입 힌트 (1) - 기본 타입
Basic (강사 시연용)

학습 목표:
- 타입 힌트의 필요성과 장점 이해
- 기본 타입 힌트 사용법 (int, str, float, bool)
- 매개변수와 반환 타입에 타입 힌트 적용
- 타입 힌트는 힌트일 뿐 강제가 아님을 이해
"""

# ============================================
# 1. 기본 타입 힌트 - int, str
# ============================================

# 타입 힌트가 없는 함수
def add_old(a, b):
    return a + b

# 타입 힌트가 있는 함수 - 훨씬 명확!
def add(a: int, b: int) -> int:
    """두 정수를 더합니다"""
    return a + b

result = add(10, 20)
print(f"10 + 20 = {result}")  # 출력: 10 + 20 = 30


# 문자열 타입 힌트
def greet(name: str) -> str:
    """이름을 받아 인사말을 반환합니다"""
    return f"안녕하세요, {name}님!"

message = greet("홍길동")
print(message)  # 출력: 안녕하세요, 홍길동님!


# ============================================
# 2. float, bool 타입 힌트
# ============================================

# float 타입 (소수점 계산)
def calculate_price(price: float, tax: float = 0.1) -> float:
    """가격에 세금을 더한 최종 금액을 계산합니다"""
    return price * (1 + tax)

final_price = calculate_price(10000, 0.1)
print(f"최종 가격: {final_price}원")  # 출력: 최종 가격: 11000.0원


# bool 타입 (True/False 반환)
def is_adult(age: int) -> bool:
    """성인 여부를 판단합니다 (만 18세 이상)"""
    return age >= 18

print(is_adult(25))  # 출력: True
print(is_adult(15))  # 출력: False


# ============================================
# 3. 타입 힌트는 강제가 아닙니다!
# ============================================

# 타입 힌트가 있어도 다른 타입으로 실행 가능
result1 = add(5, 3)  # OK - 정상적인 사용
print(result1)  # 출력: 8

result2 = add("Hello", "World")  # 타입 에러지만 실행은 됨!
print(result2)  # 출력: HelloWorld

# 타입 힌트의 목적:
# 1. 코드 가독성 향상
# 2. IDE의 자동완성 지원
# 3. 버그 사전 예방 (IDE가 경고)
# 4. FastAPI/Pydantic에서 필수!


# ============================================
# 4. 실전 예제 1: 상품 정보 처리
# ============================================

def format_product_info(name: str, price: int, stock: int) -> str:
    """상품 정보를 보기 좋게 포맷팅합니다"""
    return f"상품명: {name} | 가격: {price:,}원 | 재고: {stock}개"

info = format_product_info("노트북", 1500000, 5)
print(info)  # 출력: 상품명: 노트북 | 가격: 1,500,000원 | 재고: 5개


# ============================================
# 5. 실전 예제 2: 사용자 검증
# ============================================

def validate_password(password: str, min_length: int = 8) -> bool:
    """비밀번호가 최소 길이를 만족하는지 확인합니다"""
    return len(password) >= min_length

def validate_email(email: str) -> bool:
    """이메일 형식이 올바른지 간단히 확인합니다"""
    return "@" in email and "." in email

# 테스트
print(validate_password("abc123"))  # 출력: False (8자 미만)
print(validate_password("abc12345"))  # 출력: True (8자 이상)
print(validate_email("user@example.com"))  # 출력: True
print(validate_email("invalid-email"))  # 출력: False
