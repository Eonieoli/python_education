"""
Day 5 - 07교시: import 완전 정복
Exercise 단계 - models.py

Product와 User 클래스를 작성하세요.
이 모듈은 main.py에서 import해서 사용됩니다.
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
            
        TODO:
            self.name, self.price, self.stock 속성 설정
        """
        # TODO: 여기에 코드 작성
        pass
    
    def is_available(self) -> bool:
        """
        재고가 있는지 확인
        
        Returns:
            재고가 있으면 True
            
        TODO:
            self.stock이 0보다 크면 True
        """
        # TODO: 여기에 코드 작성
        pass
    
    def sell(self, quantity: int = 1) -> bool:
        """
        상품 판매
        
        Args:
            quantity: 판매 수량
            
        Returns:
            판매 성공하면 True, 실패하면 False
            
        TODO:
            1. self.stock >= quantity 인지 확인
            2. 충분하면 self.stock에서 quantity만큼 빼고 True 반환
            3. 부족하면 False 반환
        """
        # TODO: 여기에 코드 작성
        pass
    
    def restock(self, quantity: int) -> None:
        """
        재고 추가
        
        Args:
            quantity: 추가할 수량
            
        TODO:
            self.stock에 quantity 더하기
        """
        # TODO: 여기에 코드 작성
        pass
    
    def get_info(self) -> str:
        """
        상품 정보 문자열 반환
        
        Returns:
            상품 정보 (이름, 가격, 재고)
            
        TODO:
            f-string으로 "상품명 - 가격원 (재고: 재고개)" 형식
        """
        # TODO: 여기에 코드 작성
        pass


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
            
        TODO:
            모든 속성 설정
        """
        # TODO: 여기에 코드 작성
        pass
    
    def get_profile(self) -> str:
        """
        프로필 정보 문자열 반환
        
        Returns:
            프로필 정보
            
        TODO:
            1. age가 None이 아니면 나이도 포함
            2. f-string으로 포맷팅
        """
        # TODO: 여기에 코드 작성
        pass
    
    def change_password(self, new_password: str) -> None:
        """
        비밀번호 변경
        
        Args:
            new_password: 새 비밀번호
            
        TODO:
            self.password를 new_password로 변경
        """
        # TODO: 여기에 코드 작성
        pass


class ShoppingCart:
    """장바구니 클래스"""
    
    def __init__(self):
        """
        장바구니 생성
        
        TODO:
            self.items를 빈 리스트로 초기화
        """
        # TODO: 여기에 코드 작성
        pass
    
    def add_item(self, product: Product, quantity: int = 1) -> None:
        """
        상품 추가
        
        Args:
            product: Product 객체
            quantity: 수량
            
        TODO:
            딕셔너리 {"product": product, "quantity": quantity}를
            self.items에 추가
        """
        # TODO: 여기에 코드 작성
        pass
    
    def get_total_price(self) -> int:
        """
        총 금액 계산
        
        Returns:
            장바구니 총 금액
            
        TODO:
            1. self.items의 각 항목에 대해
            2. product.price * quantity 계산
            3. 모두 더해서 반환
        """
        # TODO: 여기에 코드 작성
        pass
    
    def get_item_count(self) -> int:
        """
        장바구니 상품 개수
        
        Returns:
            장바구니에 담긴 상품 종류 개수
            
        TODO:
            len(self.items) 반환
        """
        # TODO: 여기에 코드 작성
        pass


# 직접 실행 시 테스트
if __name__ == "__main__":
    print("=" * 50)
    print("models.py 테스트")
    print("=" * 50)
    
    # TODO 완성 후 주석 해제해서 테스트
    """
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
    
    # User 테스트
    print("\nUser 테스트:")
    user = User("alice", "alice@example.com", "Password123", 25)
    print(user.get_profile())
    
    user.change_password("NewPassword456")
    print("비밀번호 변경 완료!")
    
    # ShoppingCart 테스트
    print("\nShoppingCart 테스트:")
    cart = ShoppingCart()
    
    laptop = Product("노트북", 1500000, 10)
    keyboard = Product("키보드", 150000, 20)
    
    cart.add_item(laptop, 1)
    cart.add_item(keyboard, 2)
    
    print(f"장바구니 상품 수: {cart.get_item_count()}개")
    print(f"총 금액: {cart.get_total_price():,}원")
    """
