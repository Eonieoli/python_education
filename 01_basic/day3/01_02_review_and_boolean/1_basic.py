"""
Day 3 - Boolean과 비교/논리 연산자 완전 정복
1교시 개념 + 2교시 실습 통합

학습 목표:
1. Boolean 타입의 개념과 필요성 이해
2. 비교 연산자를 사용한 조건 판단
3. 논리 연산자로 복잡한 조건 표현
4. 실생활 시나리오에 적용하기

"""

# ============================================================
# 1교시: Boolean 개념 (PPT 설명 후 코드로 확인)
# ============================================================

print("=" * 60)
print("1. Boolean 타입이란?")
print("=" * 60)

# Boolean은 True 또는 False 두 가지 값만 가지는 타입
# 조건을 판단하고 프로그램의 흐름을 제어하는 데 사용

is_logged_in = True   # 로그인 됨
is_adult = False      # 미성년자

print(f"로그인 상태: {is_logged_in}")  # True
print(f"성인 여부: {is_adult}")        # False
print(f"type(is_logged_in) = {type(is_logged_in)}")  # <class 'bool'>

print("\n왜 Boolean이 필요한가?")
print("→ 프로그램이 '예/아니오' 질문에 답하고 분기하기 위해")
print("→ 실생활 예시:")
print("  - 로그인 검증: 아이디와 비밀번호가 맞는가?")
print("  - 나이 확인: 성인인가?")
print("  - 재고 확인: 상품이 있는가?")
print("  - 할인 대상: 조건을 만족하는가?")

print()


# ============================================================
# 2. 비교 연산자 - 두 값을 비교해서 Boolean 반환
# ============================================================

print("=" * 60)
print("2. 비교 연산자")
print("=" * 60)

# 숫자 비교
age = 25
print(f"\n나이: {age}")
print(f"age == 25: {age == 25}")  # True (같음)
print(f"age != 20: {age != 20}")  # True (다름)
print(f"age > 20: {age > 20}")    # True (큼)
print(f"age < 30: {age < 30}")    # True (작음)
print(f"age >= 25: {age >= 25}")  # True (크거나 같음)
print(f"age <= 20: {age <= 20}")  # False (작거나 같음)

# 문자열 비교
username = "admin"
print(f"\n아이디: {username}")
print(f'username == "admin": {username == "admin"}')    # True
print(f'username == "user": {username == "user"}')      # False
print(f'username != "guest": {username != "guest"}')    # True

# 문자열은 사전순(알파벳순)으로 비교됨
print(f"\n문자열 크기 비교:")
print(f'"apple" < "banana": {"apple" < "banana"}')  # True
print(f'"zebra" > "apple": {"zebra" > "apple"}')    # True

print()


# ============================================================
# 3. 논리 연산자 - Boolean 값들을 조합
# ============================================================

print("=" * 60)
print("3. 논리 연산자")
print("=" * 60)

# and: 둘 다 True여야 True
print("\n[ and 연산자 - 둘 다 참이어야 참 ]")
has_id = True
has_password = True
print(f"아이디 있음: {has_id}, 비밀번호 있음: {has_password}")
print(f"로그인 가능: {has_id and has_password}")  # True

has_id = True
has_password = False
print(f"\n아이디 있음: {has_id}, 비밀번호 있음: {has_password}")
print(f"로그인 가능: {has_id and has_password}")  # False

# or: 하나라도 True면 True
print("\n[ or 연산자 - 하나라도 참이면 참 ]")
is_member = False
is_senior = True
print(f"회원: {is_member}, 경로우대: {is_senior}")
print(f"할인 대상: {is_member or is_senior}")  # True

is_member = False
is_senior = False
print(f"\n회원: {is_member}, 경로우대: {is_senior}")
print(f"할인 대상: {is_member or is_senior}")  # False

# not: 반대로 뒤집기
print("\n[ not 연산자 - 반대로 ]")
is_available = True
print(f"재고 있음: {is_available}")
print(f"재고 없음: {not is_available}")  # False

is_available = False
print(f"\n재고 있음: {is_available}")
print(f"재고 없음: {not is_available}")  # True

print()


# ============================================================
# *** 1교시와 2교시 경계선 ***
# 위: 1교시 개념 설명 (PPT + 간단한 코드 확인)
# 아래: 2교시 실전 코드 (Basic 심화)
# ============================================================


print("=" * 60)
print("4. 실전 패턴 - 복잡한 조건 조합")
print("=" * 60)

# 패턴 1: 성인 검증
age = 25
print(f"\n나이: {age}")
is_adult = age >= 19
print(f"성인인가? {is_adult}")  # True

