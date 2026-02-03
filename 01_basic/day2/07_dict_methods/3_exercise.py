# 3_exercise.py

"""
Day 2 - 7교시: 딕셔너리 메서드
Exercise - 상품 재고 관리 시스템

문제:
온라인 쇼핑몰의 상품 재고 관리 시스템을 만드세요.

요구사항:
1. 초기 재고 딕셔너리에 새 상품 정보를 병합하세요
2. 판매된 상품을 재고에서 제거하고 판매 수량을 기록하세요
3. in 연산자로 특정 상품들의 재고 존재 여부를 확인하세요
4. get() 메서드로 재고 수량을 안전하게 조회하세요 (없으면 0)

출력 예시:
병합 후 재고: {'노트북': 10, '마우스': 25, '키보드': 15, '모니터': 8, '헤드셋': 12}
판매된 마우스: 25개
남은 재고: {'노트북': 10, '키보드': 15, '모니터': 8, '헤드셋': 12}
노트북 있음: True
노트북 재고: 10개
태블릿 있음: False
태블릿 재고: 0개
"""

# ============================================
# 주어진 데이터
# ============================================

# 초기 재고
inventory = {
    "노트북": 10,
    "마우스": 25,
    "키보드": 15
}

# 새로 입고된 상품
new_stock = {
    "모니터": 8,
    "헤드셋": 12
}

# 판매 정보
sold_item = "마우스"

# 조회할 상품들
check_items = ["노트북", "태블릿"]


# ============================================
# TODO: 여기서부터 코드를 작성하세요
# ============================================

# 1. update()를 사용하여 new_stock을 inventory에 병합하세요


# 병합 후 재고 출력
print("병합 후 재고:", inventory)


# 2. pop()을 사용하여 sold_item(마우스)을 재고에서 제거하고
#    판매 수량을 sold_count 변수에 저장하세요


# 판매 정보 출력
print(f"판매된 {sold_item}: {sold_count}개")
print("남은 재고:", inventory)


# 3. check_items의 각 상품에 대해 in 연산자와 get() 사용:

# 노트북 확인
item1 = check_items[0]  # "노트북"

# TODO: in 연산자로 item1이 재고에 있는지 확인 (True/False)
# 힌트: has_item1 = item1 in inventory


print(f"{item1} 있음: {has_item1}")

# TODO: get()으로 item1의 재고 수량 가져오기 (없으면 0)
# 힌트: count1 = inventory.get(item1, 0)


print(f"{item1} 재고: {count1}개")


# 태블릿 확인
item2 = check_items[1]  # "태블릿"

# TODO: in 연산자로 item2가 재고에 있는지 확인 (True/False)
# 힌트: has_item2 = item2 in inventory


print(f"{item2} 있음: {has_item2}")

# TODO: get()으로 item2의 재고 수량 가져오기 (없으면 0)
# 힌트: count2 = inventory.get(item2, 0)


print(f"{item2} 재고: {count2}개")

