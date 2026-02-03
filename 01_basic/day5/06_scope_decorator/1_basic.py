# 1_basic.py

"""
Day 5 - 6교시: 스코프 + 데코레이터 개념
Basic (강사 시연용)

학습 목표:
- 지역 변수와 전역 변수의 차이 이해
- 변수 스코프 규칙 이해
- 클래스 변수와 인스턴스 변수 구분
- 데코레이터 개념 이해 (@ 문법)
- FastAPI에서 데코레이터 활용 미리보기
"""


# ============================================
# 1. 변수 스코프 (Scope) 기본
# ============================================

# 지역 변수: 함수 내부에서만 사용 가능
def calculate_area():
    width = 10  # 지역 변수
    height = 5  # 지역 변수
    area = width * height
    return area

result = calculate_area()
print("면적:", result)  # 출력: 면적: 50
# print(width)  # 에러! width는 함수 밖에서 접근 불가


# 전역 변수: 프로그램 전체에서 사용 가능
total_count = 0  # 전역 변수

def add_count():
    global total_count  # global 키워드로 전역 변수 사용
    total_count += 1
    print(f"현재 카운트: {total_count}")

add_count()  # 출력: 현재 카운트: 1
add_count()  # 출력: 현재 카운트: 2
add_count()  # 출력: 현재 카운트: 3


# ============================================
# 2. 클래스와 스코프
# ============================================

class Counter:
    # 클래스 변수: 모든 인스턴스가 공유
    total = 0
    
    def __init__(self, name: str):
        # 인스턴스 변수: 각 인스턴스마다 독립적
        self.name = name
        self.count = 0
        Counter.total += 1  # 클래스 변수 접근
    
    def increment(self) -> None:
        self.count += 1  # 인스턴스 변수

# 여러 Counter 객체 생성
counter1 = Counter("첫번째")
counter2 = Counter("두번째")

counter1.increment()
counter1.increment()
counter2.increment()

print(f"{counter1.name} 카운트: {counter1.count}")  # 출력: 첫번째 카운트: 2
print(f"{counter2.name} 카운트: {counter2.count}")  # 출력: 두번째 카운트: 1
print(f"전체 Counter 개수: {Counter.total}")  # 출력: 전체 Counter 개수: 2


# ============================================
# 3. 데코레이터 기본 개념
# ============================================

# 데코레이터: 함수를 꾸며주는 함수
def my_decorator(func):
    """함수를 꾸며주는 데코레이터"""
    def wrapper():
        print("=== 함수 실행 전 ===")
        func()  # 원래 함수 실행
        print("=== 함수 실행 후 ===")
    return wrapper

# @ 문법으로 데코레이터 사용
@my_decorator
def say_hello():
    print("안녕하세요!")

say_hello()
# 출력:
# === 함수 실행 전 ===
# 안녕하세요!
# === 함수 실행 후 ===


# ============================================
# 4. FastAPI에서의 데코레이터 (미리보기)
# ============================================

# FastAPI에서는 이렇게 사용합니다!
# @app.get("/users")  # ← 이게 데코레이터!
# def get_users():
#     return {"users": ["Alice", "Bob"]}

# 간단한 시뮬레이션
class FakeApp:
    """FastAPI app 흉내"""
    def get(self, path: str):
        """@app.get() 데코레이터"""
        def decorator(func):
            print(f"경로 '{path}'에 함수 '{func.__name__}' 등록!")
            return func
        return decorator

app = FakeApp()

@app.get("/users")
def get_users():
    return {"users": ["Alice", "Bob"]}

# 출력: 경로 '/users'에 함수 'get_users' 등록!


# ============================================
# 5. @property 데코레이터
# ============================================

class User:
    """@property 사용 예제"""
    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name  # private 변수 (관례적 표기)
        self._last_name = last_name
    
    @property
    def full_name(self) -> str:
        """메서드를 속성처럼 사용 가능!"""
        return f"{self._first_name} {self._last_name}"
    
    @property
    def name(self) -> str:
        """이름 반환"""
        return self._first_name

user = User("홍", "길동")
print(user.full_name)  # 출력: 홍 길동 (메서드인데 () 없이 호출!)
print(user.name)  # 출력: 홍


print("\n=== 모든 예제 실행 완료! ===")
