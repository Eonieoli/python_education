# 2_practice.py

"""
Day 5 - 4교시: 클래스 상속 기초
Practice (강사와 함께 실습)

학습 목표:
- 상품 → 할인상품 상속 구현
- BaseModel 상속 연습
- 메서드 오버라이딩 실습
"""

from pydantic import BaseModel

# ============================================
# 실습 1: 상품 → 할인상품 상속 (처음부터 끝까지)
# ============================================

# 부모 클래스: 일반 상품
class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
    
    def get_price(self) -> int:
        return self.price
    
    def get_info(self) -> str:
        return f"{self.name}: {self.price}원"

# 자식 클래스: 할인 상품
class DiscountProduct(Product):  # Product 상속
    def __init__(self, name: str, price: int, discount_rate: float):
        # 부모의 __init__ 내용을 직접 실행
        self.name = name
        self.price = price
        self.discount_rate = discount_rate
    
    def get_price(self) -> int:  # 메서드 오버라이딩!
        # 할인 가격 계산
        return int(self.price * (1 - self.discount_rate))
    
    def get_info(self) -> str:  # 메서드 오버라이딩!
        original_price = self.price
        discount_price = self.get_price()
        return f"{self.name}: {original_price}원 → {discount_price}원 (할인)"

# 테스트
normal = Product("일반 티셔츠", 20000)
print(normal.get_info())  # 출력: 일반 티셔츠: 20000원

discount = DiscountProduct("세일 티셔츠", 20000, 0.2)
print(discount.get_info())  # 출력: 세일 티셔츠: 20000원 → 16000원 (할인)


# ============================================
# 실습 2: Pydantic BaseModel 상속 (TODO)
# ============================================

# TODO: PostBase 클래스를 작성하세요
# 필드: title (str), content (str)
class PostBase(BaseModel):
    title: str
    content: str

# TODO: PostCreate 클래스를 작성하세요 (PostBase 상속)
# 추가 필드: author (str)
class PostCreate(PostBase):
    author: str

# TODO: PostResponse 클래스를 작성하세요 (PostBase 상속)
# 추가 필드: id (int), views (int)
class PostResponse(PostBase):
    id: int
    views: int

# 테스트
new_post = PostCreate(
    title="안녕하세요",
    content="첫 게시글입니다",
    author="홍길동"
)
print(new_post)

response_post = PostResponse(
    title="안녕하세요",
    content="첫 게시글입니다",
    id=1,
    views=100
)
print(response_post)
