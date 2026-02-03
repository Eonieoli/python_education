# 1_basic.py

"""
Day 3 - 7교시: 리스트 컴프리헨션
Basic (강사 시연용)

학습 목표:
- for문과 리스트 컴프리헨션 비교
- 기본 패턴 이해
- 조건 포함 패턴
- 변환 패턴
- FastAPI 실전 예제
"""

# ============================================
# 1. for문 vs 리스트 컴프리헨션 비교
# ============================================

# for문으로 0~9까지 리스트 만들기
numbers_for = []
for x in range(10):
    numbers_for.append(x)
print("for문:", numbers_for)  # 출력: for문: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 리스트 컴프리헨션으로 동일하게 만들기
numbers_comp = [x for x in range(10)]
print("컴프리헨션:", numbers_comp)  # 출력: 컴프리헨션: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# ============================================
# 2. 조건 포함 패턴 (if)
# ============================================

# for문으로 짝수만 추출
evens_for = []
for x in range(10):
    if x % 2 == 0:
        evens_for.append(x)
print("짝수(for문):", evens_for)  # 출력: 짝수(for문): [0, 2, 4, 6, 8]

# 리스트 컴프리헨션으로 짝수만 추출
evens_comp = [x for x in range(10) if x % 2 == 0]
print("짝수(컴프리헨션):", evens_comp)  # 출력: 짝수(컴프리헨션): [0, 2, 4, 6, 8]


# ============================================
# 3. 변환 패턴
# ============================================

# 0~4의 제곱 리스트
squares = [x**2 for x in range(5)]
print("제곱:", squares)  # 출력: 제곱: [0, 1, 4, 9, 16]

# 1~5를 2배로
doubled = [x * 2 for x in range(1, 6)]
print("2배:", doubled)  # 출력: 2배: [2, 4, 6, 8, 10]


# ============================================
# 4. 문자열 리스트 변환
# ============================================

# 이름 리스트를 대문자로 변환
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print("대문자:", upper_names)  # 출력: 대문자: ['ALICE', 'BOB', 'CHARLIE']

# 이름 길이 리스트
name_lengths = [len(name) for name in names]
print("이름 길이:", name_lengths)  # 출력: 이름 길이: [5, 3, 7]


# ============================================
# 5. 실전: API 응답 변환 (FastAPI 핵심!)
# ============================================

# 사용자 데이터 (API 응답이라고 가정)
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]

# 이름만 추출
names_only = [user["name"] for user in users]
print("이름 목록:", names_only)  # 출력: 이름 목록: ['Alice', 'Bob', 'Charlie']

# 나이만 추출
ages_only = [user["age"] for user in users]
print("나이 목록:", ages_only)  # 출력: 나이 목록: [25, 30, 20]

# 25세 이상만 필터링
adults = [user["age"] for user in users if user["age"] >= 25]
print("25세 이상:", adults)  # 출력: 25세 이상: [25, 30]


# ============================================
# 6. 복합 예제: 상품 데이터 처리
# ============================================

# 상품 리스트
products = [
    {"name": "노트북", "price": 1000000, "stock": 5},
    {"name": "마우스", "price": 30000, "stock": 0},
    {"name": "키보드", "price": 80000, "stock": 10}
]

# 재고가 있는 상품 이름만 추출
available_products = [p["name"] for p in products if p["stock"] > 0]
print("재고 있는 상품:", available_products)  # 출력: 재고 있는 상품: ['노트북', '키보드']

# 10만원 이상 상품의 가격
expensive_prices = [p["price"] for p in products if p["price"] >= 100000]
print("고가 상품 가격:", expensive_prices)  # 출력: 고가 상품 가격: [1000000]
