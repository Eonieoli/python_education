# 3_exercise_solution.py

"""
Day 5 - 6교시: 스코프 + 데코레이터 개념
Exercise - 방문자 카운터 시스템 (정답)
"""


# ============================================
# 문제 1: 전역 변수를 활용한 방문자 카운터
# ============================================

# 전역 변수 초기화
visitor_count = 0

def visit() -> None:
    """방문자 수 증가"""
    global visitor_count
    visitor_count += 1
    print(f"방문자 {visitor_count}명 입장!")

def get_visitor_count() -> int:
    """현재 방문자 수 반환"""
    return visitor_count

# 테스트 코드
visit()  # 출력: 방문자 1명 입장!
visit()  # 출력: 방문자 2명 입장!
visit()  # 출력: 방문자 3명 입장!
print(f"현재 총 방문자: {get_visitor_count()}명")  # 출력: 현재 총 방문자: 3명


print("\n" + "="*50 + "\n")


# ============================================
# 문제 2: 클래스 변수와 인스턴스 변수 활용
# ============================================

class BankAccount:
    # 클래스 변수: 전체 계좌 수
    total_accounts = 0
    
    def __init__(self, owner: str, initial_balance: int):
        # 인스턴스 변수
        self.owner = owner
        self.balance = initial_balance
        # 클래스 변수 증가
        BankAccount.total_accounts += 1
    
    def deposit(self, amount: int) -> None:
        """입금"""
        self.balance += amount
        print(f"{amount}원 입금되었습니다. 현재 잔액: {self.balance}원")
    
    @property
    def account_info(self) -> str:
        """계좌 정보 반환"""
        return f"계좌 정보: {self.owner}님, 잔액: {self.balance}원"

# 테스트 코드
account1 = BankAccount("홍길동", 100000)
account2 = BankAccount("김철수", 50000)

account1.deposit(50000)  # 출력: 50000원 입금되었습니다. 현재 잔액: 150000원
account2.deposit(20000)  # 출력: 20000원 입금되었습니다. 현재 잔액: 70000원

print(f"\n총 계좌 수: {BankAccount.total_accounts}개")  # 출력: 총 계좌 수: 2개
print(account1.account_info)  # 출력: 계좌 정보: 홍길동님, 잔액: 150000원
print(account2.account_info)  # 출력: 계좌 정보: 김철수님, 잔액: 70000원


print("\n=== 모든 문제 정답 확인 완료! ===")
