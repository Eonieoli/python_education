"""
validators.py - 검증 함수 모듈 (해답)

이메일, 비밀번호 등을 검증하는 함수들을 제공합니다.
FastAPI의 Pydantic validator 패턴을 흉내냅니다.
"""

from typing import Optional


def validate_email(email: str) -> str:
    """
    이메일 검증 및 정규화
    
    Args:
        email: 검증할 이메일 주소
    
    Returns:
        str: 소문자로 변환된 이메일
    
    Raises:
        ValueError: 이메일 형식이 올바르지 않을 때
    """
    if '@' not in email:
        raise ValueError("이메일 형식이 올바르지 않습니다")
    
    return email.lower()


def validate_password(password: str) -> str:
    """
    비밀번호 강도 검증
    
    Args:
        password: 검증할 비밀번호
    
    Returns:
        str: 검증된 비밀번호
    
    Raises:
        ValueError: 비밀번호 요구사항을 만족하지 않을 때
    """
    # 길이 검증
    if len(password) < 8:
        raise ValueError("비밀번호는 8자 이상이어야 합니다")
    
    # 대문자 포함 검증
    if not any(c.isupper() for c in password):
        raise ValueError("비밀번호는 대문자를 포함해야 합니다")
    
    return password


def validate_age(age: int) -> int:
    """
    나이 검증
    
    Args:
        age: 검증할 나이
    
    Returns:
        int: 검증된 나이
    
    Raises:
        ValueError: 나이가 유효한 범위를 벗어날 때
    """
    if age < 0:
        raise ValueError("나이는 0 이상이어야 합니다")
    
    if age > 150:
        raise ValueError("나이가 너무 많습니다")
    
    return age
