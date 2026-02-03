# 2_practice.py

"""
Day 5 - 6교시: 스코프 + 데코레이터 개념
Practice (강사와 함께 실습)

학습 목표:
- 변수 스코프 직접 실험하기
- 클래스 변수와 인스턴스 변수 구분하기
- 데코레이터 패턴 이해하기
"""


# ============================================
# 실습 1: 변수 스코프 실험
# ============================================

# 전역 변수
price = 10000

def apply_discount():
    # TODO: global 키워드를 사용하여 price를 20% 할인하세요
    # 힌트: global price 선언 후 price *= 0.8
    global price
    price *= 0.8
    print(f"할인 적용! 현재 가격: {price}원")

print(f"원래 가격: {price}원")  # 출력: 원래 가격: 10000원
apply_discount()  # 출력: 할인 적용! 현재 가격: 8000.0원
print(f"최종 가격: {price}원")  # 출력: 최종 가격: 8000.0원


# ============================================
# 실습 2: 클래스 변수 vs 인스턴스 변수
# ============================================

class Product:
    # TODO: 클래스 변수 total_products를 0으로 초기화하세요
    total_products = 0
    
    def __init__(self, name: str, price: int):
        # TODO: 인스턴스 변수 name과 price를 설정하세요
        self.name = name
        self.price = price
        # TODO: 클래스 변수 total_products를 1 증가시키세요
        Product.total_products += 1

# 상품 3개 생성
product1 = Product("노트북", 1500000)
product2 = Product("마우스", 30000)
product3 = Product("키보드", 80000)

print(f"총 상품 개수: {Product.total_products}개")  # 출력: 총 상품 개수: 3개
print(f"상품1 이름: {product1.name}")  # 출력: 상품1 이름: 노트북


# ============================================
# 실습 3: 데코레이터 패턴 이해
# ============================================

def uppercase_decorator(func):
    """결과를 대문자로 변환하는 데코레이터"""
    def wrapper(name: str) -> str:
        # TODO: func(name)을 호출하고 결과를 대문자로 변환하세요
        # 힌트: result = func(name), return result.upper()
        result = func(name)
        return result.upper()
    return wrapper

# TODO: @uppercase_decorator를 사용하여 greet 함수를 꾸며주세요
@uppercase_decorator
def greet(name: str) -> str:
    return f"hello, {name}!"

message = greet("alice")
print(message)  # 출력: HELLO, ALICE!


# ============================================
# 실습 4: @property 활용
# ============================================

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    # TODO: @property 데코레이터를 사용하여 area 메서드를 만드세요
    # 힌트: 넓이 = width * height
    @property
    def area(self) -> int:
        return self.width * self.height

rect = Rectangle(10, 5)
print(f"사각형 넓이: {rect.area}")  # 출력: 사각형 넓이: 50 (메서드인데 ()없이!)


print("\n=== 모든 실습 완료! ===")
