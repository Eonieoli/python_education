# 3_exercise_solution.py

"""
Day 2 - 5교시: 튜플 + 집합
Exercise - 좌표 계산 및 중복 제거 (정답)
"""

# ============================================
# Exercise 1: 좌표 계산하기 (정답)
# ============================================

# 주어진 데이터
point1 = (0, 0)
point2 = (3, 4)

# 1. 각 점 언패킹
x1, y1 = point1
x2, y2 = point2

# 점 출력
print(f"점 1: {point1}")
print(f"점 2: {point2}")

# 2. 좌표 차이 계산
x_diff = x2 - x1  # 3 - 0 = 3
y_diff = y2 - y1  # 4 - 0 = 4

# 3. 거리 계산
# 거리 = √((x2-x1)² + (y2-y1)²)
distance = ((x_diff ** 2) + (y_diff ** 2)) ** 0.5  # √(9 + 16) = √25 = 5.0

# 결과 출력
print(f"x 차이: {x_diff}")  # 출력: x 차이: 3
print(f"y 차이: {y_diff}")  # 출력: y 차이: 4
print(f"거리: {distance}")  # 출력: 거리: 5.0


# ============================================
# Exercise 2: 중복 방문자 제거 (정답)
# ============================================

# 주어진 데이터
visitors = ["user1", "user2", "user1", "user3", "user2", "admin", "user1"]

# 전체 방문 출력
print(f"전체 방문: {len(visitors)} 회")  # 출력: 전체 방문: 7 회

# 1. 집합으로 변환하여 중복 제거
unique_visitors = set(visitors)

# 2. 고유 방문자 출력
print(f"고유 방문자: {unique_visitors}")
# 출력: 고유 방문자: {'user1', 'user2', 'user3', 'admin'}

# 3. 고유 방문자 수 출력
print(f"고유 방문자 수: {len(unique_visitors)} 명")
# 출력: 고유 방문자 수: 4 명

# 4. "admin" 방문 확인
admin_visited = "admin" in unique_visitors  # True

# 5. "guest" 방문 확인
guest_visited = "guest" in unique_visitors  # False

# 결과 출력
print(f"admin 방문: {admin_visited}")  # 출력: admin 방문: True
print(f"guest 방문: {guest_visited}")  # 출력: guest 방문: False
