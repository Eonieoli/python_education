# 1_basic.py

"""
Day 5 - 4교시: 클래스 상속 기초
Basic (강사 시연용)

학습 목표:
- 상속의 개념과 필요성 이해
- 부모 클래스와 자식 클래스 작성
- 메서드 오버라이딩
- Pydantic BaseModel 상속 패턴 미리보기
"""

# ============================================
# 1. 간단한 상속 - Animal과 Dog
# ============================================

# 부모 클래스 (Animal)
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def speak(self) -> str:
        return "Some sound"

# 자식 클래스 (Dog) - Animal을 상속
class Dog(Animal):  # 괄호 안에 부모 클래스 이름
    def speak(self) -> str:  # 메서드 오버라이딩!
        return "Woof!"

# 자식 클래스 (Cat) - Animal을 상속
class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

# 사용 예제
dog = Dog("멍멍이")
print(dog.name)    # 출력: 멍멍이 (부모 클래스의 속성 사용)
print(dog.speak()) # 출력: Woof! (자식 클래스에서 오버라이딩한 메서드)

cat = Cat("야옹이")
print(cat.name)    # 출력: 야옹이
print(cat.speak()) # 출력: Meow!


# ============================================
# 2. Pydantic BaseModel 상속 패턴
# ============================================

# Pydantic을 FastAPI에서 이렇게 사용합니다!
from pydantic import BaseModel

# 기본 User 모델 (공통 필드)
class UserBase(BaseModel):
    email: str
    name: str

# 회원가입용 모델 (비밀번호 추가)
class UserCreate(UserBase):  # UserBase 상속
    password: str  # 추가 필드

# 응답용 모델 (id 추가, 비밀번호 제외)
class UserResponse(UserBase):  # UserBase 상속
    id: int  # 추가 필드

# 사용 예제
# 회원가입 데이터 (비밀번호 포함)
new_user = UserCreate(
    email="alice@example.com",
    name="Alice",
    password="secret123"
)
print(new_user)
# 출력: email='alice@example.com' name='Alice' password='secret123'

# API 응답 데이터 (비밀번호 제외, id 포함)
user_response = UserResponse(
    email="alice@example.com",
    name="Alice",
    id=1
)
print(user_response)
# 출력: email='alice@example.com' name='Alice' id=1
