# Day 5 - 07교시: import 완전 정복 - Basic 단계

## 📚 학습 목표

1. **표준 라이브러리 import 이해**
   - `import 모듈명`
   - `from 모듈명 import 함수명`
   - `import 모듈명 as 별칭`

2. **typing 모듈 복습**
   - `List`, `Dict`, `Optional`, `Union`
   - 어제 배운 타입 힌트와 연결

3. **내 파일 import 활용**
   - 모듈 파일 만들기 (`models.py`, `utils.py`)
   - 다른 파일에서 import해서 사용하기

## 📂 파일 구조

```
1_basic/
├── README.md                 # 이 파일
├── basic_import.py          # 표준 라이브러리 import 시연
├── typing_review.py         # typing 모듈 복습
├── models.py                # User, Product 클래스
├── utils.py                 # 유틸리티 함수들
└── main.py                  # models와 utils를 import해서 사용
```

## 🚀 실행 방법

### 1단계: 표준 라이브러리 import
```bash
python basic_import.py
```
- json, math, datetime, random 등 표준 라이브러리 사용법
- import, from import, as 별칭 사용법

### 2단계: typing 모듈 복습
```bash
python typing_review.py
```
- List, Dict, Optional, Union 타입 복습
- 어제 배운 타입 힌트 활용

### 3단계: 내 파일 테스트 (선택)
```bash
python models.py    # User, Product 클래스 테스트
python utils.py     # 유틸리티 함수 테스트
```

### 4단계: 통합 사용 (중요!)
```bash
python main.py
```
- models.py와 utils.py를 import해서 사용
- 클래스와 함수를 조합해서 실전 시나리오 구현

## 💡 핵심 개념

### import 방법 3가지

```python
# 1. 모듈 전체 import
import json
result = json.dumps(data)

# 2. 특정 함수만 import
from json import dumps, loads
result = dumps(data)

# 3. 별칭 사용
import math as m
area = m.pi * r**2
```

### typing 모듈

```python
from typing import List, Dict, Optional, Union

def get_users() -> List[Dict[str, str]]:
    return [{"name": "Alice", "email": "alice@example.com"}]

def find_user(user_id: int) -> Optional[Dict[str, str]]:
    # 없으면 None 반환 가능!
    return None
```

### 내 파일 import

```python
# models.py에 User 클래스 정의
# utils.py에 validate_email 함수 정의

# main.py에서 사용
from models import User
from utils import validate_email

user = User("Alice", "alice@example.com")
if validate_email(user.email):
    print("Valid!")
```

## ⚠️ 주의사항

1. **같은 디렉터리에 있어야 import 가능**
   - models.py, utils.py, main.py가 같은 폴더에 있어야 함

2. **파일명이 모듈명**
   - models.py → `from models import ...`
   - utils.py → `from utils import ...`

3. **Python 표준 라이브러리는 설치 불필요**
   - json, math, datetime, random 등은 바로 사용 가능
   - typing도 표준 라이브러리!

## 🎯 다음 단계

이제 Practice 단계에서:
- 학생 모델 모듈 만들기
- 성적 처리 유틸리티 모듈 만들기
- 여러 모듈을 조합해서 사용하기

**핵심**: FastAPI 프로젝트에서는 이렇게 기능별로 파일을 분리해서 관리합니다!
