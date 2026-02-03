"""
Day 5 - 07교시: import 완전 정복
Basic 단계 - utils.py (유틸리티 함수 모듈)

여러 곳에서 사용할 수 있는 범용 함수들을 모아놓은 모듈!
"""


def validate_email(email: str) -> bool:
    """
    이메일 유효성 간단 검증
    
    Args:
        email: 검증할 이메일 주소
        
    Returns:
        유효하면 True, 아니면 False
    """
    # 간단한 검증: @가 있고, .이 있으면 OK
    return "@" in email and "." in email


def format_price(price: int) -> str:
    """
    가격을 읽기 좋은 형식으로 포맷팅
    
    Args:
        price: 가격 (정수)
        
    Returns:
        포맷팅된 문자열 (예: "1,500,000원")
    """
    return f"{price:,}원"


def calculate_discount(price: int, discount_rate: float) -> int:
    """
    할인된 가격 계산
    
    Args:
        price: 원래 가격
        discount_rate: 할인율 (0.0 ~ 1.0, 예: 0.1 = 10% 할인)
        
    Returns:
        할인된 가격 (정수)
    """
    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("할인율은 0.0 ~ 1.0 사이여야 합니다")
    
    discounted = price * (1 - discount_rate)
    return int(discounted)


def truncate_text(text: str, max_length: int = 20) -> str:
    """
    긴 텍스트를 잘라서 표시
    
    Args:
        text: 원본 텍스트
        max_length: 최대 길이 (기본값 20)
        
    Returns:
        잘린 텍스트 (길면 "..." 추가)
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."


def safe_divide(a: float, b: float) -> float:
    """
    안전한 나눗셈 (0으로 나누면 0 반환)
    
    Args:
        a: 피제수
        b: 제수
        
    Returns:
        나눗셈 결과 (b가 0이면 0.0 반환)
    """
    if b == 0:
        return 0.0
    return a / b


# 이 파일을 직접 실행하면 테스트 코드가 실행됨
if __name__ == "__main__":
    print("=" * 50)
    print("utils.py 테스트")
    print("=" * 50)
    
    # 이메일 검증
    print("이메일 검증:")
    print(f"  alice@example.com: {validate_email('alice@example.com')}")
    print(f"  invalid-email: {validate_email('invalid-email')}")
    
    # 가격 포맷팅
    print("\n가격 포맷팅:")
    print(f"  1500000 → {format_price(1500000)}")
    print(f"  50000 → {format_price(50000)}")
    
    # 할인 계산
    print("\n할인 계산:")
    original_price = 100000
    print(f"  원가: {format_price(original_price)}")
    print(f"  10% 할인: {format_price(calculate_discount(original_price, 0.1))}")
    print(f"  30% 할인: {format_price(calculate_discount(original_price, 0.3))}")
    
    # 텍스트 자르기
    print("\n텍스트 자르기:")
    long_text = "이것은 매우 긴 텍스트입니다. 잘려야 합니다."
    print(f"  원본: {long_text}")
    print(f"  잘린 텍스트: {truncate_text(long_text, 15)}")
    
    # 안전한 나눗셈
    print("\n안전한 나눗셈:")
    print(f"  10 / 2 = {safe_divide(10, 2)}")
    print(f"  10 / 0 = {safe_divide(10, 0)} (에러 대신 0 반환)")
