# 2_practice.py

"""
Day 5 - 01_02: 클래스 기본
Practice (강사와 함께 실습)

학습 목표:
- 학생 클래스 작성 (타입 힌트 포함)
- 계좌 클래스 작성 (메서드 활용)
- 클래스 기반 프로그래밍 연습
"""


# ============================================
# 실습 1: 학생 클래스 만들기 (처음부터 끝까지)
# ============================================

# Student 클래스 정의
class Student:
    """학생 정보를 관리하는 클래스"""
    
    def __init__(self, name: str, student_id: str, grade: int):
        """
        생성자 메서드
        name: 학생 이름
        student_id: 학번
        grade: 학년
        """
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.scores = []  # 성적 리스트 (빈 리스트로 시작)
    
    def add_score(self, score: int) -> None:
        """성적 추가 메서드"""
        self.scores.append(score)
        print(f"{self.name} 학생의 성적 {score}점이 추가되었습니다.")
    
    def get_average(self) -> float:
        """평균 성적 계산 메서드"""
        if len(self.scores) == 0:
            return 0.0
        return sum(self.scores) / len(self.scores)
    
    def get_info(self) -> str:
        """학생 정보 반환 메서드"""
        avg = self.get_average()
        return f"이름: {self.name}, 학번: {self.student_id}, 학년: {self.grade}, 평균: {avg:.1f}점"


# Student 객체 생성 및 사용
student1 = Student("김철수", "2024001", 1)

# 성적 추가
student1.add_score(85)  # 출력: 김철수 학생의 성적 85점이 추가되었습니다.
student1.add_score(90)  # 출력: 김철수 학생의 성적 90점이 추가되었습니다.
student1.add_score(88)  # 출력: 김철수 학생의 성적 88점이 추가되었습니다.

# 학생 정보 출력
print(student1.get_info())  
# 출력: 이름: 김철수, 학번: 2024001, 학년: 1, 평균: 87.7점


# ============================================
# 실습 2: 계좌 클래스 만들기 (TODO)
# ============================================

# TODO: Account 클래스를 작성하세요
# 요구사항:
# - owner(소유자), balance(잔액) 인스턴스 변수
# - deposit(입금), withdraw(출금), check_balance(잔액 확인) 메서드
# - 모든 메서드에 타입 힌트 추가

class Account:
    """계좌 관리 클래스"""
    
    def __init__(self, owner: str, balance: int = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: int) -> None:
        """입금 메서드"""
        self.balance += amount
        print(f"{amount}원 입금되었습니다. 잔액: {self.balance}원")
    
    def withdraw(self, amount: int) -> bool:
        """출금 메서드"""
        if amount > self.balance:
            print("잔액이 부족합니다!")
            return False
        self.balance -= amount
        print(f"{amount}원 출금되었습니다. 잔액: {self.balance}원")
        return True
    
    def check_balance(self) -> int:
        """잔액 확인 메서드"""
        return self.balance


# 계좌 사용 예시
my_account = Account("홍길동", 50000)

print(f"소유자: {my_account.owner}")  # 출력: 소유자: 홍길동
print(f"잔액: {my_account.check_balance()}원")  # 출력: 잔액: 50000원

my_account.deposit(20000)   # 출력: 20000원 입금되었습니다. 잔액: 70000원
my_account.withdraw(30000)  # 출력: 30000원 출금되었습니다. 잔액: 40000원


# ============================================
# 실습 3: 상품 클래스 만들기 (TODO)
# ============================================

# TODO: Item 클래스를 작성하세요
# 요구사항:
# - name(상품명), price(가격), quantity(수량) 인스턴스 변수
# - get_total_price() 메서드: 총 가격 계산 (가격 × 수량)
# - apply_discount() 메서드: 할인율 적용

class Item:
    """상품 관리 클래스"""
    
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_total_price(self) -> int:
        """총 가격 계산"""
        return self.price * self.quantity
    
    def apply_discount(self, discount_rate: float) -> int:
        """
        할인 적용
        discount_rate: 할인율 (0.1 = 10% 할인)
        """
        total = self.get_total_price()
        discounted = int(total * (1 - discount_rate))
        return discounted


# 상품 사용 예시
item = Item("노트북", 1000000, 2)

print(f"상품: {item.name}")  # 출력: 상품: 노트북
print(f"총 가격: {item.get_total_price()}원")  # 출력: 총 가격: 2000000원

discounted_price = item.apply_discount(0.15)  # 15% 할인
print(f"할인 후: {discounted_price}원")  # 출력: 할인 후: 1700000원
