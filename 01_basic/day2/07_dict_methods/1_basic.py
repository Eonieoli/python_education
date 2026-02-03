# 1_basic.py

"""
Day 2 - 7교시: 딕셔너리 메서드
Basic (강사 시연용)

학습 목표:
- keys(), values(), items() 메서드 이해
- get() 메서드로 안전한 접근 (KeyError 방지)
- pop() 메서드로 키-값 쌍 제거
- update() 메서드로 딕셔너리 병합
- in 연산자로 키 존재 확인
"""

# ============================================
# 1. keys(), values(), items() 메서드
# ============================================

# 사용자 정보 딕셔너리
user = {
    "name": "홍길동",
    "age": 25,
    "email": "hong@example.com"
}

# keys(): 모든 키 가져오기
print(user.keys())  # 출력: dict_keys(['name', 'age', 'email'])

# values(): 모든 값 가져오기
print(user.values())  # 출력: dict_values(['홍길동', 25, 'hong@example.com'])

# items(): 모든 키-값 쌍 가져오기 (튜플로)
print(user.items())  # 출력: dict_items([('name', '홍길동'), ('age', 25), ('email', 'hong@example.com')])


# ============================================
# 2. get() 메서드 - KeyError 방지 (핵심!)
# ============================================

# 일반 접근 방식의 문제점
product = {"name": "노트북", "price": 1200000}

# 존재하는 키는 문제 없음
print(product["name"])  # 출력: 노트북

# 존재하지 않는 키는 에러 발생!
# print(product["stock"])  # KeyError 발생!

# get() 메서드로 안전하게 접근
print(product.get("name"))  # 출력: 노트북
print(product.get("stock"))  # 출력: None (에러 없이 None 반환)

# get()의 두 번째 인자: 기본값 설정
print(product.get("stock", 0))  # 출력: 0 (키가 없으면 0 반환)
print(product.get("discount", 0.1))  # 출력: 0.1 (키가 없으면 0.1 반환)


# ============================================
# 3. pop() 메서드 - 키 제거 및 값 반환
# ============================================

# 장바구니 딕셔너리
cart = {
    "사과": 3,
    "바나나": 2,
    "우유": 1
}

print("원래 장바구니:", cart)  # 출력: 원래 장바구니: {'사과': 3, '바나나': 2, '우유': 1}

# pop()으로 키 제거하고 값 받기
banana_count = cart.pop("바나나")
print("제거된 바나나 개수:", banana_count)  # 출력: 제거된 바나나 개수: 2
print("남은 장바구니:", cart)  # 출력: 남은 장바구니: {'사과': 3, '우유': 1}

# pop()에도 기본값 설정 가능 (키가 없어도 에러 안남)
grape_count = cart.pop("포도", 0)
print("제거된 포도 개수:", grape_count)  # 출력: 제거된 포도 개수: 0


# ============================================
# 4. update() 메서드 - 딕셔너리 병합
# ============================================

# 기본 사용자 정보
user_info = {
    "name": "김철수",
    "age": 30
}

# 추가 정보
extra_info = {
    "email": "kim@example.com",
    "phone": "010-1234-5678"
}

print("원래 정보:", user_info)  # 출력: 원래 정보: {'name': '김철수', 'age': 30}

# update()로 병합
user_info.update(extra_info)
print("병합 후:", user_info)
# 출력: 병합 후: {'name': '김철수', 'age': 30, 'email': 'kim@example.com', 'phone': '010-1234-5678'}

# 기존 키가 있으면 값이 업데이트됨
user_info.update({"age": 31, "city": "서울"})
print("업데이트 후:", user_info)
# 출력: 업데이트 후: {'name': '김철수', 'age': 31, 'email': 'kim@example.com', 'phone': '010-1234-5678', 'city': '서울'}


# ============================================
# 5. in 연산자 - 키 존재 확인
# ============================================

# 재고 딕셔너리
inventory = {
    "노트북": 5,
    "마우스": 20,
    "키보드": 15
}

# in 연산자로 키 존재 확인 (True/False 반환)
print("노트북" in inventory)  # 출력: True
print("모니터" in inventory)  # 출력: False

# not in 연산자 (키가 없는지 확인)
print("모니터" not in inventory)  # 출력: True
print("노트북" not in inventory)  # 출력: False

# in 연산자 + get() 조합 (안전한 패턴)
# 방법 1: get()으로 기본값 제공
print(inventory.get("노트북", 0))  # 출력: 5 (있으면 값 반환)
print(inventory.get("모니터", 0))  # 출력: 0 (없으면 기본값 반환)

# 방법 2: in 연산자 결과 확인
has_laptop = "노트북" in inventory
has_monitor = "모니터" in inventory
print(f"노트북 있음: {has_laptop}")  # 출력: 노트북 있음: True
print(f"모니터 있음: {has_monitor}")  # 출력: 모니터 있음: False


# ============================================
# 6. 실전 예제: API 응답 처리
# ============================================

# API에서 받은 사용자 데이터 (일부 정보가 없을 수 있음)
api_response = {
    "user_id": 12345,
    "username": "alice",
    "email": "alice@example.com"
    # bio와 avatar는 선택적 필드
}

# get()으로 안전하게 접근
user_id = api_response.get("user_id")
username = api_response.get("username", "익명")
bio = api_response.get("bio", "소개가 없습니다")  # 없는 키는 기본값 사용
avatar = api_response.get("avatar", "default.png")

print(f"사용자: {username} (ID: {user_id})")  # 출력: 사용자: alice (ID: 12345)
print(f"소개: {bio}")  # 출력: 소개: 소개가 없습니다
print(f"프로필 사진: {avatar}")  # 출력: 프로필 사진: default.png
