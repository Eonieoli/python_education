"""
Day 5 - 07교시: import 완전 정복
Basic 단계 - models.py (내가 만든 모듈!)

이 파일은 다른 파일에서 import해서 사용할 거예요!
"""

from typing import Optional


class User:
    """사용자 클래스"""
    
    def __init__(self, name: str, email: Optional[str] = None):
        """
        사용자 생성
        
        Args:
            name: 사용자 이름 (필수)
            email: 이메일 주소 (선택)
        """
        self.name = name
        self.email = email
    
    def greet(self) -> str:
        """인사말 반환"""
        if self.email:
            return f"안녕하세요, {self.name}님! ({self.email})"
        return f"안녕하세요, {self.name}님!"
    
    def has_email(self) -> bool:
        """이메일이 있는지 확인"""
        return self.email is not None


class Product:
    """상품 클래스"""
    
    def __init__(self, name: str, price: int, stock: int = 0):
        """
        상품 생성
        
        Args:
            name: 상품명
            price: 가격
            stock: 재고 (기본값 0)
        """
        self.name = name
        self.price = price
        self.stock = stock
    
    def get_info(self) -> str:
        """상품 정보 문자열 반환"""
        return f"{self.name} - {self.price:,}원 (재고: {self.stock}개)"
    
    def is_available(self) -> bool:
        """재고가 있는지 확인"""
        return self.stock > 0
    
    def sell(self, quantity: int = 1) -> bool:
        """
        상품 판매
        
        Args:
            quantity: 판매 수량
            
        Returns:
            판매 성공 여부
        """
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False


# 이 파일을 직접 실행하면 테스트 코드가 실행됨
if __name__ == "__main__":
    print("=" * 50)
    print("models.py 테스트")
    print("=" * 50)
    
    # User 테스트
    user1 = User("Alice", "alice@example.com")
    print(user1.greet())
    print(f"이메일 있음? {user1.has_email()}")
    
    user2 = User("Bob")  # 이메일 없음
    print(user2.greet())
    print(f"이메일 있음? {user2.has_email()}")
    
    print()
    
    # Product 테스트
    product = Product("노트북", 1500000, 10)
    print(product.get_info())
    print(f"구매 가능? {product.is_available()}")
    
    # 3개 판매
    if product.sell(3):
        print("판매 성공!")
        print(product.get_info())
