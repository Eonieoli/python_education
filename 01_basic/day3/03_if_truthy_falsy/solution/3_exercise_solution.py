# 3_exercise_solution.py

"""
Day 3 - 3교시: 조건문 (if) + Truthy/Falsy
Exercise - 할인율 계산 및 안전한 데이터 접근 (정답)
"""

# ============================================
# 문제 1: 할인율 계산 (정답)
# ============================================

# 주어진 데이터
member_grade = "VIP"
purchase_amount = 60000

# 회원 등급에 따른 기본 할인율
if member_grade == "VIP":
    discount_rate = 0.2  # 20%
elif member_grade == "일반":
    discount_rate = 0.1  # 10%
else:
    discount_rate = 0  # 할인 없음

# 구매 금액에 따른 추가 할인
if purchase_amount >= 50000:
    discount_rate += 0.05  # 5% 추가

# 최종 금액 계산
final_amount = purchase_amount * (1 - discount_rate)

# 결과 출력
print(f"원가: {purchase_amount}원")
print(f"할인율: {int(discount_rate * 100)}%")
print(f"최종 금액: {int(final_amount)}원")
# 출력:
# 원가: 60000원
# 할인율: 25%
# 최종 금액: 45000원


print("\n" + "="*50 + "\n")


# ============================================
# 문제 2: 안전한 데이터 접근 (정답)
# ============================================

# 사용자 정보
user_data = {
    "name": "김철수",
    "phone": "010-1234-5678"
}

# 딕셔너리가 비어있지 않은지 확인
if user_data:
    # 이름 출력
    print(f"이름: {user_data['name']}")
    
    # 이메일이 있는지 확인
    if "email" in user_data:
        print(f"이메일: {user_data['email']}")
    else:
        print("이메일: 정보 없음")
    
    # 전화번호 출력
    print(f"전화번호: {user_data['phone']}")
else:
    print("사용자 정보가 없습니다")

# 출력:
# 이름: 김철수
# 이메일: 정보 없음
# 전화번호: 010-1234-5678
