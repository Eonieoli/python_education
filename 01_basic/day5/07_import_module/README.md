# Day 5 - 07교시: import 완전 정복

## 📚 교시 개요

**학습 목표**:
1. Python 표준 라이브러리 import 방법 이해
2. typing 모듈 활용 (List, Dict, Optional, Union)
3. 내 파일을 모듈로 만들어서 import하기
4. 여러 모듈을 조합해서 실전 프로젝트 구조 만들기

**FastAPI 연결**:
- 프로젝트 구조의 기초 (models/, utils/, api/ 분리)
- typing 모듈은 Pydantic의 핵심
- 모듈 import는 FastAPI 프로젝트의 필수 기술

## 📂 전체 디렉토리 구조

```
day5_07_import/
├── README.md                      # 이 파일
│
├── 1_basic/                       # Basic 단계 (강사 시연)
│   ├── README.md
│   ├── basic_import.py           # 표준 라이브러리 import
│   ├── typing_review.py          # typing 모듈 복습
│   ├── models.py                 # User, Product 클래스
│   ├── utils.py                  # 유틸리티 함수들
│   └── main.py                   # models + utils 통합
│
├── 2_practice/                    # Practice 단계 (함께 실습)
│   ├── README.md
│   ├── student_model.py          # Student 클래스 (TODO 포함)
│   ├── grade_utils.py            # 성적 함수들 (TODO 포함)
│   └── main.py                   # 통합 (TODO 포함)
│
├── 3_exercise/                    # Exercise 단계 (학생 독립)
│   ├── README.md
│   ├── validation.py             # 검증 함수들 (TODO만)
│   ├── models.py                 # 클래스들 (TODO만)
│   └── main.py                   # 통합 (TODO만)
│
└── 3_exercise_solution/           # Exercise 정답
    ├── README.md
    ├── validation.py             # 검증 함수들 (완성)
    ├── models.py                 # 클래스들 (완성)
    └── main.py                   # 통합 (완성)
```

## 🎯 단계별 학습 가이드

### 1️⃣ Basic 단계 (25분) - 강사 시연

**목표**: import의 기본 개념 이해

**실행 순서**:
```bash
cd 1_basic

# 1. 표준 라이브러리 import
python basic_import.py
# json, math, datetime, random 등 사용법

# 2. typing 모듈 복습
python typing_review.py
# List, Dict, Optional, Union 활용

# 3. 내 파일 개별 테스트 (선택)
python models.py
python utils.py

# 4. 통합 사용 (중요!)
python main.py
# models와 utils를 import해서 사용
```

**핵심 개념**:
- `import 모듈명`: 모듈 전체 가져오기
- `from 모듈명 import 함수명`: 특정 함수만 가져오기
- `import 모듈명 as 별칭`: 짧은 이름으로 사용
- Python 표준 라이브러리는 설치 불필요
- typing 모듈로 타입 힌트 강화

### 2️⃣ Practice 단계 (18분) - 함께 실습

**목표**: 모델과 유틸리티 모듈 만들기

**실행 순서**:
```bash
cd 2_practice

# 1. TODO 완성하기
# - student_model.py: get_average(), get_grade_letter()
# - grade_utils.py: 통계 함수들
# - main.py: import + 통합

# 2. 개별 테스트
python student_model.py
python grade_utils.py

# 3. 메인 실행
python main.py
```

**완성해야 할 부분**:
- Student 클래스: 평균 계산, 등급 판정
- 성적 유틸리티: 반 평균, 최고/최저 점수, 합격자 수
- 메인 프로그램: import + 통합 사용

### 3️⃣ Exercise 단계 (5분) - 학생 독립 실습

**목표**: 검증 + 모델을 조합한 쇼핑몰 시스템

**실행 순서**:
```bash
cd 3_exercise

# 모든 TODO를 완성하세요!
# - validation.py: 5개 검증 함수
# - models.py: 3개 클래스
# - main.py: 통합

# 완성 후 실행
python main.py
```

**완성해야 할 부분**:
- validation.py: 이메일, 전화번호, 비밀번호, 사용자명, 나이 검증
- models.py: Product, User, ShoppingCart 클래스
- main.py: 전체 쇼핑몰 시스템 통합

**막히면**: `3_exercise_solution/` 디렉토리의 정답 참고

