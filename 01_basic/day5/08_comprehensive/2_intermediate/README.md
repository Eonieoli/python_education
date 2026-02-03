# 🟡 응용 Problem (15분): 쇼핑몰 관리 시스템

## 📋 학습 목표
1. 모듈화 프로젝트 구조 이해
2. models.py + utils.py + main.py 패턴
3. 타입 힌트 완벽 적용
4. 예외 처리 강화
5. import 활용

## 📂 프로젝트 구조
```
2_intermediate/
├── models.py      # User, Product 클래스 정의
├── utils.py       # 검증 함수들 (이메일, 가격 등)
├── main.py        # 메인 실행 파일
└── README.md      # 이 파일
```

## ✅ 작업 순서

### 1단계: utils.py 작성
검증 함수들을 작성하세요:
- `validate_email(email: str) -> bool`: 이메일 형식 검증 (@포함 여부)
- `validate_price(price: float) -> None`: 가격 검증 (0보다 커야 함, 예외 발생)
- `validate_stock(stock: int) -> None`: 재고 검증 (0 이상이어야 함, 예외 발생)

### 2단계: models.py 작성
클래스들을 작성하세요:

#### User 클래스
- 속성: name, email, user_id
- 메서드: __init__, __str__
- utils의 validate_email 사용하여 검증

#### Product 클래스
- 속성: name, price, stock, product_id
- 메서드: __init__, __str__, purchase(quantity), restock(quantity)
- utils의 validate_price, validate_stock 사용
- purchase 시 재고 부족하면 예외 발생

### 3단계: main.py 작성
- models와 utils를 import
- User와 Product 인스턴스 생성
- 구매 기능 테스트
- 예외 처리 테스트

## 🚀 실행 방법
```bash
python main.py
```

## 📝 기대 출력
```
=== 쇼핑몰 관리 시스템 테스트 ===

1. 사용자 생성
사용자: 홍길동 (gildong@example.com), ID: U001

2. 상품 생성
상품: 노트북 - 1200000원, 재고: 10개, ID: P001

3. 구매 테스트
2개 구매 완료! 남은 재고: 8개

4. 예외 처리 테스트
재고 부족 에러: 재고가 부족합니다 (현재: 8개, 요청: 20개)
잘못된 이메일 에러: 이메일 형식이 올바르지 않습니다
```

## 💡 힌트
- import 시: `from models import User, Product`
- import 시: `from utils import validate_email`
- 클래스 내에서 utils 함수 호출 가능
- 예외는 ValueError를 사용하거나 커스텀 예외 정의
