# 🟡 응용 Problem 해답: 쇼핑몰 관리 시스템

## 📂 프로젝트 구조
```
2_intermediate_solution/
├── models.py      # User, Product 클래스 정의
├── utils.py       # 검증 함수들
├── main.py        # 메인 실행 파일
└── README.md      # 이 파일
```

## 🚀 실행 방법
```bash
cd 2_intermediate_solution
python main.py
```

## 📊 실행 결과
```
=== 쇼핑몰 관리 시스템 테스트 ===

1. 사용자 생성
사용자: 홍길동 (gildong@example.com), ID: U001

2. 상품 생성
상품: 노트북 - 1200000원, 재고: 10개, ID: P001

3. 구매 테스트
2개 구매 완료! 남은 재고: 8개
재고 총 가치: 9600000원

4. 예외 처리 테스트
재고 부족 에러: 재고가 부족합니다 (현재: 8개, 요청: 20개)
잘못된 이메일 에러: 이메일 형식이 올바르지 않습니다
잘못된 가격 에러: 가격은 0보다 커야 합니다
```

## 📝 핵심 학습 포인트

### 1. 모듈 분리
- `utils.py`: 재사용 가능한 검증 함수
- `models.py`: 비즈니스 로직을 담은 클래스
- `main.py`: 실행 및 테스트 코드

### 2. import 활용
```python
# utils.py에서 함수 가져오기
from utils import validate_email, validate_price, validate_stock

# models.py에서 클래스 가져오기
from models import User, Product
```

### 3. 타입 힌트
```python
def validate_email(email: str) -> bool:
    ...

def __init__(self, name: str, email: str, user_id: str) -> None:
    ...
```

### 4. 예외 처리
```python
# 검증 실패 시 예외 발생
if not validate_email(email):
    raise ValueError("이메일 형식이 올바르지 않습니다")

# try-except로 예외 처리
try:
    user = User("김철수", "invalidemail.com", "U002")
except ValueError as e:
    print(f"에러: {e}")
```

### 5. 클래스 설계
- 단일 책임 원칙: 각 클래스는 하나의 역할만
- User: 사용자 정보 관리
- Product: 상품 정보 및 재고 관리
