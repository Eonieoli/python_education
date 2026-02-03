# 3_exercise.py

"""
Day 5 - 3교시: 클래스 심화
Exercise - 도서 관리 시스템

문제:
도서관의 책을 관리하는 Book 클래스와 Library 클래스를 작성하세요.

[Book 클래스 요구사항]
1. 속성: title (제목), author (저자), is_borrowed (대출 여부, 기본값 False)
2. 메서드:
   - borrow(): 책을 대출하고 성공 여부 반환
   - return_book(): 책을 반납
   - get_info(): 책 정보 문자열 반환

[Library 클래스 요구사항]
1. 속성: books (책 리스트), name (도서관 이름)
2. 메서드:
   - add_book(): 책 추가
   - find_book(): 제목으로 책 검색
   - show_books(): 모든 책 목록 출력

출력 예시:
'파이썬 기초' 도서관에 추가됨
'FastAPI 입문' 도서관에 추가됨

=== 중앙 도서관 책 목록 ===
1. 파이썬 기초 (저자: 김철수) - 대출 가능
2. FastAPI 입문 (저자: 이영희) - 대출 가능

'파이썬 기초' 대출 완료
'파이썬 기초'은(는) 이미 대출 중입니다
"""

from typing import List, Optional

# ============================================
# Book 클래스
# ============================================

class Book:
    """책 클래스"""
    
    # TODO: __init__ 메서드를 작성하세요
    # 매개변수: title (str), author (str)
    # 속성: title, author, is_borrowed (기본값 False)
    def __init__(self, title: str, author: str):
        pass
    
    
    # TODO: borrow 메서드를 작성하세요
    # 1. 이미 대출 중이면 메시지 출력하고 False 반환
    # 2. 대출 가능하면 is_borrowed를 True로 변경하고 True 반환
    def borrow(self) -> bool:
        pass
    
    
    # TODO: return_book 메서드를 작성하세요
    # is_borrowed를 False로 변경하고 반납 메시지 출력
    def return_book(self) -> None:
        pass
    
    
    # TODO: get_info 메서드를 작성하세요
    # 반환 형식: "제목 (저자: 저자명) - 대출 가능" 또는 "... - 대출 중"
    def get_info(self) -> str:
        pass


# ============================================
# Library 클래스
# ============================================

class Library:
    """도서관 클래스"""
    
    # TODO: __init__ 메서드를 작성하세요
    # 매개변수: name (str)
    # 속성: name, books (빈 리스트)
    def __init__(self, name: str):
        pass
    
    
    # TODO: add_book 메서드를 작성하세요
    # 매개변수: book (Book)
    # books 리스트에 추가하고 메시지 출력
    def add_book(self, book: Book) -> None:
        pass
    
    
    # TODO: find_book 메서드를 작성하세요
    # 매개변수: title (str)
    # 반환: 책을 찾으면 Book 객체, 못 찾으면 None
    def find_book(self, title: str) -> Optional[Book]:
        pass
    
    
    # TODO: show_books 메서드를 작성하세요
    # 모든 책 목록을 번호와 함께 출력
    def show_books(self) -> None:
        pass


# ============================================
# 테스트 코드 (수정하지 마세요)
# ============================================

# 도서관 생성
library = Library("중앙 도서관")

# 책 추가
book1 = Book("파이썬 기초", "김철수")
book2 = Book("FastAPI 입문", "이영희")
library.add_book(book1)
library.add_book(book2)

# 책 목록 출력
library.show_books()

# 책 대출
book1.borrow()
book1.borrow()  # 이미 대출 중

# 책 반납
book1.return_book()
book1.borrow()  # 다시 대출 가능
