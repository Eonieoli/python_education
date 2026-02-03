# 3_exercise_solution.py

"""
Day 3 - 7교시: 리스트 컴프리헨션
Exercise - 상품 데이터 처리 (정답)
"""

# ============================================
# 주어진 데이터
# ============================================

products = [
    {"name": "노트북", "price": 1200000, "stock": 5},
    {"name": "마우스", "price": 30000, "stock": 15},
    {"name": "키보드", "price": 80000, "stock": 0},
    {"name": "모니터", "price": 350000, "stock": 20},
    {"name": "웹캠", "price": 40000, "stock": 12},
    {"name": "헤드셋", "price": 50000, "stock": 8}
]


# ============================================
# 정답 코드
# ============================================

# 1. 재고가 10개 이상인 상품의 이름 추출
sufficient_stock = [p["name"] for p in products if p["stock"] >= 10]

# 2. 50000원 이하인 상품의 가격을 10% 할인
discount_prices = [p["price"] * 0.9 for p in products if p["price"] <= 50000]

# 3. 할인 대상 상품의 딕셔너리 리스트
discount_products = [
    {"name": p["name"], "discounted_price": p["price"] * 0.9} 
    for p in products 
    if p["price"] <= 50000
]

# 결과 출력
print("재고 충분한 상품:", sufficient_stock)
# 출력: 재고 충분한 상품: ['마우스', '모니터', '웹캠']

print("할인 가격:", discount_prices)
# 출력: 할인 가격: [27000.0, 36000.0, 45000.0]

print("할인 상품 정보:", discount_products)
# 출력: 할인 상품 정보: [
#   {'name': '마우스', 'discounted_price': 27000.0}, 
#   {'name': '웹캠', 'discounted_price': 36000.0}, 
#   {'name': '헤드셋', 'discounted_price': 45000.0}
# ]
