"""
Day 3 - Boolean과 비교/논리 연산자 Exercise 해답
학생 독립 실습 정답

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

# 해답: len()으로 길이를 구하고 8과 비교
is_strong = len(password) >= 8

print(f"비밀번호: {password}")
print(f"비밀번호 길이: {len(password)}자")
print(f"강도: {'강함' if is_strong else '약함'}")  # 강도: 강함


# 케이스 2: 약한 비밀번호
password = "1234"

is_strong = len(password) >= 8

print(f"\n비밀번호: {password}")
print(f"비밀번호 길이: {len(password)}자")
print(f"강도: {'강함' if is_strong else '약함'}")  # 강도: 약함


# 케이스 3: 경계값 (정확히 8자)
password = "abcd1234"

is_strong = len(password) >= 8

print(f"\n비밀번호: {password}")
print(f"비밀번호 길이: {len(password)}자")
print(f"강도: {'강함' if is_strong else '약함'}")  # 강도: 강함

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

# 해답: or 연산자 사용 (하나라도 True면 할인)
is_discount = is_member or (age >= 65)

print(f"나이: {age}, 회원: {is_member}")
print(f"할인 대상? {is_discount}")  # True (회원이므로)


# 케이스 2: 비회원이지만 경로우대
age = 70
is_member = False

is_discount = is_member or (age >= 65)

print(f"\n나이: {age}, 회원: {is_member}")
print(f"할인 대상? {is_discount}")  # True (경로우대)


# 케이스 3: 회원이면서 경로우대 (둘 다 해당)
age = 68
is_member = True

is_discount = is_member or (age >= 65)

print(f"\n나이: {age}, 회원: {is_member}")
print(f"할인 대상? {is_discount}")  # True (둘 다!)


# 케이스 4: 둘 다 해당 안 됨
age = 40
is_member = False

is_discount = is_member or (age >= 65)

print(f"\n나이: {age}, 회원: {is_member}")
print(f"할인 대상? {is_discount}")  # False


# 케이스 5: 경계값 (정확히 65세)
age = 65
is_member = False

is_discount = is_member or (age >= 65)

print(f"\n나이: {age}, 회원: {is_member}")
print(f"할인 대상? {is_discount}")  # True (>= 이므로 65세도 포함)

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

# 해답: and 연산자로 모든 조건 연결 (모두 True여야 함)
can_issue_coupon = is_member and (purchase_amount >= 50000) and is_event_period

print(f"회원: {is_member}")
print(f"구매 금액: {purchase_amount:,}원")
print(f"이벤트 기간: {is_event_period}")
print(f"쿠폰 발급 가능? {can_issue_coupon}")  # True


# 케이스 2: 금액만 부족
is_member = True
purchase_amount = 30000
is_event_period = True

can_issue_coupon = is_member and (purchase_amount >= 50000) and is_event_period

print(f"\n회원: {is_member}")
print(f"구매 금액: {purchase_amount:,}원")
print(f"이벤트 기간: {is_event_period}")
print(f"쿠폰 발급 가능? {can_issue_coupon}")  # False (금액 부족)


# 케이스 3: 비회원
is_member = False
purchase_amount = 100000
is_event_period = True

can_issue_coupon = is_member and (purchase_amount >= 50000) and is_event_period

print(f"\n회원: {is_member}")
print(f"구매 금액: {purchase_amount:,}원")
print(f"이벤트 기간: {is_event_period}")
print(f"쿠폰 발급 가능? {can_issue_coupon}")  # False (비회원)


# 케이스 4: 이벤트 기간 아님
is_member = True
purchase_amount = 80000
is_event_period = False

can_issue_coupon = is_member and (purchase_amount >= 50000) and is_event_period

print(f"\n회원: {is_member}")
print(f"구매 금액: {purchase_amount:,}원")
print(f"이벤트 기간: {is_event_period}")
print(f"쿠폰 발급 가능? {can_issue_coupon}")  # False (이벤트 기간 아님)

print()


# ============================================================
# 심화: 단계별 디버깅 (어떤 조건이 False인지 확인)
# ============================================================

print("=" * 60)
print("심화: 단계별 디버깅")
print("=" * 60)

is_member = False
purchase_amount = 30000
is_event_period = True

# 각 조건을 개별적으로 확인
print(f"회원: {is_member}")
print(f"구매 금액: {purchase_amount:,}원")
print(f"이벤트 기간: {is_event_period}")

print(f"\n[조건별 체크]")
print(f"1. 회원인가? {is_member}")  # False
print(f"2. 금액 충족? {purchase_amount >= 50000}")  # False
print(f"3. 이벤트 기간? {is_event_period}")  # True

# 최종 판단
can_issue_coupon = is_member and (purchase_amount >= 50000) and is_event_period
print(f"\n최종 쿠폰 발급 가능? {can_issue_coupon}")  # False
print("→ 회원도 아니고, 금액도 부족!")


print("\n" + "=" * 60)
print("Exercise 완료!")
print("=" * 60)
print("핵심 요약:")
print("1. len() >= 8: 비밀번호 강도 체크")
print("2. or 연산자: 하나라도 True면 할인")
print("3. and 연산자: 모두 True여야 쿠폰 발급")
print("4. 복잡한 조건은 단계별로 나눠서 디버깅!")
print("=" * 60)
