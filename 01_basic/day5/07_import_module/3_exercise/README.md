# Day 5 - 07교시: import 완전 정복 - Exercise 단계

## 📚 학습 목표

1. **검증 함수 모듈 만들기**
   - 이메일, 전화번호, 비밀번호 등 검증 함수 작성

2. **복잡한 클래스 모델 만들기**
   - Product, User, ShoppingCart 클래스 구현

3. **여러 모듈 조합하기**
   - validation + models를 함께 사용
   - 실전 쇼핑몰 시스템 구현

## 📂 파일 구조

```
3_exercise/
├── README.md           # 이 파일
├── validation.py      # 검증 함수들 (모두 TODO)
├── models.py          # 클래스들 (모두 TODO)
└── main.py            # 통합 사용 (모두 TODO)
```

## 🚀 실행 방법

### 1단계: validation.py 완성

다음 함수들을 구현하세요:

1. `validate_email(email: str) -> bool`
   - @와 .이 포함되어 있는지 확인

2. `validate_phone(phone: str) -> bool`
   - "010-1234-5678" 형식인지 확인

3. `validate_password(password: str) -> bool`
   - 8자 이상, 대문자 1개, 숫자 1개 포함

4. `validate_username(username: str) -> bool`
   - 3~20자, 알파벳과 숫자만

5. `validate_age(age: int) -> bool`
   - 0 < age <= 150

```bash
# 완성 후 테스트
python validation.py
```

### 2단계: models.py 완성

다음 클래스들을 구현하세요:

1. **Product 클래스**
   - `__init__(name, price, stock=0)`
   - `is_available() -> bool`
   - `sell(quantity=1) -> bool`
   - `restock(quantity) -> None`
   - `get_info() -> str`

2. **User 클래스**
   - `__init__(username, email, password, age=None)`
   - `get_profile() -> str`
   - `change_password(new_password) -> None`

3. **ShoppingCart 클래스**
   - `__init__()`
   - `add_item(product, quantity=1) -> None`
   - `get_total_price() -> int`
   - `get_item_count() -> int`

```bash
# 완성 후 테스트
python models.py
```

### 3단계: main.py 완성

모든 TODO를 완성하세요:

1. import 문 작성
2. 사용자 등록 및 검증
3. 상품 등록
4. 장바구니 관리
5. 재고 관리
6. 잘못된 데이터 검증

```bash
# 완성 후 실행
python main.py
```

## 💡 힌트

### validation.py 힌트

```python
def validate_email(email: str) -> bool:
    return "@" in email and "." in email

def validate_phone(phone: str) -> bool:
    parts = phone.split("-")
    return len(parts) == 3 and parts[0] == "010"

def validate_password(password: str) -> bool:
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_digit

def validate_username(username: str) -> bool:
    return 3 <= len(username) <= 20 and username.isalnum()

def validate_age(age: int) -> bool:
    return 0 < age <= 150
```

### models.py 힌트

```python
class Product:
    def __init__(self, name: str, price: int, stock: int = 0):
        self.name = name
        self.price = price
        self.stock = stock
    
    def is_available(self) -> bool:
        return self.stock > 0
    
    def sell(self, quantity: int = 1) -> bool:
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, product: Product, quantity: int = 1):
        self.items.append({"product": product, "quantity": quantity})
    
    def get_total_price(self) -> int:
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total
```

### main.py 힌트

```python
from validation import (
    validate_email,
    validate_phone,
    validate_password,
    validate_username,
    validate_age
)
from models import Product, User, ShoppingCart

# 사용자 생성
user = User("alice123", "alice@example.com", "Password123", 25)

# 검증
if validate_username(user.username):
    print("✓ 유효한 사용자명")

# 상품 생성
products = [
    Product("노트북", 1500000, 10),
    Product("키보드", 150000, 20)
]

# 장바구니
cart = ShoppingCart()
cart.add_item(products[0], 1)
print(f"총액: {cart.get_total_price():,}원")
```

## 📝 예상 출력

```
==================================================
쇼핑몰 시스템
==================================================

1. 사용자 등록
--------------------------------------------------
✓ 유효한 사용자명
✓ 유효한 이메일
✓ 유효한 비밀번호
✓ 유효한 나이

alice123 (alice@example.com) - 나이: 25세

2. 상품 등록
--------------------------------------------------
노트북 - 1,500,000원 (재고: 10개)
  ✓ 구매 가능
키보드 - 150,000원 (재고: 20개)
  ✓ 구매 가능
마우스 - 50,000원 (재고: 0개)
  ✗ 품절

3. 장바구니
--------------------------------------------------
노트북 1개 추가
키보드 2개 추가

장바구니 상품 수: 2개
총 금액: 1,800,000원

4. 재고 관리
--------------------------------------------------
재고 추가 전: 마우스 - 50,000원 (재고: 0개)
재고 추가 후: 마우스 - 50,000원 (재고: 15개)

5. 상품 판매
--------------------------------------------------
판매 전: 노트북 - 1,500,000원 (재고: 10개)
✓ 5개 판매 성공!
판매 후: 노트북 - 1,500,000원 (재고: 5개)
✗ 재고 부족으로 10개 판매 실패

6. 잘못된 데이터 검증
--------------------------------------------------
사용자명 'ab': False
이메일 'not-an-email': False
비밀번호 'weak': False
전화번호 '01012345678': False
```

## 🎯 학습 포인트

1. **모듈 분리의 실전 적용**
   - validation: 입력 검증
   - models: 비즈니스 로직
   - main: 통합 사용

2. **FastAPI 프로젝트 구조 미리보기**
   ```
   my_project/
   ├── validation/    # Pydantic validator
   ├── models/        # 데이터 모델
   ├── api/          # 엔드포인트
   └── main.py       # FastAPI 앱
   ```

3. **타입 힌트의 중요성**
   - Optional, List 등으로 명확한 타입
   - IDE 자동완성 지원
   - 버그 조기 발견

## ⚠️ 주의사항

1. **모든 TODO를 완성해야 함**
   - validation.py: 5개 함수
   - models.py: 3개 클래스
   - main.py: 여러 TODO

2. **테스트하면서 진행**
   - 각 파일을 직접 실행하면서 확인
   - 한 번에 완성하려 하지 말고 단계별로

3. **힌트 활용**
   - 막히면 위의 힌트 참고
   - solution 디렉토리에 정답 있음

## 🔍 다음 단계

완성 후:
1. `3_exercise_solution/` 디렉토리의 정답과 비교
2. 코드 리뷰하면서 개선점 찾기
3. 추가 기능 구현해보기
