"""
Day 5 - 07교시: import 완전 정복
Exercise Solution - main.py (정답)

validation과 models를 import해서 사용하는 완성된 버전입니다.
"""

# validation.py에서 함수들 import
from validation import (
    validate_email,
    validate_phone,
    validate_password,
    validate_username,
    validate_age
)

# models.py에서 클래스들 import
from models import Product, User, ShoppingCart


print("=" * 50)
print("쇼핑몰 시스템")
print("=" * 50)


# ===== 1. 사용자 등록 =====
print("\n1. 사용자 등록")
print("-" * 50)

# User 객체 생성
user = User("alice123", "alice@example.com", "Password123", 25)

# validation 함수로 검증
print("사용자 정보 검증:")

if validate_username(user.username):
    print("  ✓ 유효한 사용자명")
else:
    print("  ✗ 잘못된 사용자명")

if validate_email(user.email):
    print("  ✓ 유효한 이메일")
else:
    print("  ✗ 잘못된 이메일")

if validate_password(user.password):
    print("  ✓ 유효한 비밀번호")
else:
    print("  ✗ 잘못된 비밀번호")

if validate_age(user.age):
    print("  ✓ 유효한 나이")
else:
    print("  ✗ 잘못된 나이")

# 프로필 출력
print(f"\n{user.get_profile()}")


# ===== 2. 상품 등록 =====
print("\n2. 상품 등록")
print("-" * 50)

# Product 객체 3개 생성
products = [
    Product("노트북", 1500000, 10),
    Product("키보드", 150000, 20),
    Product("마우스", 50000, 0)  # 재고 없음
]

# 각 상품 정보 출력
for product in products:
    print(product.get_info())
    if product.is_available():
        print("  ✓ 구매 가능")
    else:
        print("  ✗ 품절")


# ===== 3. 장바구니에 상품 추가 =====
print("\n3. 장바구니")
print("-" * 50)

# ShoppingCart 객체 생성
cart = ShoppingCart()

# 구매 가능한 상품만 장바구니에 추가
for product in products:
    if product.is_available():
        # 노트북은 1개, 나머지는 2개
        quantity = 1 if product.name == "노트북" else 2
        cart.add_item(product, quantity)
        print(f"{product.name} {quantity}개 추가")

# 장바구니 정보 출력
print(f"\n장바구니 상품 수: {cart.get_item_count()}개")
print(f"총 금액: {cart.get_total_price():,}원")


# ===== 4. 재고 관리 =====
print("\n4. 재고 관리")
print("-" * 50)

# 마우스 재고 추가
mouse = products[2]  # 마우스
print(f"재고 추가 전: {mouse.get_info()}")

mouse.restock(15)
print(f"재고 추가 후: {mouse.get_info()}")


# ===== 5. 상품 판매 =====
print("\n5. 상품 판매")
print("-" * 50)

# 노트북 5개 판매 시도
laptop = products[0]  # 노트북
print(f"판매 전: {laptop.get_info()}")

if laptop.sell(5):
    print("✓ 5개 판매 성공!")
    print(f"판매 후: {laptop.get_info()}")
else:
    print("✗ 재고 부족으로 판매 실패")

# 노트북 10개 판매 시도 (재고 부족)
print(f"\n현재 재고: {laptop.stock}개")
print("10개 판매 시도:")
if laptop.sell(10):
    print("✓ 10개 판매 성공!")
else:
    print("✗ 재고 부족으로 10개 판매 실패")


# ===== 6. 잘못된 데이터 검증 =====
print("\n6. 잘못된 데이터 검증")
print("-" * 50)

# 잘못된 사용자 정보 테스트
test_data = {
    "사용자명 'ab'": validate_username("ab"),  # 너무 짧음
    "이메일 'not-an-email'": validate_email("not-an-email"),  # @나 .이 없음
    "비밀번호 'weak'": validate_password("weak"),  # 너무 약함
    "전화번호 '01012345678'": validate_phone("01012345678"),  # 하이픈 없음
    "나이 200": validate_age(200),  # 너무 많음
}

for desc, result in test_data.items():
    symbol = "✓" if result else "✗"
    print(f"{symbol} {desc}: {result}")


# ===== 7. 장바구니 상세 내역 =====
print("\n7. 장바구니 상세 내역")
print("-" * 50)

print("구매 목록:")
for i, item in enumerate(cart.items, 1):
    product = item["product"]
    quantity = item["quantity"]
    subtotal = product.price * quantity
    print(f"{i}. {product.name} x {quantity} = {subtotal:,}원")

print(f"\n총 결제 금액: {cart.get_total_price():,}원")


# ===== 8. 추가 기능: 전화번호 검증 =====
print("\n8. 전화번호 등록")
print("-" * 50)

phone_numbers = [
    "010-1234-5678",  # 유효
    "010-9999-8888",  # 유효
    "02-1234-5678",   # 잘못됨 (010이 아님)
    "01012345678"     # 잘못됨 (하이픈 없음)
]

for phone in phone_numbers:
    if validate_phone(phone):
        print(f"✓ {phone}: 등록 가능")
    else:
        print(f"✗ {phone}: 등록 불가 (형식 오류)")


# ===== 학습 정리 =====
print("\n" + "=" * 50)
print("학습 정리")
print("=" * 50)
print("""
이 예제에서 배운 것:

1. 여러 모듈을 조합해서 사용
   - validation.py: 데이터 검증 함수들
   - models.py: Product, User, ShoppingCart 클래스들
   - main.py: 두 모듈을 import해서 통합

2. 실전 패턴
   - 사용자 입력 검증 (validation)
   - 비즈니스 로직 (models)
   - 메인 프로그램 (main)
   
   이것이 바로 프로덕션 레벨 코드 구조!

3. FastAPI로 확장하면
   - validation/ 디렉터리: Pydantic validator
   - models/ 디렉터리: SQLAlchemy 모델
   - api/ 디렉터리: 엔드포인트 라우터
   - main.py: FastAPI 앱 실행
   
   응용 과정(Day 6-10)에서 배울 내용입니다!

4. 타입 힌트의 중요성
   - Optional, List 등으로 명확한 타입 지정
   - IDE 자동완성 지원
   - 버그를 코드 작성 시점에 발견
   - FastAPI/Pydantic의 핵심!
""")