## 💡 핵심 학습 포인트

### 1. import 3가지 방법

```python
# 방법 1: 모듈 전체 import
import json
data = json.dumps({"key": "value"})

# 방법 2: 특정 함수만 import
from json import dumps, loads
data = dumps({"key": "value"})

# 방법 3: 별칭 사용
import math as m
area = m.pi * r**2
```

### 2. typing 모듈 활용

```python
from typing import List, Dict, Optional, Union

def get_users() -> List[Dict[str, str]]:
    return [{"name": "Alice", "email": "alice@example.com"}]

def find_user(user_id: int) -> Optional[Dict[str, str]]:
    # 못 찾으면 None 반환 가능!
    return None
```

### 3. 내 파일 모듈화

```python
# models.py
class User:
    def __init__(self, name: str):
        self.name = name

# utils.py
def validate_email(email: str) -> bool:
    return "@" in email

# main.py
from models import User
from utils import validate_email

user = User("Alice")
if validate_email(user.email):
    print("Valid!")
```

## 🎓 FastAPI 연결

현재 배운 구조 → FastAPI 프로젝트 구조

```
현재 구조:                FastAPI 프로젝트 구조:
─────────                ───────────────────
validation.py     →      app/validation/
models.py         →      app/models/
utils.py          →      app/utils/
main.py           →      app/api/routers/
                         main.py (FastAPI 앱)
```

**응용 과정 (Day 6-10)에서 배울 내용**:
- FastAPI 프로젝트 구조
- Pydantic 모델 (타입 힌트 활용!)
- API 라우터 분리
- 의존성 주입

## ⚠️ 주의사항

1. **파일 위치**
   - import하려는 파일들은 같은 디렉터리에 있어야 함
   - models.py, utils.py, main.py가 한 폴더에

2. **파일명 = 모듈명**
   - models.py → `from models import ...`
   - utils.py → `from utils import ...`

3. **순환 import 주의**
   - A.py가 B.py를 import하고
   - B.py가 A.py를 import하면 에러!

4. **__name__ == "__main__"**
   - 파일을 직접 실행할 때만 동작하는 코드
   - import될 때는 실행되지 않음

## 🔍 문제 해결

### Q1: ModuleNotFoundError가 나요!

```bash
# 현재 디렉터리 확인
pwd

# 파일 목록 확인
ls

# models.py, utils.py, main.py가 같은 폴더에 있어야 함!
```

### Q2: import했는데 함수/클래스가 없다고 나요!

```python
# 잘못된 예
import models
user = User("Alice")  # NameError!

# 올바른 예
from models import User
user = User("Alice")  # OK!
```

### Q3: 타입 힌트에서 List, Dict를 못 찾아요!

```python
# typing에서 import 필요!
from typing import List, Dict, Optional, Union

def get_items() -> List[str]:
    return ["a", "b", "c"]
```

## 🚀 실습 권장 순서

1. **Basic 단계 (25분)**
   - README 읽기 (3분)
   - 파일들 순서대로 실행 (15분)
   - 코드 리뷰 (7분)

2. **Practice 단계 (18분)**
   - README 읽기 (3분)
   - TODO 완성 (12분)
   - 실행 및 확인 (3분)

3. **Exercise 단계 (5분)**
   - README 읽기 (1분)
   - TODO 완성 (3분)
   - 실행 (1분)

4. **정답 확인**
   - 막히면 3_exercise_solution/ 참고
   - 코드 비교하며 학습

## 📖 참고 자료

### Python 표준 라이브러리 문서
- json: https://docs.python.org/3/library/json.html
- datetime: https://docs.python.org/3/library/datetime.html
- typing: https://docs.python.org/3/library/typing.html

### 다음 학습 주제
- **Day 5-08교시**: 기초 과정 종합 실습
- **Day 6**: 웹과 API의 이해
- **Day 7**: FastAPI 시작하기

## 🎯 학습 체크리스트

- [ ] import 3가지 방법을 이해했나요?
- [ ] typing 모듈을 사용할 수 있나요?
- [ ] 내 파일을 모듈로 만들 수 있나요?
- [ ] 여러 모듈을 조합해서 사용할 수 있나요?
- [ ] FastAPI 프로젝트 구조를 상상할 수 있나요?

모두 체크되었다면 다음 교시로! 🎉
