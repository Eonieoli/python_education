# 2_practice.py

"""
Day 2 - 7교시: 딕셔너리 메서드
Practice (강사와 함께 실습)

학습 목표:
- get()으로 안전한 접근
- update()로 딕셔너리 병합
- pop()으로 키 제거
- in으로 키 존재 확인
"""

# ============================================
# 실습 1: get()으로 안전한 접근 (전체 타이핑)
# ============================================

# API 응답 데이터 (일부 정보가 없을 수 있음)
response = {
    "status": "success",
    "data": {
        "name": "이영희",
        "email": "lee@example.com"
    }
}

# get()으로 안전하게 데이터 추출
status = response.get("status", "unknown")
data = response.get("data", {})
name = data.get("name", "익명")
email = data.get("email", "이메일 없음")
phone = data.get("phone", "전화번호 없음")  # 없는 키

# 결과 출력
print(f"상태: {status}")  # 출력: 상태: success
print(f"이름: {name}")  # 출력: 이름: 이영희
print(f"이메일: {email}")  # 출력: 이메일: lee@example.com
print(f"전화번호: {phone}")  # 출력: 전화번호: 전화번호 없음


# ============================================
# 실습 2: update()로 딕셔너리 병합 (TODO)
# ============================================

# 기본 상품 정보
product = {
    "name": "무선 마우스",
    "price": 35000
}

# 추가 정보 (재고, 할인율)
additional_info = {
    "stock": 50,
    "discount": 0.1
}

# TODO: update()를 사용하여 additional_info를 product에 병합하세요
# 힌트: product.update(additional_info)
product.update(additional_info)

print("병합 후 상품 정보:", product)
# 출력: 병합 후 상품 정보: {'name': '무선 마우스', 'price': 35000, 'stock': 50, 'discount': 0.1}


# ============================================
# 실습 3: pop()으로 키 제거 (TODO)
# ============================================

# 사용자 임시 데이터 (비밀번호 포함)
user_data = {
    "username": "hong123",
    "email": "hong@example.com",
    "password": "secret123"  # 응답에서 제거해야 함
}

# TODO: pop()을 사용하여 password 키를 제거하세요
# 힌트: user_data.pop("password")
user_data.pop("password")

print("안전한 사용자 데이터:", user_data)
# 출력: 안전한 사용자 데이터: {'username': 'hong123', 'email': 'hong@example.com'}


# ============================================
# 실습 4: in으로 키 존재 확인 (TODO)
# ============================================

# 설정 딕셔너리
config = {
    "debug": True,
    "max_connections": 100
}

# TODO: in 연산자로 "timeout" 키가 있는지 확인하여 변수에 저장하세요
# 힌트: has_timeout = "timeout" in config
has_timeout = "timeout" in config
print(f"timeout 키 존재: {has_timeout}")  # 출력: timeout 키 존재: False

# TODO: get()으로 timeout 값을 가져오세요 (없으면 기본값 30)
# 힌트: timeout = config.get("timeout", 30)
timeout = config.get("timeout", 30)
print(f"Timeout 설정: {timeout}초")  # 출력: Timeout 설정: 30초

# TODO: in 연산자로 "debug" 키가 있는지 확인하여 변수에 저장하세요
# 힌트: has_debug = "debug" in config
has_debug = "debug" in config
print(f"debug 키 존재: {has_debug}")  # 출력: debug 키 존재: True

# TODO: get()으로 debug 값을 가져오세요
# 힌트: debug_mode = config.get("debug")
debug_mode = config.get("debug")
print(f"디버그 모드: {debug_mode}")  # 출력: 디버그 모드: True
