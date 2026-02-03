# 2_intermediate.py

"""
Day 4 - 8교시: 함수와 타입 힌트 종합 실습
🟡 응용 Problem - List, Dict, Optional 활용 데이터 처리

문제:
사용자 데이터를 처리하는 함수들을 작성하세요.
List, Dict, Optional 타입을 활용하고 완벽한 타입 힌트를 추가하세요.

요구사항:
1. 사용자 목록에서 정보 추출
2. 사용자 검색 (Optional 활용)
3. 통계 계산 (List 활용)
4. 딕셔너리 변환

제한 시간: 15분
"""

from typing import List, Dict, Optional


# ============================================
# TODO 1: 사용자 이름 추출 (3분)
# ============================================

# 사용자 딕셔너리 리스트에서 이름만 추출하여 리스트로 반환하세요
# 타입 힌트: List[Dict[str, any]] -> List[str]
# 
# 예시:
# users = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
# 결과: ["Alice", "Bob"]
def get_user_names():
    pass


# ============================================
# TODO 2: 사용자 검색 (5분)
# ============================================

# 이메일로 사용자를 검색하세요
# 찾으면 사용자 딕셔너리를 반환하고, 못 찾으면 None을 반환
# 타입 힌트: List[Dict[str, str]], str -> Optional[Dict[str, str]]
#
# 예시:
# users = [
#     {"name": "Alice", "email": "alice@test.com"},
#     {"name": "Bob", "email": "bob@test.com"}
# ]
# find_user_by_email(users, "alice@test.com")  # Alice 딕셔너리 반환
# find_user_by_email(users, "unknown@test.com")  # None 반환
def find_user_by_email():
    pass


# ============================================
# TODO 3: 평균 나이 계산 (4분)
# ============================================

# 사용자 리스트에서 평균 나이를 계산하세요
# 소수점 1자리까지 반올림
# 타입 힌트: List[Dict[str, any]] -> float
#
# 예시:
# users = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
# 결과: 27.5
def calculate_average_age():
    pass


# ============================================
# TODO 4: 사용자 프로필 생성 (3분)
# ============================================

# 이름, 나이, 이메일을 받아서 사용자 프로필 딕셔너리를 생성하세요
# 이메일은 선택사항입니다 (기본값: None)
# 타입 힌트: str, int, Optional[str] -> Dict[str, any]
#
# 예시:
# create_user_profile("Alice", 25, "alice@test.com")
# 결과: {"name": "Alice", "age": 25, "email": "alice@test.com"}
#
# create_user_profile("Bob", 30)
# 결과: {"name": "Bob", "age": 30, "email": None}
def create_user_profile():
    pass


# ============================================
# 결과 확인
# ============================================

if __name__ == "__main__":
    # 테스트 데이터
    users = [
        {"name": "홍길동", "age": 25, "email": "hong@test.com"},
        {"name": "김철수", "age": 30, "email": "kim@test.com"},
        {"name": "이영희", "age": 28, "email": "lee@test.com"}
    ]
    
    print("=" * 50)
    print("1. 사용자 이름 추출")
    print("=" * 50)
    # names = get_user_names(users)
    # print(f"사용자 이름: {names}")
    # 출력: 사용자 이름: ['홍길동', '김철수', '이영희']
    
    print("\n" + "=" * 50)
    print("2. 사용자 검색")
    print("=" * 50)
    # user = find_user_by_email(users, "kim@test.com")
    # if user:
    #     print(f"찾은 사용자: {user['name']}")
    # else:
    #     print("사용자를 찾을 수 없습니다")
    # 출력: 찾은 사용자: 김철수
    
    # user = find_user_by_email(users, "unknown@test.com")
    # if user:
    #     print(f"찾은 사용자: {user['name']}")
    # else:
    #     print("사용자를 찾을 수 없습니다")
    # 출력: 사용자를 찾을 수 없습니다
    
    print("\n" + "=" * 50)
    print("3. 평균 나이 계산")
    print("=" * 50)
    # avg_age = calculate_average_age(users)
    # print(f"평균 나이: {avg_age}세")
    # 출력: 평균 나이: 27.7세
    
    print("\n" + "=" * 50)
    print("4. 사용자 프로필 생성")
    print("=" * 50)
    # # 이메일 있음
    # profile1 = create_user_profile("박민수", 35, "park@test.com")
    # print(f"프로필 1: {profile1}")
    # 출력: 프로필 1: {'name': '박민수', 'age': 35, 'email': 'park@test.com'}
    
    # # 이메일 없음
    # profile2 = create_user_profile("최지훈", 27)
    # print(f"프로필 2: {profile2}")
    # 출력: 프로필 2: {'name': '최지훈', 'age': 27, 'email': None}
