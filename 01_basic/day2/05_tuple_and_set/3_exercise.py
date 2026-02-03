# 3_exercise.py

"""
Day 2 - 5교시: 튜플 + 집합
Exercise - 좌표 계산 및 중복 제거

학습 목표:
- 튜플 언패킹으로 여러 값 처리
- 집합으로 중복 데이터 정리
"""

# ============================================
# Exercise 1: 좌표 계산하기
# ============================================

"""
문제:
두 점 사이의 거리를 계산하는 프로그램을 작성하세요.

주어진 데이터:
- point1: (0, 0)
- point2: (3, 4)

요구사항:
1. 각 점을 언패킹하여 x, y 좌표를 추출하세요
2. x 좌표 차이와 y 좌표 차이를 계산하세요
3. 거리는 다음 공식으로 계산하세요:
   거리 = ((x2 - x1)² + (y2 - y1)²)의 제곱근
   (제곱근은 ** 0.5를 사용)

출력 예시:
점 1: (0, 0)
점 2: (3, 4)
x 차이: 3
y 차이: 4
거리: 5.0
"""

# 주어진 데이터
point1 = (0, 0)
point2 = (3, 4)

# TODO: point1을 언패킹하여 x1, y1에 할당하세요


# TODO: point2를 언패킹하여 x2, y2에 할당하세요


# 점 출력
print(f"점 1: {point1}")
print(f"점 2: {point2}")

# TODO: x 좌표 차이를 계산하세요
# 힌트: x_diff = x2 - x1


# TODO: y 좌표 차이를 계산하세요


# TODO: 거리를 계산하세요
# 힌트: distance = ((x_diff ** 2) + (y_diff ** 2)) ** 0.5


# 결과 출력
print(f"x 차이: {x_diff}")
print(f"y 차이: {y_diff}")
print(f"거리: {distance}")


# ============================================
# Exercise 2: 중복 방문자 제거
# ============================================

"""
문제:
웹사이트 방문 로그에서 중복 방문자를 제거하고,
특정 사용자가 방문했는지 확인하는 프로그램을 작성하세요.

주어진 데이터:
- visitors: ["user1", "user2", "user1", "user3", "user2", "admin", "user1"]

요구사항:
1. 집합으로 변환하여 중복 제거하세요
2. "admin"이 방문했는지 확인하세요
3. "guest"가 방문했는지 확인하세요
4. 고유 방문자 수를 출력하세요

출력 예시:
전체 방문: 7 회
고유 방문자: {'user1', 'user2', 'user3', 'admin'}
고유 방문자 수: 4 명
admin 방문: True
guest 방문: False
"""

# 주어진 데이터
visitors = ["user1", "user2", "user1", "user3", "user2", "admin", "user1"]

# 전체 방문 출력
print(f"전체 방문: {len(visitors)} 회")

# TODO: 집합으로 변환하여 중복 제거하세요
# 힌트: unique_visitors = set(visitors)


# TODO: 고유 방문자를 출력하세요
print(f"고유 방문자: {unique_visitors}")

# TODO: 고유 방문자 수를 출력하세요
# 힌트: len(unique_visitors)
print(f"고유 방문자 수: {len(unique_visitors)} 명")

# TODO: "admin"이 고유 방문자에 있는지 확인하세요
# 힌트: "admin" in unique_visitors


# TODO: "guest"가 고유 방문자에 있는지 확인하세요


# 결과 출력
print(f"admin 방문: {admin_visited}")
print(f"guest 방문: {guest_visited}")
