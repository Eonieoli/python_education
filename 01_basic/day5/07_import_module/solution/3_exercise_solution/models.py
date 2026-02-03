"""
Day 5 - 07교시: import 완전 정복
Exercise Solution - models.py (정답)

Product, User, ShoppingCart 클래스의 완성된 버전입니다.
"""

from typing import Optional, List


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
    
    def is_available(self) -> bool:
        """
        재고가 있는지 확인
        
        Returns:
            재고가 있으면 True
        """
        return self.stock > 0
    
    def sell(self, quantity: int = 1) -> bool:
        """
        상품 판매
        
        Args:
            quantity: 판매 수량
            
        Returns:
            판매 성공하면 True, 실패하면 False
        """
        # 재고가 충분한지 확인
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False
    
    def restock(self, quantity: int) -> None:
        """
        재고 추가
        
        Args:
            quantity: 추가할 수량
        """
        self.stock += quantity
    
    def get_info(self) -> str:
        """
        상품 정보 문자열 반환
        
        Returns:
            상품 정보 (이름, 가격, 재고)
        """
        return f"{self.name} - {self.price:,}원 (재고: {self.stock}개)"


class User:
    """사용자 클래스"""
    
    def __init__(
        self,
        username: str,
        email: str,
        password: str,
        age: Optional[int] = None
    ):
        """
        사용자 생성
        
        Args:
            username: 사용자명
            email: 이메일
            password: 비밀번호
            age: 나이 (선택)
        """
        self.username = username
        self.email = email
        self.password = password
        self.age = age
    
    def get_profile(self) -> str:
        """
        프로필 정보 문자열 반환
        
        Returns:
            프로필 정보
        """
        # age가 있으면 포함
        if self.age is not None:
            return f"{self.username} ({self.email}) - 나이: {self.age}세"
        return f"{self.username} ({self.email})"
    
    def change_password(self, new_password: str) -> None:
        """
        비밀번호 변경
        
        Args:
            new_password: 새 비밀번호
        """
        self.password = new_password


class ShoppingCart:
    """장바구니 클래스"""
    
    def __init__(self):
        """
        장바구니 생성
        """
        self.items: List[dict] = []
    
    def add_item(self, product: Product, quantity: int = 1) -> None:
        """
        상품 추가
        
        Args:
            product: Product 객체
            quantity: 수량
        """
        self.items.append({
            "product": product,
            "quantity": quantity
        })
    
    def get_total_price(self) -> int:
        """
        총 금액 계산
        
        Returns:
            장바구니 총 금액
        """
        total = 0
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            total += product.price * quantity
        return total
    
    def get_item_count(self) -> int:
        """
        장바구니 상품 개수
        
        Returns:
            장바구니에 담긴 상품 종류 개수
        """
        return len(self.items)


# 직접 실행 시 테스트
if __name__ == "__main__":
    print("=" * 50)
    print("models.py 테스트")
    print("=" * 50)
    
    # Product 테스트
    print("\nProduct 테스트:")
    product = Product("노트북", 1500000, 10)
    print(product.get_info())
    print(f"구매 가능? {product.is_available()}")
    
    if product.sell(3):
        print("3개 판매 성공!")
        print(product.get_info())
    
    product.restock(5)
    print("재고 5개 추가!")
    print(product.get_info())
    
    # 재고보다 많이 판매 시도
    print("\n20개 판매 시도:")
    if product.sell(20):
        print("판매 성공!")
    else:
        print("재고 부족으로 판매 실패")
    
    # User 테스트
    print("\nUser 테스트:")
    user1 = User("alice", "alice@example.com", "Password123", 25)
    print(user1.get_profile())
    
    user2 = User("bob", "bob@example.com", "SecurePass456")
    print(user2.get_profile())
    
    user1.change_password("NewPassword456")
    print("Alice 비밀번호 변경 완료!")
    
    # ShoppingCart 테스트
    print("\nShoppingCart 테스트:")
    cart = ShoppingCart()
    
    laptop = Product("노트북", 1500000, 10)
    keyboard = Product("키보드", 150000, 20)
    mouse = Product("마우스", 50000, 30)
    
    cart.add_item(laptop, 1)
    cart.add_item(keyboard, 2)
    cart.add_item(mouse, 3)
    
    print(f"장바구니 상품 수: {cart.get_item_count()}개")
    print(f"총 금액: {cart.get_total_price():,}원")
    
    # 상세 내역 출력
    print("\n장바구니 상세:")
    for item in cart.items:
        product = item["product"]
        quantity = item["quantity"]
        subtotal = product.price * quantity
        print(f"  {product.name} x {quantity} = {subtotal:,}원")
