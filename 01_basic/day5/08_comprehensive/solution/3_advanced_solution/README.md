# 🔴 도전 Problem 해답: FastAPI 스타일 API 모델 시스템

## 📂 프로젝트 구조
```
3_advanced_solution/
├── models.py         # BaseModel + 상속 모델들
├── validators.py     # 검증 함수들
├── main.py           # API 시뮬레이션
└── README.md         # 이 파일
```

## 🚀 실행 방법
```bash
cd 3_advanced_solution
python main.py
```

## 📊 실행 결과
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
비밀번호 검증 에러: 비밀번호는 대문자를 포함해야 합니다
```

## 📝 핵심 학습 포인트

### 1. BaseModel 패턴
```python
class BaseModel:
    """모든 모델의 부모 클래스"""
    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__.copy()

class UserBase(BaseModel):
    """공통 필드를 정의하는 중간 클래스"""
    def __init__(self, email: str) -> None:
        self.email = validate_email(email)
```

### 2. 모델 상속 구조
```
BaseModel (최상위)
    ↓
UserBase (공통 필드: email)
    ↓
    ├── UserCreate (요청: email + password)
    └── UserResponse (응답: email + id)
```

### 3. 요청/응답 모델 분리
**왜 분리할까?**
- **보안**: 응답에 비밀번호를 포함하지 않음
- **명확성**: 각 API의 입출력 구조가 명확함
- **타입 안정성**: 타입 힌트로 실수 방지

```python
# 회원가입 요청 (비밀번호 포함)
user_create = UserCreate("user@example.com", "SecurePass123")

# API 응답 (비밀번호 제외)
user_response = UserResponse("user@example.com", id=1)
```

### 4. 자동 검증
```python
class UserCreate(UserBase):
    def __init__(self, email: str, password: str) -> None:
        # 부모 클래스에서 이메일 검증
        super().__init__(email)
        
        # 비밀번호 검증
        self.password = validate_password(password)

# 객체 생성 시 자동으로 검증됨!
user = UserCreate("admin@example.com", "SecurePass123")  # 검증 통과
user = UserCreate("invalid", "short")  # ValueError 발생!
```

### 5. FastAPI 실전 연결
```python
from fastapi import FastAPI
from models import UserCreate, UserResponse

app = FastAPI()

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    # user는 자동으로 검증된 UserCreate 객체
    # 응답은 자동으로 UserResponse 형식으로 변환됨
    return UserResponse(email=user.email, id=1)
```

## 🎯 FastAPI에서 이렇게 사용됩니다

### 회원가입 API
```python
@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    # 1. 요청 자동 검증 (UserCreate)
    # 2. 비밀번호 해싱
    hashed_password = hash_password(user.password)
    
    # 3. DB 저장
    user_id = db.save(email=user.email, password=hashed_password)
    
    # 4. 응답 생성 (비밀번호 제외!)
    return UserResponse(email=user.email, id=user_id)
```

### 사용자 조회 API
```python
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    # DB에서 조회
    user = db.get(user_id)
    
    # UserResponse로 응답 (비밀번호 자동 제외)
    return UserResponse(email=user.email, id=user.id)
```

## 💡 왜 이 패턴이 중요한가?

1. **타입 안정성**: 잘못된 데이터 구조 사용 방지
2. **자동 검증**: 객체 생성 시점에 검증
3. **보안**: 응답 모델 분리로 민감 정보 제외
4. **문서화**: FastAPI가 자동으로 API 문서 생성
5. **유지보수**: 모델 변경 시 영향 범위 명확

## 🔥 실무 적용

이 패턴은 FastAPI의 핵심입니다. 앞으로 배울 내용:
- Pydantic의 실제 BaseModel 사용
- Field()를 통한 더 강력한 검증
- 자동 API 문서 생성 (Swagger UI)
- ORM과의 통합 (SQLAlchemy)
