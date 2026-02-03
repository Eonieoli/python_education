# 3_exercise.py

"""
Day 4 - 4교시: 키워드 인수 + None 처리
Exercise - 사용자 프로필 생성 함수

문제:
온라인 서비스의 사용자 프로필을 생성하는 함수를 작성하세요.
선택적 정보는 None을 기본값으로 하고, None일 때 적절한 기본값을 설정하세요.

요구사항:
1. 함수명: create_user_profile
2. 필수 매개변수:
   - username: 사용자명
   - email: 이메일
3. 선택적 매개변수 (기본값 None):
   - age: 나이 → None이면 "미입력"
   - city: 도시 → None이면 "미입력"
   - bio: 자기소개 → None이면 "소개가 없습니다"
4. 반환값: 사용자 프로필 딕셔너리

출력 예시:
{'username': '홍길동', 'email': 'hong@example.com', 'age': '미입력', 'city': '미입력', 'bio': '소개가 없습니다'}
{'username': '김철수', 'email': 'kim@example.com', 'age': 28, 'city': '서울', 'bio': 'Python 개발자'}
"""

# ============================================
# TODO: 여기서부터 코드를 작성하세요
# ============================================

# 함수 작성
# 힌트: def create_user_profile(username, email, age=None, city=None, bio=None):
def create_user_profile(username, email, age=None, city=None, bio=None):
    # 각 선택적 매개변수에 대해 None 체크 후 기본값 설정
    # 힌트: if age is None: age = "미입력"
    
    
    # 딕셔너리 반환
    # 힌트: return {"username": username, "email": email, ...}
    


# ============================================
# 테스트 코드 (수정하지 마세요)
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
