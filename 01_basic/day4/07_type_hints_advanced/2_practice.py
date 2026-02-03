# 2_practice.py

"""
Day 4 - 7교시: 타입 힌트 (2) - 고급 타입
Practice (강사와 함께 실습)

학습 목표:
- List, Dict 타입 힌트로 함수 작성하기
- Optional 타입으로 안전한 함수 만들기
- 복잡한 타입 조합 연습하기
"""

from typing import List, Dict, Optional, Union


# ============================================
# 실습 1: List, Dict 타입 힌트 (처음 보는 패턴이니 전체 타이핑)
# ============================================

# 학생 점수 리스트의 평균을 계산하는 함수
def calculate_average(scores: List[int]) -> float:
    """학생들의 점수 평균을 계산합니다"""
    return sum(scores) / len(scores)

# 테스트
scores = [85, 90, 78, 92, 88]
avg = calculate_average(scores)
print(f"평균 점수: {avg:.1f}점")  # 출력: 평균 점수: 86.6점


# 상품 정보를 딕셔너리로 반환하는 함수
def create_product(name: str, price: int) -> Dict[str, Union[str, int]]:
    """상품 이름과 가격으로 상품 정보 딕셔너리를 생성합니다"""
    return {"name": name, "price": price}

# 테스트
product = create_product("노트북", 1200000)
print(f"상품 정보: {product}")  # 출력: 상품 정보: {'name': '노트북', 'price': 1200000}


# ============================================
# 실습 2: Optional 타입으로 검색 함수 (TODO)
# ============================================

# 이메일 목록에서 특정 도메인의 이메일을 찾는 함수
emails = ["alice@gmail.com", "bob@naver.com", "charlie@gmail.com"]

# TODO: 특정 도메인(domain)을 포함하는 첫 번째 이메일을 찾는 함수를 작성하세요
# 함수명: find_email_by_domain
# 매개변수: emails (List[str]), domain (str)
# 반환 타입: Optional[str] (찾으면 이메일, 못 찾으면 None)
# 힌트: for문으로 순회하며 if domain in email: return email
def find_email_by_domain(emails: List[str], domain: str) -> Optional[str]:
    for email in emails:
        if domain in email:
            return email
    return None

# 테스트
result1 = find_email_by_domain(emails, "gmail.com")
print(f"gmail.com 이메일: {result1}")  # 출력: gmail.com 이메일: alice@gmail.com

result2 = find_email_by_domain(emails, "daum.net")
print(f"daum.net 이메일: {result2}")  # 출력: daum.net 이메일: None


# ============================================
# 실습 3: Dict[str, int]로 단어 빈도수 세기 (TODO)
# ============================================

# 텍스트에서 각 단어가 몇 번 나타나는지 세는 함수
words = ["python", "java", "python", "javascript", "python", "java"]

# TODO: 단어 리스트를 받아서 각 단어의 빈도수를 세는 함수를 작성하세요
# 함수명: count_words
# 매개변수: words (List[str])
# 반환 타입: Dict[str, int]
# 힌트: 빈 딕셔너리를 만들고, for문으로 순회하며 word를 키로, count를 값으로 저장
def count_words(words: List[str]) -> Dict[str, int]:
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

# 테스트
word_count = count_words(words)
print(f"단어 빈도수: {word_count}")  # 출력: 단어 빈도수: {'python': 3, 'java': 2, 'javascript': 1}