age = 17
print(f"\n나이: {age}")
is_adult = age >= 19
print(f"성인인가? {is_adult}")  # False


# 패턴 2: 로그인 검증 (아이디 AND 비밀번호)
input_id = "admin"
input_pw = "1234"
correct_id = "admin"
correct_pw = "1234"

print(f"\n입력 아이디: {input_id}, 입력 비밀번호: {input_pw}")
print(f"저장된 아이디: {correct_id}, 저장된 비밀번호: {correct_pw}")

# 둘 다 맞아야 로그인 성공
login_success = (input_id == correct_id) and (input_pw == correct_pw)
print(f"로그인 성공? {login_success}")  # True

# 아이디만 틀린 경우
input_id = "user"
login_success = (input_id == correct_id) and (input_pw == correct_pw)
print(f"\n아이디 틀림 → 로그인 성공? {login_success}")  # False


# 패턴 3: 범위 체크 (점수가 0~100 사이인가?)
score = 85
print(f"\n점수: {score}")
is_valid = (score >= 0) and (score <= 100)
print(f"유효한 점수? {is_valid}")  # True

# 더 간단한 표현 (Python 특징!)
is_valid = 0 <= score <= 100
print(f"유효한 점수? (간단 표현) {is_valid}")  # True

score = 150
print(f"\n점수: {score}")
is_valid = 0 <= score <= 100
print(f"유효한 점수? {is_valid}")  # False


# 패턴 4: 할인 대상 (회원 OR 경로우대)
is_member = False
age = 70

print(f"\n회원: {is_member}, 나이: {age}")
is_discount = is_member or (age >= 65)
print(f"할인 대상? {is_discount}")  # True (경로우대)

is_member = True
age = 30
print(f"\n회원: {is_member}, 나이: {age}")
is_discount = is_member or (age >= 65)
print(f"할인 대상? {is_discount}")  # True (회원)

is_member = False
age = 30
print(f"\n회원: {is_member}, 나이: {age}")
is_discount = is_member or (age >= 65)
print(f"할인 대상? {is_discount}")  # False


# 패턴 5: 복잡한 조건 조합 (and + or + not)
# 조건: (회원이거나 VIP이고) AND (재고가 있고) AND (판매중지가 아님)
is_member = True
is_vip = False
stock = 10
is_discontinued = False

print(f"\n회원: {is_member}, VIP: {is_vip}, 재고: {stock}, 판매중지: {is_discontinued}")

# 단계별로 계산
can_access = is_member or is_vip
has_stock = stock > 0
is_available = not is_discontinued

print(f"접근 가능: {can_access}")        # True
print(f"재고 있음: {has_stock}")         # True
print(f"판매 가능: {is_available}")      # True

can_purchase = can_access and has_stock and is_available
print(f"구매 가능? {can_purchase}")  # True

# 한 줄로도 가능 (가독성은 떨어짐)
can_purchase = (is_member or is_vip) and (stock > 0) and (not is_discontinued)
print(f"구매 가능? (한 줄) {can_purchase}")  # True


print("\n" + "=" * 60)
print("5. 실생활 시나리오 종합")
print("=" * 60)

# 시나리오: 영화 티켓 구매 가능 여부
age = 17
has_money = True
is_rated_adult = True  # 청소년 관람불가

print(f"\n나이: {age}, 돈 있음: {has_money}, 청불: {is_rated_adult}")

# 조건 1: 성인 영화면 19세 이상이어야 함
age_check = (not is_rated_adult) or (age >= 19)
print(f"나이 조건 통과? {age_check}")  # False (17세라서)

# 조건 2: 돈이 있어야 함
money_check = has_money
print(f"돈 조건 통과? {money_check}")  # True

# 최종 구매 가능 여부
can_buy = age_check and money_check
print(f"티켓 구매 가능? {can_buy}")  # False


# 성인으로 변경
age = 20
print(f"\n나이: {age}로 변경")
age_check = (not is_rated_adult) or (age >= 19)
can_buy = age_check and money_check
print(f"티켓 구매 가능? {can_buy}")  # True


print("\n" + "=" * 60)
print("학습 완료!")
print("=" * 60)
print("핵심 요약:")
print("1. Boolean: True/False 두 가지 값")
print("2. 비교 연산자: ==, !=, <, >, <=, >=")
print("3. 논리 연산자:")
print("   - and: 둘 다 참")
print("   - or: 하나라도 참")
print("   - not: 반대")
print("4. 조건 조합으로 복잡한 로직 표현 가능")
print("=" * 60)
