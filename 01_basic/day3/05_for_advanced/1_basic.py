# 1_basic.py

"""
Day 3 - 5교시: for문 심화
Basic (강사 시연용)

학습 목표:
- enumerate()로 인덱스와 값을 함께 사용하기
- items()로 딕셔너리 순회하기
- break와 continue로 반복 제어하기
- 중첩 for문 이해하기
"""

# ============================================
# 1. enumerate() - 인덱스와 값 함께 사용
# ============================================

# 일반적인 for문: 값만 가져옴
fruits = ["사과", "바나나", "딸기"]
for fruit in fruits:
    print(fruit)
# 출력:
# 사과
# 바나나
# 딸기

print()  # 빈 줄

# enumerate()를 사용하면 인덱스와 값을 함께 가져올 수 있습니다
for index, fruit in enumerate(fruits):
    print(f"{index}번: {fruit}")
# 출력:
# 0번: 사과
# 1번: 바나나
# 2번: 딸기

print()

# 실전 예제: 순위 출력 (1부터 시작)
students = ["김철수", "이영희", "박민수"]
for rank, name in enumerate(students, start=1):
    print(f"{rank}등: {name}")
# 출력:
# 1등: 김철수
# 2등: 이영희
# 3등: 박민수


# ============================================
# 2. items() - 딕셔너리 순회
# ============================================

# 딕셔너리의 키와 값을 함께 가져오기
user = {
    "name": "홍길동",
    "age": 25,
    "city": "서울"
}

# items()를 사용하면 키와 값을 동시에 가져올 수 있습니다
for key, value in user.items():
    print(f"{key}: {value}")
# 출력:
# name: 홍길동
# age: 25
# city: 서울

print()

# 실전 예제: 상품 재고 확인
inventory = {
    "노트북": 5,
    "마우스": 20,
    "키보드": 15
}

for product, quantity in inventory.items():
    print(f"{product}: {quantity}개")
# 출력:
# 노트북: 5개
# 마우스: 20개
# 키보드: 15개


# ============================================
# 3. break와 continue - 반복 제어
# ============================================

# break: 반복문을 즉시 종료
print("\n=== break 예제 ===")
for i in range(1, 11):
    if i == 5:
        print("5를 찾았습니다! 반복 종료")
        break
    print(i)
# 출력: 1 2 3 4 5를 찾았습니다! 반복 종료

print()

# continue: 현재 반복을 건너뛰고 다음 반복으로
print("=== continue 예제 ===")
for i in range(1, 6):
    if i == 3:
        continue  # 3일 때는 출력하지 않고 다음으로
    print(i)
# 출력: 1 2 4 5 (3은 건너뜀)

print()

# 실전 예제: 짝수만 출력
print("=== 짝수만 출력 ===")
for num in range(1, 11):
    if num % 2 != 0:  # 홀수면
        continue  # 건너뛰기
    print(num)
# 출력: 2 4 6 8 10


# ============================================
# 4. 중첩 for문 - 반복문 안의 반복문
# ============================================

# 기본 중첩 for문
print("\n=== 중첩 for문 기본 ===")
for i in range(1, 4):  # 외부 반복
    for j in range(1, 3):  # 내부 반복
        print(f"i={i}, j={j}")
# 출력:
# i=1, j=1
# i=1, j=2
# i=2, j=1
# i=2, j=2
# i=3, j=1
# i=3, j=2

print()

# 실전 예제: 구구단 2단
print("=== 2단 구구단 ===")
for i in range(1, 10):
    result = 2 * i
    print(f"2 × {i} = {result}")

print()

# 실전 예제: 좌석 배치도 (간단히)
print("=== 좌석 배치도 ===")
rows = ["A", "B", "C"]
for row in rows:
    for seat_num in range(1, 4):
        print(f"{row}{seat_num}", end=" ")  # 한 줄에 출력
    print()  # 행이 끝나면 줄바꿈
# 출력:
# A1 A2 A3
# B1 B2 B3
# C1 C2 C3
