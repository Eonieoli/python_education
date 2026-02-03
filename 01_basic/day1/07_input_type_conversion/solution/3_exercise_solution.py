# 3_exercise_solution.py

"""
Day 1 - 7교시: 입출력 + 형변환
Exercise - 거스름돈 계산기 (정답)
"""

# ============================================
# 정답 코드
# ============================================

print("=== 거스름돈 계산기 ===")

# 1. 물건 가격 입력받기
price_str = input("물건 가격을 입력하세요: ")
price = int(price_str)

# 2. 받은 금액 입력받기
paid_str = input("받은 금액을 입력하세요: ")
paid = int(paid_str)

# 3. 거스름돈 계산
change = paid - price

# 4. 결과 출력
print(f"거스름돈: {change} 원")
