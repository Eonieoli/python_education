# 2_intermediate_solution.py

"""
Day 4 - 8교시: 함수와 타입 힌트 종합 실습
🟡 응용 Problem - List, Dict, Optional 활용 데이터 처리 (정답)
"""

from typing import List, Dict, Optional


# ============================================
# 1. 사용자 이름 추출
# ============================================

def get_user_names(users: List[Dict[str, any]]) -> List[str]:
    """
    사용자 딕셔너리 리스트에서 이름만 추출합니다.
    
    Args:
        users: 사용자 정보 딕셔너리 리스트
    
    Returns:
        사용자 이름 리스트
    """
    names = [user["name"] for user in users]
    return names


# ============================================
# 2. 사용자 검색
# ============================================

def find_user_by_email(users: List[Dict[str, str]], email: str) -> Optional[Dict[str, str]]:
    """
    이메일로 사용자를 검색합니다.
    
    Args:
        users: 사용자 정보 딕셔너리 리스트
        email: 검색할 이메일
    
    Returns:
        찾은 사용자 딕셔너리 또는 None
    """
    for user in users:
        if user["email"] == email:
            return user
    return None


# ============================================
# 3. 평균 나이 계산
# ============================================

def calculate_average_age(users: List[Dict[str, any]]) -> float:
    """
    사용자 리스트에서 평균 나이를 계산합니다.
    
    Args:
        users: 사용자 정보 딕셔너리 리스트
    
    Returns:
        평균 나이 (소수점 1자리)
    """
    total_age = sum(user["age"] for user in users)
    average = total_age / len(users)
    return round(average, 1)


# ============================================
# 4. 사용자 프로필 생성
# ============================================

def create_user_profile(name: str, age: int, email: Optional[str] = None) -> Dict[str, any]:
    """
    사용자 프로필 딕셔너리를 생성합니다.
    
    Args:
        name: 사용자 이름
        age: 나이
        email: 이메일 (선택사항)
    
    Returns:
        사용자 프로필 딕셔너리
    """
    return {
        "name": name,
        "age": age,
        "email": email
    }


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
    names = get_user_names(users)
    print(f"사용자 이름: {names}")
    # 출력: 사용자 이름: ['홍길동', '김철수', '이영희']
    
    print("\n" + "=" * 50)
    print("2. 사용자 검색")
    print("=" * 50)
    user = find_user_by_email(users, "kim@test.com")
    if user:
        print(f"찾은 사용자: {user['name']}")
    else:
        print("사용자를 찾을 수 없습니다")
    # 출력: 찾은 사용자: 김철수
    
    user = find_user_by_email(users, "unknown@test.com")
    if user:
        print(f"찾은 사용자: {user['name']}")
    else:
        print("사용자를 찾을 수 없습니다")
    # 출력: 사용자를 찾을 수 없습니다
    
    print("\n" + "=" * 50)
    print("3. 평균 나이 계산")
    print("=" * 50)
    avg_age = calculate_average_age(users)
    print(f"평균 나이: {avg_age}세")
    # 출력: 평균 나이: 27.7세
    
    print("\n" + "=" * 50)
    print("4. 사용자 프로필 생성")
    print("=" * 50)
    # 이메일 있음
    profile1 = create_user_profile("박민수", 35, "park@test.com")
    print(f"프로필 1: {profile1}")
    # 출력: 프로필 1: {'name': '박민수', 'age': 35, 'email': 'park@test.com'}
    
    # 이메일 없음
    profile2 = create_user_profile("최지훈", 27)
    print(f"프로필 2: {profile2}")
    # 출력: 프로필 2: {'name': '최지훈', 'age': 27, 'email': None}
