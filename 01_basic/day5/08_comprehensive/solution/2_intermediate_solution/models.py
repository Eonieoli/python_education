"""
models.py - 데이터 모델 클래스들 (해답)

User와 Product 클래스를 정의합니다.
utils 모듈의 검증 함수들을 활용합니다.
"""

from typing import Optional
from utils import validate_email, validate_price, validate_stock


class User:
    """
    사용자 클래스
    
    쇼핑몰 사용자 정보를 관리합니다.
    """
    
    def __init__(self, name: str, email: str, user_id: str) -> None:
        """
        사용자 초기화
        
        Args:
            name: 사용자 이름
            email: 이메일 주소
            user_id: 사용자 ID
        
        Raises:
            ValueError: 이메일 형식이 올바르지 않을 때
        """
        # 이메일 검증
        if not validate_email(email):
            raise ValueError("이메일 형식이 올바르지 않습니다")
        
        self.name = name
        self.email = email
        self.user_id = user_id
    
    def __str__(self) -> str:
        """사용자 정보를 문자열로 반환"""
        return f"사용자: {self.name} ({self.email}), ID: {self.user_id}"


class Product:
    """
    상품 클래스
    
    쇼핑몰 상품 정보를 관리하고 구매/입고 기능을 제공합니다.
    """
    
    def __init__(self, name: str, price: float, stock: int, product_id: str) -> None:
        """
        상품 초기화
        
        Args:
            name: 상품명
            price: 가격
            stock: 재고 수량
            product_id: 상품 ID
        
        Raises:
            ValueError: 가격이나 재고가 유효하지 않을 때
        """
        # 가격과 재고 검증
        validate_price(price)
        validate_stock(stock)
        
        self.name = name
        self.price = price
        self.stock = stock
        self.product_id = product_id
    
    def purchase(self, quantity: int) -> None:
        """
        상품 구매 처리
        
        Args:
            quantity: 구매 수량
        
        Raises:
            ValueError: 수량이 잘못되었거나 재고가 부족할 때
        """
        # 수량 검증
        if quantity <= 0:
            raise ValueError("구매 수량은 0보다 커야 합니다")
        
        # 재고 확인
        if quantity > self.stock:
            raise ValueError(
                f"재고가 부족합니다 (현재: {self.stock}개, 요청: {quantity}개)"
            )
        
        # 재고 감소
        self.stock -= quantity
        print(f"{quantity}개 구매 완료! 남은 재고: {self.stock}개")
    
    def restock(self, quantity: int) -> None:
        """
        상품 입고 처리
        
        Args:
            quantity: 입고 수량
        
        Raises:
            ValueError: 수량이 잘못되었을 때
        """
        # 수량 검증
        if quantity <= 0:
            raise ValueError("입고 수량은 0보다 커야 합니다")
        
        # 재고 증가
        self.stock += quantity
        print(f"{quantity}개 입고 완료! 현재 재고: {self.stock}개")
    
    def get_total_value(self) -> float:
        """
        재고 총 가치 계산
        
        Returns:
            float: 현재 재고의 총 가치 (가격 × 재고)
        """
        return self.price * self.stock
    
    def __str__(self) -> str:
        """상품 정보를 문자열로 반환"""
        return (
            f"상품: {self.name} - {self.price}원, "
            f"재고: {self.stock}개, ID: {self.product_id}"
        )
