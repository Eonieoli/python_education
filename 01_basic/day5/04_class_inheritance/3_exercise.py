# 3_exercise.py

"""
Day 5 - 4교시: 클래스 상속 기초
Exercise - 직원 관리 시스템

문제:
회사의 직원 관리 시스템을 클래스 상속으로 구현하세요.

요구사항:
1. Employee (직원) 클래스 작성
   - 속성: name (str), salary (int)
   - 메서드: get_info() -> str (이름과 급여 정보 반환)

2. Manager (관리자) 클래스 작성 (Employee 상속)
   - 추가 속성: team_size (int) - 팀 인원 수
   - 메서드 오버라이딩: get_info() -> str (관리자 정보 포함)

출력 예시:
직원: 김철수, 급여: 3000000원
관리자: 이영희, 급여: 5000000원, 팀원: 5명
"""

from pydantic import BaseModel

# ============================================
# TODO 1: Employee 클래스 작성
# ============================================

# TODO: Employee 클래스를 작성하세요
# __init__: name (str), salary (int)
# get_info(): 이름과 급여를 반환
class Employee:
    pass  # 이 줄을 삭제하고 코드를 작성하세요


# ============================================
# TODO 2: Manager 클래스 작성 (Employee 상속)
# ============================================

# TODO: Manager 클래스를 작성하세요 (Employee 상속)
# __init__: name, salary, team_size (int)
# get_info(): 오버라이딩하여 관리자 정보 반환
class Manager:
    pass  # 이 줄을 삭제하고 코드를 작성하세요


# ============================================
# TODO 3: Pydantic 상속 - 상품 모델
# ============================================

# TODO: ProductBase 클래스를 작성하세요
# 필드: name (str), price (int)
class ProductBase:
    pass  # 이 줄을 삭제하고 코드를 작성하세요

# TODO: ProductDetail 클래스를 작성하세요 (ProductBase 상속)
# 추가 필드: description (str), stock (int)
class ProductDetail:
    pass  # 이 줄을 삭제하고 코드를 작성하세요


# ============================================
# 테스트 코드 (수정하지 마세요)
# ============================================

if __name__ == "__main__":
    # 직원 테스트
    emp = Employee("김철수", 3000000)
    print(emp.get_info())
    
    # 관리자 테스트
    mgr = Manager("이영희", 5000000, 5)
    print(mgr.get_info())
    
    # Pydantic 모델 테스트
    product = ProductDetail(
        name="노트북",
        price=1500000,
        description="고성능 노트북",
        stock=10
    )
    print(product)
