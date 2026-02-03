# 3_exercise_solution.py

"""
Day 5 - 3교시: 클래스 심화
Exercise - 도서 관리 시스템 (정답)
"""

from typing import List, Optional

# ============================================
# Book 클래스
# ============================================

class Book:
    """책 클래스"""
    
    def __init__(self, title: str, author: str):
        """책 초기화"""
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def borrow(self) -> bool:
        """책 대출"""
        if self.is_borrowed:
            print(f"'{self.title}'은(는) 이미 대출 중입니다")
            return False
        
        self.is_borrowed = True
        print(f"'{self.title}' 대출 완료")
        return True
    
    def return_book(self) -> None:
        """책 반납"""
        self.is_borrowed = False
        print(f"'{self.title}' 반납 완료")
    
    def get_info(self) -> str:
        """책 정보 반환"""
        status = "대출 중" if self.is_borrowed else "대출 가능"
        return f"{self.title} (저자: {self.author}) - {status}"


# ============================================
# Library 클래스
# ============================================

class Library:
    """도서관 클래스"""
    
    def __init__(self, name: str):
        """도서관 초기화"""
        self.name = name
        self.books: List[Book] = []
    
    def add_book(self, book: Book) -> None:
        """책 추가"""
        self.books.append(book)
        print(f"'{book.title}' 도서관에 추가됨")
    
    def find_book(self, title: str) -> Optional[Book]:
        """책 검색"""
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def show_books(self) -> None:
        """책 목록 출력"""
        print(f"\n=== {self.name} 책 목록 ===")
        if not self.books:
            print("책이 없습니다")
            return
        
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book.get_info()}")
        print()


# ============================================
# 테스트 코드
# ============================================

# 도서관 생성
library = Library("중앙 도서관")

# 책 추가
book1 = Book("파이썬 기초", "김철수")
book2 = Book("FastAPI 입문", "이영희")
library.add_book(book1)  # 출력: '파이썬 기초' 도서관에 추가됨
library.add_book(book2)  # 출력: 'FastAPI 입문' 도서관에 추가됨

# 책 목록 출력
library.show_books()
# 출력:
# === 중앙 도서관 책 목록 ===
# 1. 파이썬 기초 (저자: 김철수) - 대출 가능
# 2. FastAPI 입문 (저자: 이영희) - 대출 가능

# 책 대출
book1.borrow()  # 출력: '파이썬 기초' 대출 완료
book1.borrow()  # 출력: '파이썬 기초'은(는) 이미 대출 중입니다

# 책 반납
book1.return_book()  # 출력: '파이썬 기초' 반납 완료
book1.borrow()       # 출력: '파이썬 기초' 대출 완료
