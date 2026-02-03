"""
utils.py - 검증 함수 모듈 (해답)

이메일, 가격, 재고 등을 검증하는 유틸리티 함수들을 제공합니다.
"""

from typing import Optional


def validate_email(email: str) -> bool:
    """
    이메일 형식 검증
    
    Args:
        email: 검증할 이메일 주소
    
    Returns:
        bool: 이메일에 '@'가 포함되어 있으면 True, 아니면 False
    """
    return '@' in email


def validate_price(price: float) -> None:
    """
    가격 검증
    
    Args:
        price: 검증할 가격
    
    Raises:
        ValueError: 가격이 0 이하일 때
    """
    if price <= 0:
        raise ValueError("가격은 0보다 커야 합니다")


def validate_stock(stock: int) -> None:
    """
    재고 검증
    
    Args:
        stock: 검증할 재고 수량
    
    Raises:
        ValueError: 재고가 0 미만일 때
    """
    if stock < 0:
        raise ValueError("재고는 0 이상이어야 합니다")


def format_currency(amount: float) -> str:
    """
    금액을 천 단위 콤마가 있는 문자열로 변환
    
    Args:
        amount: 변환할 금액
    
    Returns:
        str: 포맷된 금액 문자열 (예: "1,200,000원")
    """
    return f"{amount:,.0f}원"
