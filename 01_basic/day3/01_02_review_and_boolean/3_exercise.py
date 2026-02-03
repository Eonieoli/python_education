"""
Day 3 - Boolean과 비교/논리 연산자 Exercise
학생 독립 실습 (TODO만 제공)

실습 목표:
1. 비밀번호 강도 체크 (길이 >= 8)
2. 할인 대상 판단 (나이 or 회원 여부)

"""

# ============================================================
# Exercise 1: 비밀번호 강도 체크
# ============================================================

print("=" * 60)
print("Exercise 1: 비밀번호 강도 체크")
print("=" * 60)

# 비밀번호 강도 기준:
# - 길이가 8자 이상이면 "강함"
# - 그 외는 "약함"

# 케이스 1: 강한 비밀번호
password = "python123"

# TODO: password의 길이가 8 이상인지 확인해서 is_strong에 저장
# 힌트: len(password) >= 8


print(f"비밀번호: {password}")
print(f"강도: {'강함' if is_strong else '약함'}")
# 예상 출력: 강도: 강함


# 케이스 2: 약한 비밀번호
password = "1234"

# TODO: password의 길이가 8 이상인지 확인


print(f"\n비밀번호: {password}")
print(f"강도: {'강함' if is_strong else '약함'}")
# 예상 출력: 강도: 약함


# 케이스 3: 경계값 (정확히 8자)
password = "abcd1234"

# TODO: password의 길이가 8 이상인지 확인


print(f"\n비밀번호: {password}")
print(f"강도: {'강함' if is_strong else '약함'}")
# 예상 출력: 강도: 강함

print()


# ============================================================
# Exercise 2: 할인 대상 판단
# ============================================================

print("=" * 60)
print("Exercise 2: 할인 대상 판단")
print("=" * 60)

# 할인 대상 기준:
# - 회원이거나 (is_member == True)
# - 65세 이상 경로우대 (age >= 65)
# 둘 중 하나라도 해당하면 할인!

# 케이스 1: 회원이지만 젊은 사람
age = 30
is_member = True

# TODO: 할인 대상인지 판단
# 힌트: is_member or (age >= 65)


print(f"나이: {age}, 회원: {is_member}")
print(f"할인 대상? {is_discount}")
# 예상 출력: 할인 대상? True


# 케이스 2: 비회원이지만 경로우대
age = 70
is_member = False

# TODO: 할인 대상인지 판단


print(f"\n나이: {age}, 회원: {is_member}")
print(f"할인 대상? {is_discount}")
# 예상 출력: 할인 대상? True


# 케이스 3: 회원이면서 경로우대 (둘 다 해당)
age = 68
is_member = True

# TODO: 할인 대상인지 판단


print(f"\n나이: {age}, 회원: {is_member}")
print(f"할인 대상? {is_discount}")
# 예상 출력: 할인 대상? True


# 케이스 4: 둘 다 해당 안 됨
age = 40
is_member = False

# TODO: 할인 대상인지 판단


print(f"\n나이: {age}, 회원: {is_member}")
print(f"할인 대상? {is_discount}")
# 예상 출력: 할인 대상? False


# 케이스 5: 경계값 (정확히 65세)
age = 65
is_member = False

# TODO: 할인 대상인지 판단


print(f"\n나이: {age}, 회원: {is_member}")
print(f"할인 대상? {is_discount}")
# 예상 출력: 할인 대상? True

print()


# ============================================================
# 도전 과제: 쇼핑몰 쿠폰 발급 조건
# ============================================================

print("=" * 60)
print("도전 과제: 쿠폰 발급 조건")
print("=" * 60)

# 쿠폰 발급 조건 (모두 만족해야 함):
# 1. 회원이어야 함 (is_member == True)
# 2. 구매 금액이 50000원 이상 (purchase_amount >= 50000)
# 3. 이벤트 기간 중 (is_event_period == True)

# 케이스 1: 모든 조건 만족
is_member = True
purchase_amount = 60000
is_event_period = True

# TODO: 쿠폰 발급 가능 여부 확인
# 힌트: is_member and (purchase_amount >= 50000) and is_event_period


print(f"회원: {is_member}")
print(f"구매 금액: {purchase_amount:,}원")
print(f"이벤트 기간: {is_event_period}")
print(f"쿠폰 발급 가능? {can_issue_coupon}")
# 예상 출력: 쿠폰 발급 가능? True


# 케이스 2: 금액만 부족
is_member = True
purchase_amount = 30000
is_event_period = True

# TODO: 쿠폰 발급 가능 여부 확인


print(f"\n회원: {is_member}")
print(f"구매 금액: {purchase_amount:,}원")
print(f"이벤트 기간: {is_event_period}")
print(f"쿠폰 발급 가능? {can_issue_coupon}")
# 예상 출력: 쿠폰 발급 가능? False


# 케이스 3: 비회원
is_member = False
purchase_amount = 100000
is_event_period = True

# TODO: 쿠폰 발급 가능 여부 확인


print(f"\n회원: {is_member}")
print(f"구매 금액: {purchase_amount:,}원")
print(f"이벤트 기간: {is_event_period}")
print(f"쿠폰 발급 가능? {can_issue_coupon}")
# 예상 출력: 쿠폰 발급 가능? False


# 케이스 4: 이벤트 기간 아님
is_member = True
purchase_amount = 80000
is_event_period = False

# TODO: 쿠폰 발급 가능 여부 확인


print(f"\n회원: {is_member}")
print(f"구매 금액: {purchase_amount:,}원")
print(f"이벤트 기간: {is_event_period}")
print(f"쿠폰 발급 가능? {can_issue_coupon}")
# 예상 출력: 쿠폰 발급 가능? False

print()


print("=" * 60)
print("Exercise 완료!")
print("=" * 60)
print("실습한 내용:")
print("1. 비밀번호 강도 체크 (길이 >= 8)")
print("2. 할인 대상 판단 (회원 or 경로우대)")
print("3. 도전: 쿠폰 발급 조건 (3가지 and)")
print("=" * 60)
