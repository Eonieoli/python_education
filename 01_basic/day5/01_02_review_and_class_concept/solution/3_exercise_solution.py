# 3_exercise_solution.py

"""
Day 5 - 01_02: 클래스 기본
Exercise - 상품 재고 관리 시스템 (정답)
"""


# ============================================
# Exercise 1: Product 클래스 (정답)
# ============================================

class Product:
    """상품 재고 관리 클래스"""
    
    def __init__(self, name: str, price: int, stock: int):
        """생성자 메서드"""
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
            print(f"{self.name} {quantity}개 판매 완료! 남은 재고: {self.stock}개")
            return True
    
    def restock(self, quantity: int) -> None:
        """재고 보충 메서드"""
        self.stock += quantity
        print(f"{quantity}개 입고 완료. 현재 재고: {self.stock}개")
    
    def get_info(self) -> str:
        """상품 정보 반환 메서드"""
        return f"상품: {self.name}, 가격: {self.price}원, 재고: {self.stock}개"
    
    def calculate_value(self) -> int:
        """재고 총 가치 계산 메서드"""
        return self.price * self.stock


# Product 클래스 테스트
product = Product("키보드", 50000, 10)

print(product.get_info())  
# 출력: 상품: 키보드, 가격: 50000원, 재고: 10개

product.sell(3)       
# 출력: 키보드 3개 판매 완료! 남은 재고: 7개

product.restock(5)    
# 출력: 5개 입고 완료. 현재 재고: 12개

print(f"재고 총 가치: {product.calculate_value()}원")  
# 출력: 재고 총 가치: 600000원

# 재고 부족 테스트
product.sell(20)      
# 출력: 재고 부족! (현재 재고: 12개)


# ============================================
# Exercise 2: Book 클래스 (정답)
# ============================================

class Book:
    """책 관리 클래스"""
    
    def __init__(self, title: str, author: str, pages: int):
        """생성자 메서드"""
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0  # 현재 읽은 페이지 (기본값 0)
    
    def read(self, pages: int) -> None:
        """책 읽기 메서드"""
        self.current_page += pages
        if self.current_page > self.pages:
            self.current_page = self.pages
        progress = self.get_progress()
        print(f"{pages} 페이지 읽었습니다. (진행률: {progress:.1f}%)")
    
    def get_progress(self) -> float:
        """독서 진행률 계산 메서드"""
        if self.pages == 0:
            return 0.0
        return (self.current_page / self.pages) * 100
    
    def is_finished(self) -> bool:
        """완독 여부 확인 메서드"""
        return self.current_page >= self.pages


# Book 클래스 테스트
book = Book("파이썬 기초", "홍길동", 300)

print(f"제목: {book.title}, 저자: {book.author}, 페이지: {book.pages}")
# 출력: 제목: 파이썬 기초, 저자: 홍길동, 페이지: 300

book.read(50)   
# 출력: 50 페이지 읽었습니다. (진행률: 16.7%)

book.read(100)  
# 출력: 100 페이지 읽었습니다. (진행률: 50.0%)

print(f"완독 여부: {book.is_finished()}")  
# 출력: 완독 여부: False

book.read(150)  
# 출력: 150 페이지 읽었습니다. (진행률: 100.0%)

print(f"완독 여부: {book.is_finished()}")  
# 출력: 완독 여부: True
