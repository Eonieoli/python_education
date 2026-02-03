# 3_exercise_solution.py

"""
Day 4 - 7교시: 타입 힌트 (2) - 고급 타입
Exercise - 사용자 관리 시스템 (정답)
"""

from typing import List, Dict, Optional, Union


# ============================================
# 주어진 데이터
# ============================================

users = [
    {"id": 1, "name": "Alice", "age": 17},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 30}
]


# ============================================
# 문제 1 정답 - 나이로 필터링하는 함수
# ============================================

def filter_users_by_age(users: List[Dict[str, Union[str, int]]], min_age: int) -> List[Dict[str, Union[str, int]]]:
    """
    특정 나이 이상인 사용자만 필터링합니다
    
    Args:
        users: 사용자 목록
        min_age: 최소 나이
    
    Returns:
        필터링된 사용자 목록
    """
    result = []
    for user in users:
        if user["age"] >= min_age:
            result.append(user)
    return result


# ============================================
# 문제 2 정답 - ID로 사용자 찾기
# ============================================

def find_user_by_id(users: List[Dict[str, Union[str, int]]], user_id: int) -> Optional[Dict[str, Union[str, int]]]:
    """
    사용자 ID로 사용자를 찾습니다
    
    Args:
        users: 사용자 목록
        user_id: 찾을 사용자 ID
    
    Returns:
        찾은 사용자 정보, 없으면 None
    """
    for user in users:
        if user["id"] == user_id:
            return user
    return None


# ============================================
# 테스트 코드
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
