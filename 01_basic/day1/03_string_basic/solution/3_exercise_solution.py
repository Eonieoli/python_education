# 3_exercise_solution.py

"""
Day 1 - 3교시: 문자열 기본
Exercise - 프로필 카드 만들기 (정답)
"""

# ============================================
# 주어진 데이터
# ============================================

name = "홍길동"
age = "25"
job = "개발자"


# ============================================
# 정답 코드
# ============================================

# 1. 구분선 만들기
separator = "*" * 30

# 2. 프로필 문자열 조합하기
profile_name = "이름: " + name
profile_age = "나이: " + age + "세"
profile_job = "직업: " + job

# 3. 전체 프로필 문자열 만들기
full_profile = profile_name + profile_age + profile_job

# 4. 프로필 길이 계산
profile_length = len(full_profile)

# 5. 결과 출력
print(separator)
print(profile_name)
print(profile_age)
print(profile_job)
print(separator)
print(f"프로필 길이: {profile_length}글자")


# ============================================
# 실행 결과
# ============================================
# ******************************
# 이름: 홍길동
# 나이: 25세
# 직업: 개발자
# ******************************
# 프로필 길이: 20글자
