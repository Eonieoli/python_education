"""
Day 5 - 07교시: import 완전 정복
Exercise 단계 - validation.py

여러 검증 함수들을 작성하세요.
이 모듈은 main.py에서 import해서 사용됩니다.
"""


def validate_email(email: str) -> bool:
    """
    이메일 유효성 검증
    
    Args:
        email: 검증할 이메일 주소
        
    Returns:
        유효하면 True, 아니면 False
        
    TODO:
        1. @가 포함되어 있는지 확인
        2. .이 포함되어 있는지 확인
        3. 두 조건 모두 만족하면 True
    """
    # TODO: 여기에 코드 작성
    pass


def validate_phone(phone: str) -> bool:
    """
    전화번호 유효성 검증 (간단 버전)
    
    Args:
        phone: 검증할 전화번호 (예: "010-1234-5678")
        
    Returns:
        유효하면 True, 아니면 False
        
    TODO:
        1. 하이픈(-)이 2개 있는지 확인
        2. split('-')로 나눴을 때 3부분인지 확인
        3. 첫 부분이 "010"인지 확인
    """
    # TODO: 여기에 코드 작성
    pass


def validate_password(password: str) -> bool:
    """
    비밀번호 강도 검증
    
    Args:
        password: 검증할 비밀번호
        
    Returns:
        유효하면 True, 아니면 False
        
    TODO:
        1. 길이가 8자 이상인지 확인
        2. 대문자가 최소 1개 있는지 확인 (힌트: any(c.isupper() for c in password))
        3. 숫자가 최소 1개 있는지 확인 (힌트: any(c.isdigit() for c in password))
    """
    # TODO: 여기에 코드 작성
    pass


def validate_username(username: str) -> bool:
    """
    사용자명 유효성 검증
    
    Args:
        username: 검증할 사용자명
        
    Returns:
        유효하면 True, 아니면 False
        
    TODO:
        1. 길이가 3자 이상, 20자 이하인지 확인
        2. 알파벳과 숫자만 포함하는지 확인 (힌트: username.isalnum())
    """
    # TODO: 여기에 코드 작성
    pass


def validate_age(age: int) -> bool:
    """
    나이 유효성 검증
    
    Args:
        age: 검증할 나이
        
    Returns:
        유효하면 True, 아니면 False
        
    TODO:
        1. 0보다 크고 150 이하인지 확인
    """
    # TODO: 여기에 코드 작성
    pass


# 직접 실행 시 테스트
if __name__ == "__main__":
    print("=" * 50)
    print("validation.py 테스트")
    print("=" * 50)
    
    # TODO 완성 후 주석 해제해서 테스트
    """
    # 이메일 테스트
    print("\n이메일 검증:")
    print(f"  alice@example.com: {validate_email('alice@example.com')}")
    print(f"  invalid-email: {validate_email('invalid-email')}")
    
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
    
    # 사용자명 테스트
    print("\n사용자명 검증:")
    print(f"  alice123: {validate_username('alice123')}")
    print(f"  ab: {validate_username('ab')}")  # 너무 짧음
    print(f"  alice@123: {validate_username('alice@123')}")  # 특수문자
    
    # 나이 테스트
    print("\n나이 검증:")
    print(f"  25: {validate_age(25)}")
    print(f"  0: {validate_age(0)}")
    print(f"  200: {validate_age(200)}")
    """
