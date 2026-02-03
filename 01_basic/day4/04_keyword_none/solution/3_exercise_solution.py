# 3_exercise_solution.py

"""
Day 4 - 4교시: 키워드 인수 + None 처리
Exercise - 사용자 프로필 생성 함수 (정답)
"""

# ============================================
# 정답 코드
# ============================================

def create_user_profile(username, email, age=None, city=None, bio=None):
    """사용자 프로필을 생성하는 함수"""
    # None 체크 후 기본값 설정
    if age is None:
        age = "미입력"
    
    if city is None:
        city = "미입력"
    
    if bio is None:
        bio = "소개가 없습니다"
    
    # 딕셔너리 반환
    return {
        "username": username,
        "email": email,
        "age": age,
        "city": city,
        "bio": bio
    }


# ============================================
# 테스트 코드
# ============================================

# 테스트 1: 필수 정보만 입력
profile1 = create_user_profile(
    username="홍길동",
    email="hong@example.com"
)
print(profile1)
# 출력: {'username': '홍길동', 'email': 'hong@example.com', 'age': '미입력', 'city': '미입력', 'bio': '소개가 없습니다'}

# 테스트 2: 일부 선택 정보 입력
profile2 = create_user_profile(
    username="이영희",
    email="lee@example.com",
    age=25,
    city="부산"
)
print(profile2)
# 출력: {'username': '이영희', 'email': 'lee@example.com', 'age': 25, 'city': '부산', 'bio': '소개가 없습니다'}

# 테스트 3: 모든 정보 입력 (키워드 인수 사용)
profile3 = create_user_profile(
    username="김철수",
    email="kim@example.com",
    age=28,
    city="서울",
    bio="Python 개발자"
)
print(profile3)
# 출력: {'username': '김철수', 'email': 'kim@example.com', 'age': 28, 'city': '서울', 'bio': 'Python 개발자'}
