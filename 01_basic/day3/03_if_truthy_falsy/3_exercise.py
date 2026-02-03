# 3_exercise.py

"""
Day 3 - 3교시: 조건문 (if) + Truthy/Falsy
Exercise - 할인율 계산 및 안전한 데이터 접근

문제 1: 할인율 계산
회원 등급과 구매 금액에 따라 다른 할인율을 적용하는 프로그램을 작성하세요.

할인 규칙:
- VIP 회원: 20% 할인
- 일반 회원: 10% 할인
- 비회원: 할인 없음
- 추가: 구매 금액이 50000원 이상이면 5% 추가 할인

출력 예시:
원가: 60000원
할인율: 25%
최종 금액: 45000원
"""

# ============================================
# 문제 1: 할인율 계산
# ============================================

# 주어진 데이터
member_grade = "VIP"  # "VIP", "일반", "비회원"
purchase_amount = 60000

# TODO: 회원 등급에 따라 기본 할인율을 정하세요
# 힌트: if/elif/else 사용
if member_grade == "VIP":
    discount_rate =   # VIP는 0.2 (20%)
elif member_grade == "일반":
    discount_rate =   # 일반은 0.1 (10%)
else:
    discount_rate =   # 비회원은 0 (할인 없음)

# TODO: 구매 금액이 50000원 이상이면 5% 추가 할인
# 힌트: if 조건문 사용, discount_rate에 0.05 더하기
if purchase_amount >= 50000:
    discount_rate +=   # 0.05 추가

# TODO: 최종 금액을 계산하세요
# 힌트: 최종 금액 = 원가 × (1 - 할인율)
final_amount =

# 결과 출력
print(f"원가: {purchase_amount}원")
print(f"할인율: {int(discount_rate * 100)}%")
print(f"최종 금액: {int(final_amount)}원")


print("\n" + "="*50 + "\n")


"""
문제 2: 안전한 데이터 접근
사용자 정보 딕셔너리에서 안전하게 데이터를 가져오는 프로그램을 작성하세요.
Truthy/Falsy를 활용하여 빈 딕셔너리나 없는 키를 처리하세요.

출력 예시:
이름: 김철수
이메일: 정보 없음
전화번호: 010-1234-5678
"""

# ============================================
# 문제 2: 안전한 데이터 접근
# ============================================

# 사용자 정보 (이메일이 없음)
user_data = {
    "name": "김철수",
    "phone": "010-1234-5678"
}

# TODO: user_data가 비어있는지 먼저 확인하세요
# 힌트: if user_data: 형태로 Truthy/Falsy 활용
if user_data:
    # TODO: 이름을 출력하세요
    # 힌트: user_data["name"]
    print(f"이름: {  }")
    
    # TODO: 이메일이 있는지 확인하고 출력하세요
    # 힌트: if "email" in user_data: 사용
    if   :
        print(f"이메일: {user_data['email']}")
    else:
        print("이메일: 정보 없음")
    
    # TODO: 전화번호를 출력하세요
    print(f"전화번호: {  }")
    
else:
    print("사용자 정보가 없습니다")
