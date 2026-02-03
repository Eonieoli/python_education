# 3_exercise.py

"""
Day 4 - 7교시: 타입 힌트 (2) - 고급 타입
Exercise - 사용자 관리 시스템

문제 1: 사용자 목록 필터링 (10분)
사용자 리스트에서 특정 나이 이상인 사용자만 필터링하는 함수를 작성하세요.

요구사항:
- 함수명: filter_users_by_age
- 매개변수: users (List[Dict[str, Union[str, int]]]), min_age (int)
- 반환 타입: List[Dict[str, Union[str, int]]]
- 기능: min_age 이상인 사용자만 반환

문제 2: 사용자 ID로 검색 (Optional 활용)
사용자 리스트에서 ID로 사용자를 찾는 함수를 작성하세요.
찾으면 사용자 정보를, 못 찾으면 None을 반환하세요.

요구사항:
- 함수명: find_user_by_id
- 매개변수: users (List[Dict[str, Union[str, int]]]), user_id (int)
- 반환 타입: Optional[Dict[str, Union[str, int]]]
- 기능: user_id와 일치하는 사용자를 찾아 반환, 없으면 None

출력 예시:
성인 사용자: [{'id': 2, 'name': 'Bob', 'age': 25}, {'id': 3, 'name': 'Charlie', 'age': 30}]
ID 2번 사용자: {'id': 2, 'name': 'Bob', 'age': 25}
ID 999번 사용자: None
"""

from typing import List, Dict, Optional, Union


# ============================================
# 주어진 데이터
# ============================================

# 사용자 목록
users = [
    {"id": 1, "name": "Alice", "age": 17},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 30}
]


# ============================================
# TODO: 문제 1 - 나이로 필터링하는 함수 작성
# ============================================

# 힌트 1: 빈 리스트를 만들고 for문으로 users를 순회
# 힌트 2: if user["age"] >= min_age: 조건으로 필터링
# 힌트 3: 조건을 만족하면 결과 리스트에 append
def filter_users_by_age(users: List[Dict[str, Union[str, int]]], min_age: int) -> List[Dict[str, Union[str, int]]]:
    pass  # 여기에 코드를 작성하세요


# ============================================
# TODO: 문제 2 - ID로 사용자 찾기 (Optional 활용)
# ============================================

# 힌트 1: for문으로 users를 순회
# 힌트 2: if user["id"] == user_id: 조건으로 찾기
# 힌트 3: 찾으면 바로 return user, 못 찾으면 마지막에 return None
def find_user_by_id(users: List[Dict[str, Union[str, int]]], user_id: int) -> Optional[Dict[str, Union[str, int]]]:
    pass  # 여기에 코드를 작성하세요


# ============================================
# 테스트 코드 (수정하지 마세요)
# ============================================

# 문제 1 테스트
adult_users = filter_users_by_age(users, 18)
print(f"성인 사용자: {adult_users}")
# 출력: 성인 사용자: [{'id': 2, 'name': 'Bob', 'age': 25}, {'id': 3, 'name': 'Charlie', 'age': 30}]

# 문제 2 테스트
user1 = find_user_by_id(users, 2)
print(f"ID 2번 사용자: {user1}")
# 출력: ID 2번 사용자: {'id': 2, 'name': 'Bob', 'age': 25}

user2 = find_user_by_id(users, 999)
print(f"ID 999번 사용자: {user2}")
# 출력: ID 999번 사용자: None
