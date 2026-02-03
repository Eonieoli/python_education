# 2_practice.py

"""
Day 3 - 5교시: for문 심화
Practice (강사와 함께 실습)

학습 목표:
- enumerate()로 순위 매기기
- items()로 딕셔너리 데이터 처리
- 중첩 for문으로 구구단 만들기
"""

# ============================================
# 실습 1: enumerate() 활용 - 성적 순위표 (전체 타이핑)
# ============================================

# 학생별 점수 (높은 순으로 정렬되어 있음)
scores = [95, 87, 82, 79, 75]

# enumerate()로 순위와 점수를 함께 출력
for rank, score in enumerate(scores, start=1):
    print(f"{rank}등: {score}점")
# 출력:
# 1등: 95점
# 2등: 87점
# 3등: 82점
# 4등: 79점
# 5등: 75점


# ============================================
# 실습 2: items() 활용 - 상품 정보 출력 (TODO)
# ============================================

# 상품 딕셔너리
product = {
    "name": "무선 이어폰",
    "price": 89000,
    "brand": "Apple",
    "color": "화이트"
}

# TODO: items()를 사용하여 key와 value를 출력하세요
# 힌트: for key, value in product.items():
print("\n=== 상품 정보 ===")
for key, value in product.items():
    print(f"{key}: {value}")


# ============================================
# 실습 3: 딕셔너리 리스트 순회 (TODO)
# ============================================

# 여러 사용자의 정보
users = [
    {"name": "김철수", "age": 25},
    {"name": "이영희", "age": 30},
    {"name": "박민수", "age": 28}
]

# TODO: enumerate()와 items()를 함께 사용하여 출력하세요
# 힌트: enumerate(users, start=1)로 순번 추가
print("\n=== 사용자 목록 ===")
for num, user in enumerate(users, start=1):
    print(f"{num}번 사용자:")
    for key, value in user.items():
        print(f"  {key}: {value}")


# ============================================
# 실습 4: 중첩 for문 - 구구단 (TODO)
# ============================================

# TODO: 중첩 for문으로 2단부터 5단까지 출력하세요
# 힌트: 외부 for문은 range(2, 6), 내부 for문은 range(1, 10)
print("\n=== 구구단 2단 ~ 5단 ===")
for dan in range(2, 6):
    print(f"\n[{dan}단]")
    for i in range(1, 10):
        result = dan * i
        print(f"{dan} × {i} = {result}")


# ============================================
# 실습 5: break와 continue 활용 (TODO)
# ============================================

# 재고 목록
stock = {
    "사과": 0,
    "바나나": 5,
    "딸기": 0,
    "포도": 10,
    "수박": 3
}

# TODO: 재고가 있는 상품만 출력하세요 (재고 0인 상품은 건너뛰기)
# 힌트: if quantity == 0: continue
print("\n=== 재고가 있는 상품 ===")
for product, quantity in stock.items():
    if quantity == 0:
        continue
    print(f"{product}: {quantity}개")
# 출력:
# 바나나: 5개
# 포도: 10개
# 수박: 3개
