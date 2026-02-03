# 3_exercise_solution.py

"""
Day 2 - 7교시: 딕셔너리 메서드
Exercise - 상품 재고 관리 시스템 (정답)
"""

# ============================================
# 주어진 데이터
# ============================================

inventory = {
    "노트북": 10,
    "마우스": 25,
    "키보드": 15
}

new_stock = {
    "모니터": 8,
    "헤드셋": 12
}

sold_item = "마우스"
check_items = ["노트북", "태블릿"]


# ============================================
# 정답 코드
# ============================================

# 1. update()로 새 상품 병합
inventory.update(new_stock)

print("병합 후 재고:", inventory)
# 출력: 병합 후 재고: {'노트북': 10, '마우스': 25, '키보드': 15, '모니터': 8, '헤드셋': 12}


# 2. pop()으로 판매된 상품 제거
sold_count = inventory.pop(sold_item)

print(f"판매된 {sold_item}: {sold_count}개")
# 출력: 판매된 마우스: 25개
print("남은 재고:", inventory)
# 출력: 남은 재고: {'노트북': 10, '키보드': 15, '모니터': 8, '헤드셋': 12}


# 3. 상품 재고 확인 (in 연산자 + get())

# 노트북 확인
item1 = check_items[0]  # "노트북"
has_item1 = item1 in inventory  # True
count1 = inventory.get(item1, 0)  # 10

print(f"{item1} 있음: {has_item1}")
# 출력: 노트북 있음: True
print(f"{item1} 재고: {count1}개")
# 출력: 노트북 재고: 10개

# 태블릿 확인
item2 = check_items[1]  # "태블릿"
has_item2 = item2 in inventory  # False
count2 = inventory.get(item2, 0)  # 0 (없으므로 기본값)

print(f"{item2} 있음: {has_item2}")
# 출력: 태블릿 있음: False
print(f"{item2} 재고: {count2}개")
# 출력: 태블릿 재고: 0개
