# 1_basic.py

"""
Day 4 - 7교시: 타입 힌트 (2) - 고급 타입
Basic (강사 시연용)

학습 목표:
- typing 모듈에서 고급 타입 도구 가져오기
- List, Dict 타입 힌트 사용하기
- Optional 타입으로 None 처리하기
- Union 타입으로 여러 타입 허용하기
- *args, **kwargs에 타입 힌트 적용하기
"""

# ============================================
# 1. typing 모듈 import (미리보기)
# ============================================

# typing 모듈에서 고급 타입 도구들을 가져옵니다
# (내일 import를 자세히 배우지만, 오늘은 일단 따라 쓰세요)
from typing import List, Dict, Optional, Union

# Python에 내장되어 있어서 별도 설치 없이 사용 가능합니다
print("typing 모듈을 가져왔습니다!")


# ============================================
# 2. List 타입 힌트
# ============================================

# List[int]: 정수 리스트
def sum_list(numbers: List[int]) -> int:
    """숫자 리스트의 합계를 계산합니다"""
    return sum(numbers)

result = sum_list([10, 20, 30])
print(f"합계: {result}")  # 출력: 합계: 60


# List[str]: 문자열 리스트
def process_names(names: List[str]) -> List[str]:
    """이름 리스트를 모두 대문자로 변환합니다"""
    return [name.upper() for name in names]

names = ["alice", "bob", "charlie"]
upper_names = process_names(names)
print(f"대문자 변환: {upper_names}")  # 출력: 대문자 변환: ['ALICE', 'BOB', 'CHARLIE']


# ============================================
# 3. Dict 타입 힌트
# ============================================

# Dict[str, str]: 문자열 키와 문자열 값
def get_user_info() -> Dict[str, str]:
    """사용자 정보를 딕셔너리로 반환합니다"""
    return {"name": "Alice", "email": "alice@example.com"}

user = get_user_info()
print(f"사용자 정보: {user}")  # 출력: 사용자 정보: {'name': 'Alice', 'email': 'alice@example.com'}


# Dict[str, int]: 문자열 키와 정수 값
def count_items(items: List[str]) -> Dict[str, int]:
    """각 항목의 개수를 세어 딕셔너리로 반환합니다"""
    return {item: items.count(item) for item in set(items)}

fruits = ["사과", "바나나", "사과", "오렌지", "바나나", "사과"]
counts = count_items(fruits)
print(f"과일 개수: {counts}")  # 출력: 과일 개수: {'사과': 3, '바나나': 2, '오렌지': 1}


# ============================================
# 4. Optional 타입 (중요!)
# ============================================

# Optional[타입]: None을 반환할 수 있음을 명시
def get_user(user_id: int) -> Optional[Dict[str, str]]:
    """
    사용자 ID로 사용자를 찾습니다.
    찾으면 사용자 정보를, 못 찾으면 None을 반환합니다.
    """
    # 간단한 예시: user_id가 1이면 찾음, 아니면 None
    if user_id == 1:
        return {"name": "Alice", "email": "alice@example.com"}
    return None

# 사용자를 찾았을 때
found_user = get_user(1)
print(f"찾은 사용자: {found_user}")  # 출력: 찾은 사용자: {'name': 'Alice', 'email': 'alice@example.com'}

# 사용자를 못 찾았을 때
not_found = get_user(999)
print(f"찾은 사용자: {not_found}")  # 출력: 찾은 사용자: None


# Optional[str]: 문자열 또는 None
def find_item(items: List[str], target: str) -> Optional[str]:
    """
    리스트에서 항목을 찾습니다.
    있으면 그 항목을, 없으면 None을 반환합니다.
    """
    return target if target in items else None

fruits = ["사과", "바나나", "오렌지"]
result1 = find_item(fruits, "바나나")
print(f"검색 결과: {result1}")  # 출력: 검색 결과: 바나나

result2 = find_item(fruits, "포도")
print(f"검색 결과: {result2}")  # 출력: 검색 결과: None


# ============================================
# 5. Union 타입 (간단히)
# ============================================

# Union[int, str]: int 또는 str 타입 허용
def process(value: Union[int, str]) -> str:
    """숫자나 문자열을 받아서 문자열로 변환합니다"""
    return str(value)

print(process(123))  # 출력: 123
print(process("hello"))  # 출력: hello


# ============================================
# 6. *args, **kwargs에 타입 힌트
# ============================================

# *args: 여러 개의 int를 받음
def add_all(*args: int) -> int:
    """모든 숫자를 더합니다"""
    return sum(args)

total = add_all(1, 2, 3, 4, 5)
print(f"총합: {total}")  # 출력: 총합: 15


# **kwargs: 여러 개의 str 키-값 쌍을 받음
def create_user(**kwargs: str) -> Dict[str, str]:
    """사용자 정보를 딕셔너리로 생성합니다"""
    return kwargs

new_user = create_user(name="Bob", email="bob@example.com", city="서울")
print(f"새 사용자: {new_user}")  # 출력: 새 사용자: {'name': 'Bob', 'email': 'bob@example.com', 'city': '서울'}
