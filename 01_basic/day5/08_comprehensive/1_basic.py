"""
Day 5 - 8교시: 기초 과정 종합 실습
🟢 기초 Problem (15분)

주제: 은행 계좌 관리 시스템
- 타입 힌트가 완벽한 클래스 시스템
- 여러 클래스 상속 구조
- 예외 처리 포함

학습 목표:
1. 클래스 상속 구조 이해
2. 타입 힌트 완벽 적용
3. 예외 처리로 안전한 코드 작성
4. 메서드 오버라이딩
"""

from typing import List, Optional

# TODO 1: InsufficientFundsError 예외 클래스 작성
# - ValueError를 상속받는 커스텀 예외
# - "잔액이 부족합니다" 메시지를 기본으로 가짐


# TODO 2: BankAccount 부모 클래스 작성
# 속성:
#   - owner: str (계좌 소유자)
#   - balance: float (잔액, 기본값 0.0)
#   - account_number: str (계좌번호)
# 
# 메서드:
#   - __init__(owner: str, account_number: str, balance: float = 0.0) -> None
#   - deposit(amount: float) -> None
#       * amount가 0 이하면 ValueError 발생
#       * 잔액 증가
#   - withdraw(amount: float) -> None
#       * amount가 0 이하면 ValueError 발생
#       * 잔액이 부족하면 InsufficientFundsError 발생
#       * 잔액 감소
#   - get_balance() -> float
#       * 현재 잔액 반환
#   - __str__() -> str
#       * "계좌번호: {account_number}, 소유자: {owner}, 잔액: {balance}원" 형식


# TODO 3: SavingsAccount 클래스 작성 (BankAccount 상속)
# 추가 속성:
#   - interest_rate: float (이자율, 기본값 0.02)
# 
# 메서드:
#   - __init__(owner: str, account_number: str, balance: float = 0.0, 
#              interest_rate: float = 0.02) -> None
#   - add_interest() -> None
#       * 잔액에 이자 추가 (balance = balance * (1 + interest_rate))
#       * f-string으로 "이자 {이자액}원이 추가되었습니다" 출력
#   - __str__() -> str
#       * 부모의 __str__() + f", 이자율: {interest_rate*100}%" 추가


# TODO 4: CheckingAccount 클래스 작성 (BankAccount 상속)
# 추가 속성:
#   - overdraft_limit: float (마이너스 통장 한도, 기본값 0.0)
# 
# 메서드:
#   - __init__(owner: str, account_number: str, balance: float = 0.0,
#              overdraft_limit: float = 0.0) -> None
#   - withdraw(amount: float) -> None (오버라이딩!)
#       * amount가 0 이하면 ValueError 발생
#       * 잔액 + 마이너스 한도를 초과하면 InsufficientFundsError 발생
#       * 잔액 감소
#   - __str__() -> str
#       * 부모의 __str__() + f", 마이너스 한도: {overdraft_limit}원" 추가


# TODO 5: 테스트 코드 작성
if __name__ == "__main__":
    print("=== 은행 계좌 관리 시스템 테스트 ===\n")
    
    # 1. 일반 계좌 테스트
    print("1. 일반 계좌 테스트")
    # - "홍길동", "1234-5678", 초기잔액 10000원으로 계좌 생성
    # - 계좌 정보 출력 (print 사용)
    # - 5000원 입금
    # - 3000원 출금
    # - 현재 잔액 출력 (f-string 사용)
    
    
    # 2. 적금 계좌 테스트
    print("\n2. 적금 계좌 테스트")
    # - "김철수", "8765-4321", 초기잔액 50000원, 이자율 3%로 계좌 생성
    # - 계좌 정보 출력
    # - 이자 추가
    # - 현재 잔액 출력
    
    
    # 3. 마이너스 통장 테스트
    print("\n3. 마이너스 통장 테스트")
    # - "이영희", "1111-2222", 초기잔액 30000원, 마이너스 한도 20000원으로 계좌 생성
    # - 계좌 정보 출력
    # - 40000원 출금 (성공: 잔액+한도 범위 내)
    # - 현재 잔액 출력
    
    
    # 4. 예외 처리 테스트
    print("\n4. 예외 처리 테스트")
    # try-except로 다음 상황 테스트:
    # - 일반 계좌에서 잔액 초과 출금 시도
    # - 음수 입금 시도
    

"""
실행 결과 예시:
=== 은행 계좌 관리 시스템 테스트 ===

1. 일반 계좌 테스트
계좌번호: 1234-5678, 소유자: 홍길동, 잔액: 10000원
현재 잔액: 12000원

2. 적금 계좌 테스트
계좌번호: 8765-4321, 소유자: 김철수, 잔액: 50000원, 이자율: 3.0%
이자 1500.0원이 추가되었습니다
현재 잔액: 51500.0원

3. 마이너스 통장 테스트
계좌번호: 1111-2222, 소유자: 이영희, 잔액: 30000원, 마이너스 한도: 20000원
현재 잔액: -10000원

4. 예외 처리 테스트
잔액 초과 출금 시도 - 에러: 잔액이 부족합니다
음수 입금 시도 - 에러: 입금액은 0보다 커야 합니다
"""
