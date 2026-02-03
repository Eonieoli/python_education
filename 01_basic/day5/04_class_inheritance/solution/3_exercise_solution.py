# 3_exercise_solution.py

"""
Day 5 - 4교시: 클래스 상속 기초
Exercise - 직원 관리 시스템 (정답)
"""

from pydantic import BaseModel

# ============================================
# 정답 1: Employee 클래스
# ============================================

class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary
    
    def get_info(self) -> str:
        return f"직원: {self.name}, 급여: {self.salary}원"


# ============================================
# 정답 2: Manager 클래스 (Employee 상속)
# ============================================

class Manager(Employee):  # Employee 상속
    def __init__(self, name: str, salary: int, team_size: int):
        # 부모의 속성 초기화
        self.name = name
        self.salary = salary
        # 추가 속성
        self.team_size = team_size
    
    def get_info(self) -> str:  # 메서드 오버라이딩
        return f"관리자: {self.name}, 급여: {self.salary}원, 팀원: {self.team_size}명"


# ============================================
# 정답 3: Pydantic 상속 - 상품 모델
# ============================================

class ProductBase(BaseModel):
    name: str
    price: int

class ProductDetail(ProductBase):  # ProductBase 상속
    description: str
    stock: int


# ============================================
# 테스트 코드
# ============================================

if __name__ == "__main__":
    # 직원 테스트
    emp = Employee("김철수", 3000000)
    print(emp.get_info())  # 출력: 직원: 김철수, 급여: 3000000원
    
    # 관리자 테스트
    mgr = Manager("이영희", 5000000, 5)
    print(mgr.get_info())  # 출력: 관리자: 이영희, 급여: 5000000원, 팀원: 5명
    
    # Pydantic 모델 테스트
    product = ProductDetail(
        name="노트북",
        price=1500000,
        description="고성능 노트북",
        stock=10
    )
    print(product)
    # 출력: name='노트북' price=1500000 description='고성능 노트북' stock=10
