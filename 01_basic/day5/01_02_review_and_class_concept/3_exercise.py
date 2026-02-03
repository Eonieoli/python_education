# 3_exercise.py

"""
Day 5 - 01_02: 클래스 기본
Exercise - 상품 재고 관리 시스템

문제:
쇼핑몰의 상품 재고를 관리하는 Product 클래스를 작성하세요.

요구사항:
1. Product 클래스를 작성하세요
   - name (상품명)
   - price (가격)
   - stock (재고 수량)
   
2. 다음 메서드를 구현하세요:
   - sell(quantity): 상품 판매 (재고 감소)
   - restock(quantity): 재고 보충 (재고 증가)
   - get_info(): 상품 정보 반환
   - calculate_value(): 재고 총 가치 계산 (가격 × 재고)

3. 모든 메서드에 타입 힌트를 추가하세요

출력 예시:
상품: 키보드, 가격: 50000원, 재고: 10개
키보드 3개 판매 완료! 남은 재고: 7개
5개 입고 완료. 현재 재고: 12개
재고 총 가치: 600000원
"""


# ============================================
# TODO: Product 클래스를 작성하세요
# ============================================

class Product:
    """상품 재고 관리 클래스"""
    
    def __init__(self, name: str, price: int, stock: int):
        """
        생성자 메서드
        TODO: 인스턴스 변수를 초기화하세요
        """
        # 힌트: self.name = name
        
    
    def sell(self, quantity: int) -> bool:
        """
        상품 판매 메서드
        TODO: 재고가 충분한지 확인하고 판매 처리
        """
        # 힌트: 
        # 1. quantity가 self.stock보다 크면 False 반환
        # 2. 그렇지 않으면 self.stock에서 quantity를 빼고 True 반환
        
    
    def restock(self, quantity: int) -> None:
        """
        재고 보충 메서드
        TODO: 재고를 증가시키세요
        """
        # 힌트: self.stock += quantity
        
    
    def get_info(self) -> str:
        """
        상품 정보 반환 메서드
        TODO: 상품 정보를 문자열로 반환하세요
        """
        # 힌트: f"상품: {self.name}, 가격: {self.price}원, 재고: {self.stock}개"
        
    
    def calculate_value(self) -> int:
        """
        재고 총 가치 계산 메서드
        TODO: 가격 × 재고 수량을 계산하세요
        """
        # 힌트: self.price * self.stock
        


# ============================================
# TODO: Product 클래스를 테스트하세요
# ============================================

# 1. Product 객체 생성
# 힌트: product = Product("키보드", 50000, 10)


# 2. 상품 정보 출력
# 힌트: print(product.get_info())


# 3. 상품 판매 (3개)
# 힌트: product.sell(3)


# 4. 재고 보충 (5개)
# 힌트: product.restock(5)


# 5. 재고 총 가치 출력
# 힌트: print(f"재고 총 가치: {product.calculate_value()}원")


# ============================================
# Exercise 2: Book 클래스 (도전 과제)
# ============================================

"""
Book 클래스를 작성하세요.

요구사항:
1. Book 클래스를 작성하세요
   - title (제목)
   - author (저자)
   - pages (페이지 수)
   - current_page (현재 읽은 페이지, 기본값 0)

2. 다음 메서드를 구현하세요:
   - read(pages): 책 읽기 (current_page 증가)
   - get_progress(): 독서 진행률 계산 (현재 페이지 / 전체 페이지 × 100)
   - is_finished(): 완독 여부 확인 (current_page >= pages)

출력 예시:
제목: 파이썬 기초, 저자: 홍길동, 페이지: 300
50 페이지 읽었습니다. (진행률: 16.7%)
100 페이지 읽었습니다. (진행률: 50.0%)
완독 여부: False
"""

# TODO: Book 클래스를 작성하세요

class Book:
    """책 관리 클래스"""
    
    # TODO: __init__ 메서드 작성
    
    
    # TODO: read 메서드 작성
    
    
    # TODO: get_progress 메서드 작성
    
    
    # TODO: is_finished 메서드 작성
    


# TODO: Book 클래스 테스트
# 힌트: book = Book("파이썬 기초", "홍길동", 300)
