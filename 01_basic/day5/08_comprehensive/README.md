# Day 5 - 8교시: 기초 과정 종합 실습

## 📋 개요
Python 기초 과정 5일차의 마지막 종합 실습 문제들입니다.
Day 1부터 Day 5까지 배운 모든 내용을 활용하는 3단계 문제로 구성되어 있습니다.

## 🎯 학습 목표
1. **클래스 설계**: 상속, 메서드 오버라이딩, 예외 처리
2. **모듈 분리**: import, 관심사 분리, 프로젝트 구조
3. **타입 시스템**: 완벽한 타입 힌트, FastAPI 스타일 모델
4. **종합 응용**: 5일간 배운 모든 개념의 통합

## 📂 프로젝트 구조

```
day5_lesson8_comprehensive/
├── 1_basic.py                      # 🟢 기초: 은행 계좌 클래스 시스템
├── 1_basic_solution.py
│
├── 2_intermediate/                 # 🟡 응용: 쇼핑몰 관리 시스템
│   ├── models.py
│   ├── utils.py
│   ├── main.py
│   └── README.md
│
├── 2_intermediate_solution/
│   ├── models.py
│   ├── utils.py
│   ├── main.py
│   └── README.md
│
├── 3_advanced/                     # 🔴 도전: FastAPI 스타일 API 모델
│   ├── models.py
│   ├── validators.py
│   ├── main.py
│   └── README.md
│
├── 3_advanced_solution/
│   ├── models.py
│   ├── validators.py
│   ├── main.py
│   └── README.md
│
└── README.md                       # 이 파일
```

## 🎓 문제 단계

### 🟢 기초 Problem (15분)
**파일**: `1_basic.py`

**주제**: 은행 계좌 관리 시스템

**핵심 개념**:
- 클래스 상속 (BankAccount → SavingsAccount, CheckingAccount)
- 메서드 오버라이딩
- 커스텀 예외 처리
- 타입 힌트 완벽 적용

**실행**:
```bash
python 1_basic.py
```

### 🟡 응용 Problem (15분)
**폴더**: `2_intermediate/`

**주제**: 쇼핑몰 관리 시스템 (모듈화)

**핵심 개념**:
- 모듈 분리 (models.py, utils.py, main.py)
- import 활용
- 계층별 책임 분리
- 타입 힌트 + 예외 처리 강화

**실행**:
```bash
cd 2_intermediate
python main.py
```

### 🔴 도전 Problem (10분)
**폴더**: `3_advanced/`

**주제**: FastAPI 스타일 API 모델 시스템

**핵심 개념**:
- BaseModel 패턴 (Pydantic 미리보기)
- 요청/응답 모델 분리
- 자동 검증
- 완전한 타입 시스템

**실행**:
```bash
cd 3_advanced
python main.py
```

## 📚 각 문제에서 활용하는 Day 1-5 개념

### Day 1: Python 시작과 기본 자료형
- ✅ 변수와 자료형
- ✅ 문자열 (슬라이싱, 메서드, f-string)
- ✅ 형변환

### Day 2: 컬렉션 자료형
- ✅ 리스트 (메서드, 내장 함수)
- ✅ 딕셔너리 (메서드, 활용)
- ✅ 튜플 (다중 반환)

### Day 3: 제어문
- ✅ Boolean, 비교 연산자
- ✅ 조건문 (if/elif/else)
- ✅ 반복문 (for, while)
- ✅ 리스트 컴프리헨션

### Day 4: 함수와 타입 힌트
- ✅ 함수 정의
- ✅ 매개변수 (위치, 기본값, 키워드)
- ✅ *args, **kwargs
- ✅ 타입 힌트 (기본, List, Dict, Optional)

### Day 5: 클래스 + 예외처리 + 모듈
- ✅ 클래스 기본
- ✅ 상속 구조
- ✅ 예외 처리 (try-except, raise)
- ✅ 모듈 분리 (import)
- ✅ 스코프, 데코레이터 개념

## 🎯 난이도별 권장 진행 방법

### 🟢 기초 - 은행 계좌 시스템
1. InsufficientFundsError 예외 정의
2. BankAccount 부모 클래스 작성
3. SavingsAccount (이자 기능)
4. CheckingAccount (마이너스 통장)
5. 테스트 코드 실행

**예상 시간**: 15분

### 🟡 응용 - 쇼핑몰 시스템
1. utils.py: 검증 함수 3개
2. models.py: User, Product 클래스
3. main.py: import하여 사용
4. 예외 처리 테스트

**예상 시간**: 15분

### 🔴 도전 - FastAPI 스타일
1. validators.py: 이메일/비밀번호 검증
2. models.py: BaseModel 패턴
3. UserBase → UserCreate, UserResponse 상속
4. main.py: API 시뮬레이션

**예상 시간**: 10분 (빠르게!)

## 💡 학습 팁

1. **순서대로 풀기**: 기초 → 응용 → 도전 순서 권장
2. **TODO 주석 활용**: 각 파일의 TODO를 따라가면 됨
3. **솔루션 참고**: 막히면 solution 파일 참고
4. **실행 확인**: 각 단계마다 실행하여 결과 확인
5. **타입 힌트 필수**: 모든 함수/메서드에 타입 힌트

## 🚀 실행 예시

### 기초 문제
```bash
# 문제 풀기
python 1_basic.py

# 해답 확인
python 1_basic_solution.py
```

### 응용 문제
```bash
# 문제 풀기
cd 2_intermediate
python main.py

# 해답 확인
cd ../2_intermediate_solution
python main.py
```

### 도전 문제
```bash
# 문제 풀기
cd 3_advanced
python main.py

# 해답 확인
cd ../3_advanced_solution
python main.py
```

## 🎓 완료 후 체크리스트

- [ ] 기초 문제: 클래스 상속과 예외 처리 이해
- [ ] 응용 문제: 모듈 분리와 import 활용
- [ ] 도전 문제: FastAPI 모델 패턴 이해
- [ ] 모든 타입 힌트 올바르게 적용
- [ ] 예외 처리로 안전한 코드 작성
- [ ] 프로젝트 구조화 능력 향상

## 🎉 축하합니다!

이 종합 실습을 완료했다면, Python 기초 과정 5일을 성공적으로 마쳤습니다!

다음 단계:
- **Day 6-10**: Python 응용 과정 (FastAPI 시작)
- **Day 11-15**: Python 심화 과정 (프로덕션 레벨)

## 📝 피드백

궁금한 점이나 개선 제안이 있다면 언제든 질문하세요!
