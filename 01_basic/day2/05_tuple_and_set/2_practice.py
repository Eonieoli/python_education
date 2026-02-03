# 2_practice.py

"""
Day 2 - 5교시: 튜플 + 집합
Practice (강사와 함께 실습)

학습 목표:
- 좌표 처리 (x, y)
- RGB 색상값 (r, g, b)
- 여러 변수 동시 할당
- 스와핑 실습
- 태그 중복 제거
- 허용 사용자 목록 (set + in)
"""

# ============================================
# 실습 1: 좌표 처리 - 튜플 언패킹 (전체 타이핑)
# ============================================

# 화면의 한 점을 튜플로 표현
point = (150, 250)

# 언패킹으로 x, y 좌표를 분리
x, y = point

# 결과 출력
print(f"점의 위치: x={x}, y={y}")  # 출력: 점의 위치: x=150, y=250

# 또 다른 점
start = (0, 0)
end = (100, 200)

# 두 점 모두 언패킹
start_x, start_y = start
end_x, end_y = end

print(f"시작점: ({start_x}, {start_y})")  # 출력: 시작점: (0, 0)
print(f"끝점: ({end_x}, {end_y})")  # 출력: 끝점: (100, 200)


# ============================================
# 실습 2: RGB 색상값 언패킹 (TODO)
# ============================================

# 빨간색 RGB 값
red_color = (255, 0, 0)

# TODO: 튜플을 언패킹하여 r, g, b 변수에 할당하세요
# 힌트: r, g, b = red_color
r, g, b = red_color

# TODO: f-string으로 RGB 값을 출력하세요
# 출력 예시: Red: R=255, G=0, B=0
print(f"Red: R={r}, G={g}, B={b}")


# 파란색 RGB 값
blue_color = (0, 0, 255)

# TODO: 파란색도 언패킹하고 출력하세요
r, g, b = blue_color
print(f"Blue: R={r}, G={g}, B={b}")


# ============================================
# 실습 3: 값 교환 (스와핑) (TODO)
# ============================================

# 두 변수의 값
first = "A"
second = "B"

print(f"교환 전: first={first}, second={second}")
# 출력: 교환 전: first=A, second=B

# TODO: 튜플 언패킹으로 first와 second 값을 교환하세요
# 힌트: first, second = second, first
first, second = second, first

print(f"교환 후: first={first}, second={second}")
# 출력: 교환 후: first=B, second=A


# ============================================
# 실습 4: 집합으로 중복 제거 (전체 타이핑)
# ============================================

# 설문조사 응답 (중복 포함)
survey_responses = ["파이썬", "자바", "파이썬", "C++", "자바", "파이썬", "Go"]

# 집합으로 변환하여 중복 제거
unique_languages = set(survey_responses)

print(f"원본 응답: {survey_responses}")
# 출력: 원본 응답: ['파이썬', '자바', '파이썬', 'C++', '자바', '파이썬', 'Go']

print(f"고유 언어: {unique_languages}")
# 출력: 고유 언어: {'파이썬', '자바', 'C++', 'Go'}

print(f"총 응답 수: {len(survey_responses)}")  # 출력: 총 응답 수: 7
print(f"고유 언어 수: {len(unique_languages)}")  # 출력: 고유 언어 수: 4


# ============================================
# 실습 5: 허용 사용자 목록 (TODO)
# ============================================

# 시스템에 접근 가능한 사용자
allowed_users = {"admin", "user1", "user2", "manager"}

# TODO: "admin"이 allowed_users에 있는지 확인하세요
# 힌트: if "admin" in allowed_users:
if "admin" in allowed_users:
    print("admin: 접근 허용")  # 출력: admin: 접근 허용

# TODO: "guest"가 allowed_users에 있는지 확인하세요
# 없으면 "접근 거부" 출력
if "guest" in allowed_users:
    print("guest: 접근 허용")
else:
    print("guest: 접근 거부")  # 출력: guest: 접근 거부

# TODO: "user1"을 allowed_users에서 제거하세요
# 힌트: allowed_users.remove("user1")
allowed_users.remove("user1")
print(f"제거 후: {allowed_users}")
# 출력: 제거 후: {'admin', 'user2', 'manager'}
