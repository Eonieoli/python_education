# 1_basic.py

"""
Day 5 - 01_02: 클래스 기본
Basic (강사 시연용)

학습 목표:
- 클래스와 객체의 개념 이해
- __init__ 메서드와 self의 역할
- 인스턴스 변수와 메서드 작성
- 타입 힌트를 활용한 클래스 작성
"""


# ============================================
# 📌 1교시 복습: 타입 힌트 복습
# ============================================

# 함수와 타입 힌트 복습
def greet(name: str) -> str:
    return f"Hello, {name}"

print(greet("Alice"))  # 출력: Hello, Alice


from typing import List, Dict, Optional

def get_users() -> List[str]:
    return ["Alice", "Bob", "Charlie"]

print(get_users())  # 출력: ['Alice', 'Bob', 'Charlie']


# ============================================
# 📌 2교시 시작: 클래스 기본
# ============================================

# ============================================
# 1. 첫 번째 클래스 만들기
# ============================================

# User 클래스 정의
class User:
    """사용자 정보를 관리하는 클래스"""
    
    def __init__(self, name: str, age: int):
        """
        생성자 메서드
        name: 사용자 이름
        age: 사용자 나이
        """
        self.name = name  # 인스턴스 변수
        self.age = age    # 인스턴스 변수
    
    def greet(self) -> str:
        """인사 메시지를 반환하는 메서드"""
        return f"안녕하세요, 저는 {self.name}입니다."
    
    def is_adult(self) -> bool:
        """성인 여부를 확인하는 메서드"""
        return self.age >= 18


# User 객체 생성
user1 = User("홍길동", 25)

# 속성 접근
print(user1.name)  # 출력: 홍길동
print(user1.age)   # 출력: 25

# 메서드 호출
print(user1.greet())      # 출력: 안녕하세요, 저는 홍길동입니다.
print(user1.is_adult())   # 출력: True


# ============================================
# 2. 여러 인스턴스 생성하기
# ============================================

# 여러 User 객체 생성
user1 = User("홍길동", 25)
user2 = User("김철수", 17)
user3 = User("이영희", 30)

# 각각 독립적인 객체
print(user1.name, user1.age)  # 출력: 홍길동 25
print(user2.name, user2.age)  # 출력: 김철수 17
print(user3.name, user3.age)  # 출력: 이영희 30

print(user2.is_adult())  # 출력: False (17세는 미성년자)


# ============================================
# 3. 실전 예제: 은행 계좌 클래스
# ============================================

class BankAccount:
    """은행 계좌를 관리하는 클래스"""
    
    def __init__(self, owner: str, balance: int = 0):
        """
        생성자 메서드
        owner: 계좌 소유자
        balance: 초기 잔액 (기본값 0)
        """
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: int) -> None:
        """입금 메서드"""
        self.balance += amount
        print(f"{amount}원 입금 완료. 현재 잔액: {self.balance}원")
    
    def withdraw(self, amount: int) -> bool:
        """출금 메서드 (성공 여부 반환)"""
        if amount > self.balance:
            print("잔액이 부족합니다!")
            return False
        else:
            self.balance -= amount
            print(f"{amount}원 출금 완료. 현재 잔액: {self.balance}원")
            return True
    
    def get_balance(self) -> int:
        """현재 잔액 조회"""
        return self.balance


# 은행 계좌 사용하기
account = BankAccount("홍길동", 10000)

print(f"계좌 소유자: {account.owner}")  # 출력: 계좌 소유자: 홍길동
print(f"현재 잔액: {account.get_balance()}원")  # 출력: 현재 잔액: 10000원

account.deposit(5000)   # 출력: 5000원 입금 완료. 현재 잔액: 15000원
account.withdraw(3000)  # 출력: 3000원 출금 완료. 현재 잔액: 12000원
account.withdraw(20000) # 출력: 잔액이 부족합니다!


# ============================================
# 4. 실전 예제: 상품 클래스
# ============================================

class Product:
    """상품 정보를 관리하는 클래스"""
    
    def __init__(self, name: str, price: int, stock: int):
        """
        생성자 메서드
        name: 상품명
        price: 가격
        stock: 재고 수량
        """
        self.name = name
        self.price = price
        self.stock = stock
    
    def sell(self, quantity: int) -> bool:
        """상품 판매 메서드"""
        if quantity > self.stock:
            print(f"재고 부족! (현재 재고: {self.stock}개)")
            return False
        else:
            self.stock -= quantity
            total_price = self.price * quantity
            print(f"{self.name} {quantity}개 판매 완료!")
            print(f"판매 금액: {total_price}원, 남은 재고: {self.stock}개")
            return True
    
    def restock(self, quantity: int) -> None:
        """재고 보충 메서드"""
        self.stock += quantity
        print(f"{quantity}개 입고 완료. 현재 재고: {self.stock}개")


# 상품 관리하기
laptop = Product("노트북", 1200000, 5)

print(f"상품: {laptop.name}, 가격: {laptop.price}원")  
# 출력: 상품: 노트북, 가격: 1200000원

laptop.sell(2)       # 2개 판매
# 출력: 노트북 2개 판매 완료!
#       판매 금액: 2400000원, 남은 재고: 3개

laptop.restock(10)   # 10개 입고
# 출력: 10개 입고 완료. 현재 재고: 13개
