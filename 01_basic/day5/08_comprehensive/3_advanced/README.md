# 🔴 도전 Problem (10분): FastAPI 스타일 API 모델 시스템

## 📋 학습 목표
1. FastAPI 스타일 모델 구조 이해
2. BaseModel 패턴 (Pydantic 미리보기)
3. 완전한 타입 시스템
4. 데이터 검증 자동화

## 💡 핵심 개념
FastAPI에서는 Pydantic의 BaseModel을 상속받아 API 요청/응답 모델을 정의합니다.
이 문제에서는 Pydantic 없이 유사한 패턴을 구현해봅니다.

## 📂 프로젝트 구조
```
3_advanced/
├── models.py         # BaseModel + UserBase, UserCreate, UserResponse
├── validators.py     # 검증 함수들
├── main.py           # API 시뮬레이션
└── README.md         # 이 파일
```

## ✅ 작업 순서

### 1단계: validators.py 작성
검증 함수들을 작성하세요:
- `validate_email(email: str) -> str`: 이메일 검증 후 소문자로 반환
- `validate_password(password: str) -> str`: 비밀번호 강도 검증
  - 8자 이상
  - 대문자 포함
  - 검증 실패 시 예외 발생

### 2단계: models.py 작성

#### BaseModel 클래스 (부모 클래스)
- 모든 모델의 부모 클래스
- `to_dict() -> dict` 메서드 제공
- 타입 힌트 완벽 적용

#### UserBase 클래스 (BaseModel 상속)
- 속성: email (str)
- 이메일 검증 포함

#### UserCreate 클래스 (UserBase 상속)
- 추가 속성: password (str)
- 비밀번호 검증 포함
- 회원가입 시 사용

#### UserResponse 클래스 (UserBase 상속)
- 추가 속성: id (int)
- 비밀번호 없음 (보안!)
- API 응답 시 사용

### 3단계: main.py 작성
- FastAPI 스타일 함수 작성
- `create_user(user_data: UserCreate) -> UserResponse`
- `get_user(user_id: int) -> UserResponse`
- 검증 및 변환 테스트

## 🚀 실행 방법
```bash
python main.py
```

## 📝 기대 출력
```
=== FastAPI 스타일 API 모델 테스트 ===

1. 회원가입 (UserCreate -> UserResponse)
요청 데이터: {'email': 'admin@example.com', 'password': 'SecurePass123'}
응답 데이터: {'email': 'admin@example.com', 'id': 1}

2. 사용자 조회 (UserResponse)
응답 데이터: {'email': 'admin@example.com', 'id': 1}

3. 예외 처리 테스트
이메일 검증 에러: 이메일 형식이 올바르지 않습니다
비밀번호 검증 에러: 비밀번호는 8자 이상이어야 합니다
```

## 💡 힌트
- BaseModel의 `to_dict()` 메서드는 모든 속성을 딕셔너리로 변환
- 자식 클래스는 부모의 `__init__`을 호출하여 검증 수행
- FastAPI에서는 이렇게 모델을 분리해서 사용합니다:
  - UserCreate: 회원가입 요청 (비밀번호 포함)
  - UserResponse: API 응답 (비밀번호 제외)

## 🎯 왜 이렇게 하나요?
1. **보안**: 응답에 비밀번호를 포함하지 않음
2. **명확성**: 요청과 응답 구조를 명확히 분리
3. **검증**: 데이터 생성 시 자동으로 검증
4. **타입 안정성**: 타입 힌트로 실수 방지
