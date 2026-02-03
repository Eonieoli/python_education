"""
Day 5 - 07교시: import 완전 정복
Exercise 단계 - main.py

validation과 models를 import해서 사용하세요.
모든 TODO를 완성해야 정상 동작합니다!
"""

# TODO: validation.py에서 필요한 함수들 import
# 힌트: from validation import validate_email, validate_phone, ...


# TODO: models.py에서 필요한 클래스들 import
# 힌트: from models import Product, User, ShoppingCart


print("=" * 50)
print("쇼핑몰 시스템")
print("=" * 50)


# ===== 1. 사용자 등록 =====
print("\n1. 사용자 등록")
print("-" * 50)

# TODO: User 객체 생성
# username: "alice123"
# email: "alice@example.com"
# password: "Password123"
# age: 25


# TODO: validation 함수로 검증
# validate_username(user.username)
# validate_email(user.email)
# validate_password(user.password)
# validate_age(user.age)


# TODO: 검증 결과 출력
# 힌트:
# if validate_username(user.username):
#     print("✓ 유효한 사용자명")
# else:
#     print("✗ 잘못된 사용자명")
# ... 나머지도 비슷하게


# TODO: 프로필 출력
# print(f"\n{user.get_profile()}")


# ===== 2. 상품 등록 =====
print("\n2. 상품 등록")
print("-" * 50)

# TODO: Product 객체 3개 생성
# products = [
#     Product("노트북", 1500000, 10),
#     Product("키보드", 150000, 20),
#     Product("마우스", 50000, 0)  # 재고 없음
# ]


# TODO: 각 상품 정보 출력
# 힌트: for product in products:
#           print(product.get_info())
#           if product.is_available():
#               print("  ✓ 구매 가능")
#           else:
#               print("  ✗ 품절")


# ===== 3. 장바구니에 상품 추가 =====
print("\n3. 장바구니")
print("-" * 50)

# TODO: ShoppingCart 객체 생성
# cart = ShoppingCart()


# TODO: 구매 가능한 상품만 장바구니에 추가
# 힌트: for product in products:
#           if product.is_available():
#               # 노트북은 1개, 나머지는 2개
#               quantity = 1 if product.name == "노트북" else 2
#               cart.add_item(product, quantity)
#               print(f"{product.name} {quantity}개 추가")


# TODO: 장바구니 정보 출력
# print(f"\n장바구니 상품 수: {cart.get_item_count()}개")
# print(f"총 금액: {cart.get_total_price():,}원")


# ===== 4. 재고 관리 =====
print("\n4. 재고 관리")
print("-" * 50)

# TODO: 마우스 재고 추가
# mouse = products[2]  # 마우스
# print(f"재고 추가 전: {mouse.get_info()}")
# mouse.restock(15)
# print(f"재고 추가 후: {mouse.get_info()}")


# ===== 5. 상품 판매 =====
print("\n5. 상품 판매")
print("-" * 50)

# TODO: 노트북 5개 판매 시도
# laptop = products[0]  # 노트북
# print(f"판매 전: {laptop.get_info()}")
# 
# if laptop.sell(5):
#     print("✓ 5개 판매 성공!")
#     print(f"판매 후: {laptop.get_info()}")
# else:
#     print("✗ 재고 부족으로 판매 실패")


# TODO: 노트북 10개 판매 시도 (재고 부족)
# if laptop.sell(10):
#     print("✓ 10개 판매 성공!")
# else:
#     print("✗ 재고 부족으로 10개 판매 실패")


# ===== 6. 잘못된 데이터 검증 =====
print("\n6. 잘못된 데이터 검증")
print("-" * 50)

# TODO: 잘못된 사용자 정보 테스트
# 힌트:
# invalid_username = "ab"  # 너무 짧음
# print(f"사용자명 '{invalid_username}': {validate_username(invalid_username)}")
# 
# invalid_email = "not-an-email"
# print(f"이메일 '{invalid_email}': {validate_email(invalid_email)}")
# 
# invalid_password = "weak"  # 너무 약함
# print(f"비밀번호 '{invalid_password}': {validate_password(invalid_password)}")
# 
# invalid_phone = "01012345678"  # 하이픈 없음
# print(f"전화번호 '{invalid_phone}': {validate_phone(invalid_phone)}")


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

3. FastAPI로 확장하면
   - validation/ 디렉터리: Pydantic validator
   - models/ 디렉터리: SQLAlchemy 모델
   - api/ 디렉터리: 엔드포인트 라우터
   
이것이 프로덕션 레벨 프로젝트 구조의 기본!
""")
