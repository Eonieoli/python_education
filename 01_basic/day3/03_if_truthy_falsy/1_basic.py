# 1_basic.py

"""
Day 3 - 3교시: 조건문 (if) + Truthy/Falsy
Basic (강사 시연용)

학습 목표:
- if/elif/else 기본 구조 이해
- Truthy/Falsy 개념 완전 정복
- in 연산자 활용
"""

# ============================================
# 1. if/elif/else 기본 구조
# ============================================

# 성적에 따른 등급 판정
score = 85

if score >= 90:
    print("A 등급")
elif score >= 80:
    print("B 등급")  # 출력: B 등급
elif score >= 70:
    print("C 등급")
else:
    print("D 등급")


# ============================================
# 2. Truthy/Falsy - 핵심 개념! ⭐⭐⭐
# ============================================

# False로 취급되는 값들 (Falsy)
if "":        print("실행 안 됨")  # 빈 문자열
if 0:         print("실행 안 됨")  # 숫자 0
if []:        print("실행 안 됨")  # 빈 리스트
if {}:        print("실행 안 됨")  # 빈 딕셔너리
if None:      print("실행 안 됨")  # None

# True로 취급되는 값들 (Truthy)
if "hello":   print("문자열 있음")  # 출력: 문자열 있음
if 1:         print("0이 아님")     # 출력: 0이 아님
if [1, 2]:    print("리스트 있음")  # 출력: 리스트 있음

# 실전 활용: 장바구니 체크
cart = []
if cart:
    print("상품이 있습니다")
else:
    print("장바구니가 비어있습니다")  # 출력: 장바구니가 비어있습니다


# ============================================
# 3. in 연산자 활용
# ============================================

# 리스트에서 값 찾기
fruits = ["사과", "바나나", "딸기"]
if "사과" in fruits:
    print("사과가 있습니다")  # 출력: 사과가 있습니다

# 딕셔너리에서 키 확인
user = {"name": "홍길동", "age": 25}
if "email" in user:
    print("이메일 있음")
else:
    print("이메일 없음")  # 출력: 이메일 없음


# ============================================
# 4. 실전 예제: 로그인 검증
# ============================================

username = "admin"
password = "1234"
input_id = ""
input_pw = "1234"

if not input_id:  # 빈 문자열 체크 (Truthy/Falsy 활용)
    print("아이디를 입력하세요")  # 출력: 아이디를 입력하세요
elif not input_pw:
    print("비밀번호를 입력하세요")
elif input_id == username and input_pw == password:
    print("로그인 성공!")
else:
    print("로그인 실패!")
