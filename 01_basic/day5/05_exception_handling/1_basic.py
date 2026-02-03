# 1_basic.py

"""
Day 5 - 5교시: 예외 처리
Basic (강사 시연용)

학습 목표:
- try-except 기본 문법 이해
- Exception as e로 에러 정보 활용
- finally를 사용한 정리 작업
- raise로 예외 발생시키기
- 클래스 메서드에서 예외 처리
"""

# ============================================
# 1. 기본 try-except
# ============================================

# 0으로 나누기 - 예외 발생!
def divide(a: int, b: int) -> float:
    """두 숫자를 나누는 함수"""
    try:
        # 나눗셈 시도
        result = a / b
        return result
    except ZeroDivisionError:
        # 0으로 나누면 이 블록 실행
        print("❌ 오류: 0으로 나눌 수 없습니다")
        return 0.0

# 테스트
print("=== 기본 try-except ===")
print(divide(10, 2))  # 출력: 5.0
print(divide(10, 0))  # 출력: ❌ 오류: 0으로 나눌 수 없습니다 \n 0.0
print()


# ============================================
# 2. Exception as e - 에러 정보 활용
# ============================================

# 문자열을 숫자로 변환
def process_data(data: str) -> int:
    """문자열을 정수로 변환하는 함수"""
    try:
        # 변환 시도
        number = int(data)
        return number
    except ValueError as e:
        # 에러 메시지 출력
        print(f"❌ 변환 실패: {e}")
        return 0

# 테스트
print("=== Exception as e ===")
print(process_data("123"))  # 출력: 123
print(process_data("abc"))  # 출력: ❌ 변환 실패: invalid literal for int()... \n 0
print()


# ============================================
# 3. finally - 항상 실행되는 코드
# ============================================

# 파일 읽기 (finally로 안전하게 닫기)
def read_file(filename: str) -> str:
    """파일을 읽는 함수"""
    f = None
    try:
        # 파일 열기 시도
        f = open(filename, 'r', encoding='utf-8')
        content = f.read()
        return content
    except FileNotFoundError:
        # 파일이 없을 때
        print(f"❌ 파일을 찾을 수 없습니다: {filename}")
        return ""
    finally:
        # 항상 실행! (파일 닫기)
        if f is not None:
            f.close()
            print("✅ 파일을 닫았습니다")

# 테스트 (실제 파일이 없어도 finally는 실행됨)
print("=== finally ===")
result = read_file("없는파일.txt")
print()


# ============================================
# 4. raise - 예외 직접 발생시키기
# ============================================

# 나이 검증 함수
def validate_age(age: int) -> None:
    """나이가 유효한지 검증하는 함수"""
    if age < 0:
        # 예외 발생!
        raise ValueError("나이는 0 이상이어야 합니다")
    if age > 150:
        raise ValueError("나이가 너무 많습니다")
    print(f"✅ 유효한 나이: {age}세")

# 테스트
print("=== raise로 예외 발생 ===")
try:
    validate_age(25)   # 출력: ✅ 유효한 나이: 25세
    validate_age(-5)   # ValueError 발생!
except ValueError as e:
    print(f"❌ 검증 실패: {e}")
print()


# ============================================
# 5. 클래스 메서드에서 예외 처리
# ============================================

class BankAccount:
    """은행 계좌 클래스"""
    
    def __init__(self, balance: int):
        """초기 잔액으로 계좌 생성"""
        self.balance = balance
    
    def withdraw(self, amount: int) -> None:
        """돈을 인출하는 메서드"""
        if amount > self.balance:
            # 잔액 부족 시 예외 발생
            raise ValueError(f"잔액 부족! (잔액: {self.balance}원, 요청: {amount}원)")
        
        # 인출 성공
        self.balance -= amount
        print(f"✅ {amount}원 인출 완료 (잔액: {self.balance}원)")
    
    def deposit(self, amount: int) -> None:
        """돈을 입금하는 메서드"""
        if amount <= 0:
            raise ValueError("입금액은 0보다 커야 합니다")
        
        self.balance += amount
        print(f"✅ {amount}원 입금 완료 (잔액: {self.balance}원)")

# 테스트
print("=== 클래스 메서드 예외 처리 ===")
account = BankAccount(10000)

try:
    account.withdraw(3000)   # 출력: ✅ 3000원 인출 완료 (잔액: 7000원)
    account.deposit(5000)    # 출력: ✅ 5000원 입금 완료 (잔액: 12000원)
    account.withdraw(20000)  # ValueError 발생!
except ValueError as e:
    print(f"❌ 거래 실패: {e}")
