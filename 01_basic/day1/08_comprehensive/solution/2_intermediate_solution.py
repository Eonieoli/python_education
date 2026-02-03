# 2_intermediate_solution.py

"""
Day 1 - 8교시: 종합 실습
🟡 응용 Problem - 쇼핑몰 영수증 (정답)
"""

# ============================================
# 정답 코드
# ============================================

# 1. 상품 정보 입력받기
product_name = input("상품명을 입력하세요: ")
price = input("가격을 입력하세요: ")
quantity = input("수량을 입력하세요: ")

# 2. 가격과 수량을 숫자로 변환
price_num = int(price)
quantity_num = int(quantity)

# 3. 계산하기
subtotal = price_num * quantity_num  # 소계

# 할인 금액 계산 (10% 할인)
discount_rate = 0.1
discount = subtotal * discount_rate  # 할인 금액

# 최종 금액 계산
final_amount = subtotal - discount  # 최종 금액

# 4. 영수증 출력
print("========================================")
print("           쇼핑몰 영수증")
print("========================================")
print(f"상품명: {product_name}")
print(f"단가: {price_num}원")
print(f"수량: {quantity_num}개")
print(f"소계: {subtotal}원")
print(f"할인 (10%): -{discount:.0f}원")
print("========================================")
print(f"최종 결제 금액: {final_amount:.0f}원")
print("========================================")
