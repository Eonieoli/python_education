"""
Day 5 - 07교시: import 완전 정복
Basic 단계 - main.py (내 파일 import 활용!)

models.py와 utils.py를 import해서 사용하는 예제
"""

# ===== 내가 만든 모듈 import =====
print("=" * 50)
print("내가 만든 모듈 import!")
print("=" * 50)

# models.py에서 User, Product 클래스 가져오기
from models import User, Product

# utils.py에서 함수들 가져오기
from utils import (
    validate_email,
    format_price,
    calculate_discount,
    truncate_text
)

print("""
from models import User, Product
from utils import validate_email, format_price, ...

이제 models.py와 utils.py의 클래스와 함수를 사용할 수 있어요!
""")


# ===== 1. User 클래스 활용 =====
print("\n" + "=" * 50)
print("1. User 클래스 활용")
print("=" * 50)

# 사용자 생성
user1 = User("Alice", "alice@example.com")
user2 = User("Bob", "bob-invalid-email")  # 잘못된 이메일
user3 = User("Charlie")  # 이메일 없음

users = [user1, user2, user3]

# 각 사용자 정보 출력
for user in users:
    print(f"\n{user.greet()}")
    
    # 이메일 검증 (utils의 validate_email 사용!)
    if user.has_email():
        if validate_email(user.email):
            print("  ✓ 유효한 이메일")
        else:
            print("  ✗ 잘못된 이메일 형식")
    else:
        print("  - 이메일 없음")


# ===== 2. Product 클래스와 utils 함수 조합 =====
print("\n" + "=" * 50)
print("2. Product 클래스 + utils 함수 조합")
print("=" * 50)

# 상품 생성
products = [
    Product("노트북", 1500000, 5),
    Product("키보드", 150000, 10),
    Product("마우스", 50000, 0),  # 재고 없음
    Product("모니터", 300000, 3)
]

print("상품 목록:")
print("-" * 50)

for product in products:
    # 가격 포맷팅 (utils의 format_price 사용!)
    formatted_price = format_price(product.price)
    
    # 10% 할인가 계산 (utils의 calculate_discount 사용!)
    discount_price = calculate_discount(product.price, 0.1)
    formatted_discount = format_price(discount_price)
    
    # 상품명 잘라서 표시 (utils의 truncate_text 사용!)
    short_name = truncate_text(product.name, 10)
    
    print(f"\n상품명: {short_name}")
    print(f"  원가: {formatted_price}")
    print(f"  할인가 (10% 할인): {formatted_discount}")
    print(f"  재고: {product.stock}개")
    
    if product.is_available():
        print("  ✓ 구매 가능")
    else:
        print("  ✗ 품절")


# ===== 3. 상품 구매 시뮬레이션 =====
print("\n" + "=" * 50)
print("3. 상품 구매 시뮬레이션")
print("=" * 50)

# 노트북 구매 시도
laptop = products[0]
print(f"\n'{laptop.name}' 구매 시도:")
print(f"현재 재고: {laptop.stock}개")

if laptop.sell(2):
    print("✓ 2개 구매 성공!")
    print(f"남은 재고: {laptop.stock}개")
    
    # 총 결제 금액 계산 (할인 적용)
    total_price = laptop.price * 2
    discount_total = calculate_discount(total_price, 0.15)  # 15% 할인
    
    print(f"\n결제 정보:")
    print(f"  상품: {laptop.name}")
    print(f"  수량: 2개")
    print(f"  정가: {format_price(total_price)}")
    print(f"  할인율: 15%")
    print(f"  최종 금액: {format_price(discount_total)}")
else:
    print("✗ 재고 부족으로 구매 실패")


# ===== 4. 실전 시나리오: 사용자 + 상품 =====
print("\n" + "=" * 50)
print("4. 실전: 사용자가 상품 구매")
print("=" * 50)

# 구매자 정보
buyer = User("David", "david@example.com")
print(buyer.greet())

# 이메일 검증
if buyer.has_email() and validate_email(buyer.email):
    print("✓ 이메일 인증 완료\n")
    
    # 구매할 상품
    keyboard = products[1]
    print(f"구매 상품: {keyboard.name}")
    print(f"가격: {format_price(keyboard.price)}")
    
    # 회원 할인 20%
    final_price = calculate_discount(keyboard.price, 0.2)
    print(f"회원 할인가 (20%): {format_price(final_price)}")
    
    if keyboard.sell(1):
        print("\n✓ 구매가 완료되었습니다!")
        print(f"주문 확인 이메일을 {buyer.email}로 발송했습니다.")
    else:
        print("\n✗ 재고가 부족합니다.")
else:
    print("✗ 유효한 이메일이 필요합니다.")


# ===== 학습 정리 =====
print("\n" + "=" * 50)
print("학습 정리")
print("=" * 50)
print("""
내 파일을 모듈로 만들어서 import하는 방법:

1. models.py 파일 생성
   - User, Product 등의 클래스 정의

2. utils.py 파일 생성
   - validate_email, format_price 등의 함수 정의

3. main.py에서 import해서 사용
   from models import User, Product
   from utils import validate_email, format_price

장점:
- 코드를 기능별로 분리해서 관리하기 쉬움
- 재사용 가능한 코드를 모듈로 만들어서 여러 곳에서 활용
- FastAPI 프로젝트 구조의 기본!
  예) models/ - 데이터 모델
      utils/ - 유틸리티 함수
      api/ - API 엔드포인트

주의사항:
- 같은 디렉터리에 있어야 import 가능
- 파일명이 모듈명이 됨 (models.py → models)
- __name__ == "__main__" 으로 직접 실행 여부 확인 가능
""")
