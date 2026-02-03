# 3_exercise.py

"""
Day 5 - 6교시: 스코프 + 데코레이터 개념
Exercise - 방문자 카운터 시스템

문제 1: 전역 변수를 활용한 방문자 카운터
웹사이트 방문자 수를 추적하는 시스템을 만드세요.

요구사항:
1. 전역 변수 visitor_count를 사용하세요
2. visit() 함수는 방문자 수를 1 증가시키고 현재 수를 반환합니다
3. get_visitor_count() 함수는 현재 방문자 수를 반환합니다

출력 예시:
방문자 1명 입장!
방문자 2명 입장!
방문자 3명 입장!
현재 총 방문자: 3명
"""

# ============================================
# TODO: 전역 변수 visitor_count를 0으로 초기화하세요
# ============================================



# ============================================
# TODO: visit() 함수를 작성하세요
# ============================================
# 요구사항:
# 1. global 키워드로 visitor_count 사용
# 2. visitor_count를 1 증가
# 3. "방문자 N명 입장!" 출력
# 힌트: global visitor_count




# ============================================
# TODO: get_visitor_count() 함수를 작성하세요
# ============================================
# 요구사항:
# 1. 현재 visitor_count 반환
# 힌트: return visitor_count



# 테스트 코드
visit()
visit()
visit()
print(f"현재 총 방문자: {get_visitor_count()}명")


print("\n" + "="*50 + "\n")


"""
문제 2: 클래스 변수와 인스턴스 변수 활용

BankAccount 클래스를 완성하세요.

요구사항:
1. 클래스 변수 total_accounts: 전체 계좌 수 추적
2. 인스턴스 변수: owner(예금주), balance(잔액)
3. deposit() 메서드: 입금
4. @property를 사용한 account_info: 계좌 정보 반환

출력 예시:
총 계좌 수: 2개
계좌 정보: 홍길동님, 잔액: 150000원
계좌 정보: 김철수님, 잔액: 70000원
"""

class BankAccount:
    # TODO: 클래스 변수 total_accounts를 0으로 초기화
    
    
    def __init__(self, owner: str, initial_balance: int):
        # TODO: 인스턴스 변수 owner와 balance를 설정
        # TODO: 클래스 변수 total_accounts를 1 증가
        
        
        
    
    def deposit(self, amount: int) -> None:
        # TODO: balance에 amount를 더하고 결과 출력
        # 힌트: "N원 입금되었습니다. 현재 잔액: M원"
        
    
    # TODO: @property 데코레이터를 사용하여 account_info 메서드 작성
    # 반환 형식: "계좌 정보: {owner}님, 잔액: {balance}원"
    


# 테스트 코드
account1 = BankAccount("홍길동", 100000)
account2 = BankAccount("김철수", 50000)

account1.deposit(50000)
account2.deposit(20000)

print(f"\n총 계좌 수: {BankAccount.total_accounts}개")
print(account1.account_info)
print(account2.account_info)
