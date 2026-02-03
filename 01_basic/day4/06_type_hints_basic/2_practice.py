# 2_practice.py

"""
Day 4 - 6교시: 타입 힌트 (1) - 기본 타입
Practice (강사와 함께 실습)

학습 목표:
- 기존 함수에 타입 힌트 추가하기
- 매개변수와 반환 타입 지정하기
- 다양한 기본 타입 조합 연습
"""

# ============================================
# 실습 1: 첫 타입 힌트 추가 (전체 타이핑)
# ============================================

# 타입 힌트가 없는 함수
def subtract_old(a, b):
    return a - b

# 타입 힌트를 추가한 함수
def subtract(a: int, b: int) -> int:
    """두 정수를 뺍니다"""
    return a - b

result = subtract(50, 20)
print(f"50 - 20 = {result}")  # 출력: 50 - 20 = 30


# ============================================
# 실습 2: 문자열 함수에 타입 힌트 추가 (TODO)
# ============================================

# TODO: 아래 함수에 타입 힌트를 추가하세요
# 힌트: name은 str 타입, 반환도 str 타입
def make_greeting(name: str) -> str:
    return f"{name}님, 환영합니다!"

print(make_greeting("김철수"))  # 출력: 김철수님, 환영합니다!


# ============================================
# 실습 3: 계산 함수에 타입 힌트 추가 (TODO)
# ============================================

# TODO: 아래 함수에 타입 힌트를 추가하세요
# 힌트: 모든 매개변수는 float, 반환도 float
def calculate_average(score1: float, score2: float, score3: float) -> float:
    """세 점수의 평균을 계산합니다"""
    return (score1 + score2 + score3) / 3

avg = calculate_average(85.5, 90.0, 88.5)
print(f"평균: {avg:.1f}점")  # 출력: 평균: 88.0점


# ============================================
# 실습 4: bool 반환 함수 (TODO)
# ============================================

# TODO: 아래 함수에 타입 힌트를 추가하세요
# 힌트: price는 int, discount_rate는 float, 반환은 bool
def is_discounted(price: int, discount_rate: float) -> bool:
    """할인율이 10% 이상이면 True를 반환합니다"""
    return discount_rate >= 0.1

print(is_discounted(10000, 0.15))  # 출력: True
print(is_discounted(10000, 0.05))  # 출력: False


# ============================================
# 실습 5: 여러 타입 조합 (TODO)
# ============================================

# TODO: 아래 함수에 타입 힌트를 추가하세요
# 힌트: name(str), age(int), height(float), is_student(bool), 반환(str)
def create_profile(name: str, age: int, height: float, is_student: bool) -> str:
    """사용자 프로필 문자열을 생성합니다"""
    student_status = "학생" if is_student else "일반"
    return f"{name}({age}세, {height}cm, {student_status})"

profile = create_profile("박지민", 20, 165.5, True)
print(profile)  # 출력: 박지민(20세, 165.5cm, 학생)
