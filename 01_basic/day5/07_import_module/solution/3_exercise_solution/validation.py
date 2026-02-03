"""
Day 5 - 07교시: import 완전 정복
Exercise Solution - validation.py (정답)

여러 검증 함수들의 완성된 버전입니다.
"""


def validate_email(email: str) -> bool:
    """
    이메일 유효성 검증
    
    Args:
        email: 검증할 이메일 주소
        
    Returns:
        유효하면 True, 아니면 False
    """
    # @와 .이 모두 포함되어 있는지 확인
    return "@" in email and "." in email


def validate_phone(phone: str) -> bool:
    """
    전화번호 유효성 검증 (간단 버전)
    
    Args:
        phone: 검증할 전화번호 (예: "010-1234-5678")
        
    Returns:
        유효하면 True, 아니면 False
    """
    # 하이픈으로 나누기
    parts = phone.split("-")
    
    # 3부분이어야 하고, 첫 부분이 "010"이어야 함
    if len(parts) != 3:
        return False
    
    if parts[0] != "010":
        return False
    
    return True


def validate_password(password: str) -> bool:
    """
    비밀번호 강도 검증
    
    Args:
        password: 검증할 비밀번호
        
    Returns:
        유효하면 True, 아니면 False
    """
    # 길이 확인
    if len(password) < 8:
        return False
    
    # 대문자 확인
    has_upper = any(c.isupper() for c in password)
    if not has_upper:
        return False
    
    # 숫자 확인
    has_digit = any(c.isdigit() for c in password)
    if not has_digit:
        return False
    
    return True


def validate_username(username: str) -> bool:
    """
    사용자명 유효성 검증
    
    Args:
        username: 검증할 사용자명
        
    Returns:
        유효하면 True, 아니면 False
    """
    # 길이 확인 (3자 이상 20자 이하)
    if len(username) < 3 or len(username) > 20:
        return False
    
    # 알파벳과 숫자만 포함하는지 확인
    if not username.isalnum():
        return False
    
    return True


def validate_age(age: int) -> bool:
    """
    나이 유효성 검증
    
    Args:
        age: 검증할 나이
        
    Returns:
        유효하면 True, 아니면 False
    """
    # 0보다 크고 150 이하
    return 0 < age <= 150


# 직접 실행 시 테스트
if __name__ == "__main__":
    print("=" * 50)
    print("validation.py 테스트")
    print("=" * 50)
    
    # 이메일 테스트
    print("\n이메일 검증:")
    print(f"  alice@example.com: {validate_email('alice@example.com')}")
    print(f"  invalid-email: {validate_email('invalid-email')}")
    print(f"  no-at-sign.com: {validate_email('no-at-sign.com')}")
    
    # 전화번호 테스트
    print("\n전화번호 검증:")
    print(f"  010-1234-5678: {validate_phone('010-1234-5678')}")
    print(f"  02-1234-5678: {validate_phone('02-1234-5678')}")
    print(f"  01012345678: {validate_phone('01012345678')}")
    
    # 비밀번호 테스트
    print("\n비밀번호 검증:")
    print(f"  Password123: {validate_password('Password123')}")
    print(f"  weak: {validate_password('weak')}")
    print(f"  NoNumber: {validate_password('NoNumber')}")
    print(f"  nonumber1: {validate_password('nonumber1')}")
    
    # 사용자명 테스트
    print("\n사용자명 검증:")
    print(f"  alice123: {validate_username('alice123')}")
    print(f"  ab: {validate_username('ab')}")  # 너무 짧음
    print(f"  alice@123: {validate_username('alice@123')}")  # 특수문자
    print(f"  averylongusernamethatexceeds20chars: {validate_username('averylongusernamethatexceeds20chars')}")
    
    # 나이 테스트
    print("\n나이 검증:")
    print(f"  25: {validate_age(25)}")
    print(f"  0: {validate_age(0)}")
    print(f"  200: {validate_age(200)}")
    print(f"  -5: {validate_age(-5)}")
