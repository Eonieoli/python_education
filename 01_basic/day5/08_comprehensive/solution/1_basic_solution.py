"""
Day 5 - 8교시: 기초 과정 종합 실습
🟢 기초 Problem 해답

은행 계좌 관리 시스템
"""

from typing import List, Optional

# 커스텀 예외 클래스
class InsufficientFundsError(ValueError):
    """잔액 부족 시 발생하는 예외"""
    def __init__(self, message: str = "잔액이 부족합니다"):
        super().__init__(message)


# 부모 클래스: 일반 은행 계좌
class BankAccount:
    """
    은행 계좌 기본 클래스
    
    모든 계좌 타입의 부모 클래스로, 기본적인 입출금 기능을 제공합니다.
    """
    
    def __init__(self, owner: str, account_number: str, balance: float = 0.0) -> None:
        """
        계좌 초기화
        
        Args:
            owner: 계좌 소유자 이름
            account_number: 계좌번호
            balance: 초기 잔액 (기본값 0.0)
        """
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount: float) -> None:
        """
        입금 처리
        
        Args:
            amount: 입금할 금액
            
        Raises:
            ValueError: amount가 0 이하일 때
        """
        if amount <= 0:
            raise ValueError("입금액은 0보다 커야 합니다")
        
        self.balance += amount
        print(f"{amount}원이 입금되었습니다")
    
    def withdraw(self, amount: float) -> None:
        """
        출금 처리
        
        Args:
            amount: 출금할 금액
            
        Raises:
            ValueError: amount가 0 이하일 때
            InsufficientFundsError: 잔액이 부족할 때
        """
        if amount <= 0:
            raise ValueError("출금액은 0보다 커야 합니다")
        
        if amount > self.balance:
            raise InsufficientFundsError()
        
        self.balance -= amount
        print(f"{amount}원이 출금되었습니다")
    
    def get_balance(self) -> float:
        """현재 잔액 반환"""
        return self.balance
    
    def __str__(self) -> str:
        """계좌 정보를 문자열로 반환"""
        return f"계좌번호: {self.account_number}, 소유자: {self.owner}, 잔액: {self.balance}원"


# 자식 클래스 1: 적금 계좌
class SavingsAccount(BankAccount):
    """
    적금 계좌 클래스
    
    일반 계좌에 이자 기능이 추가된 계좌입니다.
    """
    
    def __init__(self, owner: str, account_number: str, 
                 balance: float = 0.0, interest_rate: float = 0.02) -> None:
        """
        적금 계좌 초기화
        
        Args:
            owner: 계좌 소유자 이름
            account_number: 계좌번호
            balance: 초기 잔액 (기본값 0.0)
            interest_rate: 이자율 (기본값 0.02 = 2%)
        """
        # 부모 클래스의 __init__ 호출
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self) -> None:
        """이자를 계산하여 잔액에 추가"""
        interest = self.balance * self.interest_rate  # 이자 계산
        self.balance += interest  # 잔액에 이자 추가
        print(f"이자 {interest}원이 추가되었습니다")
    
    def __str__(self) -> str:
        """계좌 정보를 문자열로 반환 (이자율 포함)"""
        # 부모의 __str__() 호출 후 이자율 정보 추가
        return super().__str__() + f", 이자율: {self.interest_rate * 100}%"


# 자식 클래스 2: 마이너스 통장
class CheckingAccount(BankAccount):
    """
    마이너스 통장 클래스
    
    일반 계좌에 마이너스 한도 기능이 추가된 계좌입니다.
    """
    
    def __init__(self, owner: str, account_number: str, 
                 balance: float = 0.0, overdraft_limit: float = 0.0) -> None:
        """
        마이너스 통장 초기화
        
        Args:
            owner: 계좌 소유자 이름
            account_number: 계좌번호
            balance: 초기 잔액 (기본값 0.0)
            overdraft_limit: 마이너스 한도 (기본값 0.0)
        """
        super().__init__(owner, account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount: float) -> None:
        """
        출금 처리 (오버라이딩)
        
        마이너스 한도까지 출금 가능하도록 부모 메서드를 재정의합니다.
        
        Args:
            amount: 출금할 금액
            
        Raises:
            ValueError: amount가 0 이하일 때
            InsufficientFundsError: 잔액 + 한도를 초과할 때
        """
        if amount <= 0:
            raise ValueError("출금액은 0보다 커야 합니다")
        
        # 잔액 + 마이너스 한도 확인
        if amount > self.balance + self.overdraft_limit:
            raise InsufficientFundsError()
        
        self.balance -= amount
        print(f"{amount}원이 출금되었습니다")
    
    def __str__(self) -> str:
        """계좌 정보를 문자열로 반환 (마이너스 한도 포함)"""
        return super().__str__() + f", 마이너스 한도: {self.overdraft_limit}원"


# 테스트 코드
if __name__ == "__main__":
    print("=== 은행 계좌 관리 시스템 테스트 ===\n")
    
    # 1. 일반 계좌 테스트
    print("1. 일반 계좌 테스트")
    account1 = BankAccount("홍길동", "1234-5678", 10000)
    print(account1)  # __str__ 호출
    account1.deposit(5000)
    account1.withdraw(3000)
    print(f"현재 잔액: {account1.get_balance()}원")
    
    # 2. 적금 계좌 테스트
    print("\n2. 적금 계좌 테스트")
    savings = SavingsAccount("김철수", "8765-4321", 50000, 0.03)
    print(savings)
    savings.add_interest()
    print(f"현재 잔액: {savings.get_balance()}원")
    
    # 3. 마이너스 통장 테스트
    print("\n3. 마이너스 통장 테스트")
    checking = CheckingAccount("이영희", "1111-2222", 30000, 20000)
    print(checking)
    checking.withdraw(40000)  # 잔액 30000 + 한도 20000 = 50000 범위 내
    print(f"현재 잔액: {checking.get_balance()}원")
    
    # 4. 예외 처리 테스트
    print("\n4. 예외 처리 테스트")
    
    # 잔액 초과 출금 시도
    try:
        account1.withdraw(50000)  # 잔액 12000원인데 50000원 출금 시도
    except InsufficientFundsError as e:
        print(f"잔액 초과 출금 시도 - 에러: {e}")
    
    # 음수 입금 시도
    try:
        account1.deposit(-1000)
    except ValueError as e:
        print(f"음수 입금 시도 - 에러: {e}")
