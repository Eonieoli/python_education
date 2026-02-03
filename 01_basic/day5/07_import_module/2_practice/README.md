# Day 5 - 07교시: import 완전 정복 - Practice 단계

## 📚 학습 목표

1. **모델 모듈 만들기**
   - Student 클래스 정의
   - 성적 관리 메서드 구현

2. **유틸리티 모듈 만들기**
   - 성적 처리 함수들 구현
   - 통계 계산, 등급 분포 등

3. **모듈 조합해서 사용하기**
   - student_model과 grade_utils를 import
   - 클래스와 함수를 함께 활용

## 📂 파일 구조

```
2_practice/
├── README.md                 # 이 파일
├── student_model.py         # Student 클래스 (TODO 포함)
├── grade_utils.py           # 성적 처리 함수들 (TODO 포함)
└── main.py                  # import해서 사용 (TODO 포함)
```

## 🚀 실행 방법

### 1단계: 각 파일 테스트 (선택)

```bash
# Student 클래스 테스트
python student_model.py

# 성적 유틸리티 함수 테스트
python grade_utils.py
```

### 2단계: TODO 완성하기

각 파일의 TODO 주석을 찾아서 완성하세요:

1. **student_model.py**
   - `get_average()`: 평균 계산
   - `get_grade_letter()`: 등급 판정

2. **grade_utils.py**
   - `calculate_class_average()`: 반 평균 계산
   - `find_lowest_grade()`: 최저 점수 찾기
   - `count_passing_students()`: 합격자 수 세기
   - `format_grade_report()`: 리포트 생성

3. **main.py**
   - import 문 작성
   - 학생 생성
   - 통계 계산
   - 리포트 출력

### 3단계: 메인 프로그램 실행

```bash
python main.py
```

## 💡 힌트

### student_model.py

```python
# get_average() 힌트
def get_average(self) -> float:
    if not self.grades:
        return 0.0
    return sum(self.grades) / len(self.grades)

# get_grade_letter() 힌트
def get_grade_letter(self) -> str:
    avg = self.get_average()
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    # ... 나머지도 비슷하게
```

### grade_utils.py

```python
# calculate_class_average() 힌트
def calculate_class_average(grades: List[int]) -> float:
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

# count_passing_students() 힌트
def count_passing_students(grades: List[int], passing_score: int = 60) -> int:
    return len([g for g in grades if g >= passing_score])

# format_grade_report() 힌트
def format_grade_report(...) -> str:
    return f"""총 학생 수: {total_students}명
평균 점수: {average:.1f}점
최고 점수: {highest}점
최저 점수: {lowest}점"""
```

### main.py

```python
# import 힌트
from student_model import Student
from grade_utils import (
    calculate_class_average,
    find_highest_grade,
    find_lowest_grade,
    count_passing_students,
    get_grade_distribution,
    format_grade_report
)

# 학생 생성 힌트
students = [
    Student("김철수", "2024001", [85, 90, 88]),
    Student("이영희", "2024002", [92, 88, 95]),
    Student("박민수", "2024003", [78, 82, 80])
]

# 전체 성적 모으기 힌트
all_grades = []
for student in students:
    all_grades.extend(student.grades)
```

## 📝 예상 출력

```
==================================================
학생 성적 관리 시스템
==================================================

1. 학생 정보 생성
--------------------------------------------------
생성된 학생 정보:
김철수 (2024001) - 평균: 87.7점 (B)
이영희 (2024002) - 평균: 91.7점 (A)
박민수 (2024003) - 평균: 80.0점 (B)

2. 반 전체 성적 통계
--------------------------------------------------
전체 성적: [85, 90, 88, 92, 88, 95, 78, 82, 80]
반 평균: 86.4점
최고 점수: 95점
최저 점수: 78점
합격자 수: 9명 (60점 이상)

3. 등급 분포
--------------------------------------------------
A: 2명
B: 6명
C: 1명
D: 0명
F: 0명

4. 성적 리포트
--------------------------------------------------
총 학생 수: 3명
평균 점수: 86.4점
최고 점수: 95점
최저 점수: 78점
...
```

## 🎯 학습 포인트

1. **모듈 분리의 장점**
   - 코드를 기능별로 정리
   - 재사용 가능한 코드 작성
   - 유지보수가 쉬움

2. **import 활용**
   - 다른 파일의 클래스와 함수 사용
   - FastAPI 프로젝트 구조의 기본

3. **타입 힌트 활용**
   - List, Optional 등으로 명확한 타입 지정
   - IDE 자동완성 지원

## ⚠️ 주의사항

1. **파일들이 같은 디렉터리에 있어야 함**
   - student_model.py, grade_utils.py, main.py

2. **TODO를 모두 완성해야 정상 실행됨**
   - 하나씩 완성하면서 테스트하세요

3. **테스트 방법**
   - 각 파일을 직접 실행해보면서 확인
   - main.py 실행 전에 각 모듈 테스트
