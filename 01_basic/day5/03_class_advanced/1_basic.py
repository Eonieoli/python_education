# 1_basic.py

"""
Day 5 - 3교시: 클래스 심화
Basic (강사 시연용)

학습 목표:
- 여러 메서드를 가진 클래스 설계
- 인스턴스 변수 vs 클래스 변수 이해
- 실전 패턴 적용 (장바구니, 계좌 등)
"""

# ============================================
# 1. 여러 메서드를 가진 클래스
# ============================================

class BankAccount:
    """은행 계좌 클래스 - 여러 메서드 예제"""
    
    def __init__(self, owner: str, balance: int = 0):
        """계좌 초기화"""
        self.owner = owner      # 예금주
        self.balance = balance  # 잔액
    
    def deposit(self, amount: int) -> None:
        """입금 메서드"""
        self.balance += amount
        print(f"{amount}원 입금 완료. 잔액: {self.balance}원")
    
    def withdraw(self, amount: int) -> bool:
        """출금 메서드 - 성공 여부 반환"""
        if amount > self.balance:
            print(f"잔액 부족! 현재 잔액: {self.balance}원")
            return False
        
        self.balance -= amount
        print(f"{amount}원 출금 완료. 잔액: {self.balance}원")
        return True
    
    def get_balance(self) -> int:
        """잔액 조회 메서드"""
        return self.balance

# 계좌 사용 예시
account = BankAccount("홍길동", 10000)
account.deposit(5000)   # 출력: 5000원 입금 완료. 잔액: 15000원
account.withdraw(3000)  # 출력: 3000원 출금 완료. 잔액: 12000원
account.withdraw(20000) # 출력: 잔액 부족! 현재 잔액: 12000원


# ============================================
# 2. 인스턴스 변수 vs 클래스 변수
# ============================================

class User:
    """사용자 클래스 - 클래스 변수 예제"""
    
    # 클래스 변수: 모든 인스턴스가 공유하는 변수
    total_users = 0
    
    def __init__(self, name: str, email: str):
        """사용자 초기화"""
        # 인스턴스 변수: 각 인스턴스마다 고유한 변수
        self.name = name
        self.email = email
        
        # 클래스 변수 증가
        User.total_users += 1
    
    def get_info(self) -> str:
        """사용자 정보 반환"""
        return f"{self.name} ({self.email})"

# 사용자 생성
user1 = User("김철수", "kim@example.com")
user2 = User("이영희", "lee@example.com")
user3 = User("박민수", "park@example.com")

# 각 인스턴스는 고유한 정보를 가짐
print(user1.get_info())  # 출력: 김철수 (kim@example.com)
print(user2.get_info())  # 출력: 이영희 (lee@example.com)

# 클래스 변수는 모든 인스턴스가 공유
print(f"전체 사용자 수: {User.total_users}명")  # 출력: 전체 사용자 수: 3명


# ============================================
# 3. 실전 패턴: 장바구니 클래스
# ============================================

from typing import List, Dict

class ShoppingCart:
    """온라인 쇼핑몰 장바구니 클래스"""
    
    def __init__(self):
        """장바구니 초기화 - 빈 리스트로 시작"""
        self.items: List[Dict[str, int]] = []
    
    def add_item(self, name: str, price: int, quantity: int = 1) -> None:
        """상품 추가"""
        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.items.append(item)
        print(f"{name} {quantity}개 추가됨")
    
    def get_total(self) -> int:
        """총 금액 계산"""
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]
        return total
    
    def show_items(self) -> None:
        """장바구니 내역 출력"""
        print("\n=== 장바구니 ===")
        for item in self.items:
            subtotal = item["price"] * item["quantity"]
            print(f"{item['name']}: {item['price']}원 x {item['quantity']}개 = {subtotal}원")
        print(f"총 금액: {self.get_total()}원\n")

# 장바구니 사용 예시
cart = ShoppingCart()
cart.add_item("노트북", 1500000)      # 출력: 노트북 1개 추가됨
cart.add_item("마우스", 30000, 2)     # 출력: 마우스 2개 추가됨
cart.add_item("키보드", 80000)        # 출력: 키보드 1개 추가됨
cart.show_items()
# 출력:
# === 장바구니 ===
# 노트북: 1500000원 x 1개 = 1500000원
# 마우스: 30000원 x 2개 = 60000원
# 키보드: 80000원 x 1개 = 80000원
# 총 금액: 1640000원
