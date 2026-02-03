"""
Day 5 - 07교시: import 완전 정복
Basic 단계 - typing import 복습

학습 목표:
1. typing 모듈이 뭔지 이해
2. List, Dict, Optional, Union 타입 복습
3. 어제 배운 타입 힌트와 연결
"""

# ===== typing 모듈 import =====
print("=" * 50)
print("typing 모듈 import")
print("=" * 50)
print("""
어제 타입 힌트 배울 때 이거 썼죠?
from typing import List, Dict, Optional, Union

typing은 Python 내장 모듈이에요 (설치 안 해도 됨!)
타입 힌트를 위한 도구들을 제공합니다.
""")

from typing import List, Dict, Optional, Union


# ===== 1. List 타입 =====
print("\n" + "=" * 50)
print("1. List 타입 힌트")
print("=" * 50)

def get_student_names(students: List[str]) -> List[str]:
    """학생 이름 목록을 받아서 대문자로 변환"""
    return [name.upper() for name in students]

def sum_numbers(numbers: List[int]) -> int:
    """정수 리스트의 합계"""
    return sum(numbers)

# 사용 예시
students = ["alice", "bob", "charlie"]
print(f"원본: {students}")
print(f"대문자 변환: {get_student_names(students)}")

scores = [85, 90, 78, 92, 88]
print(f"\n점수 목록: {scores}")
print(f"총점: {sum_numbers(scores)}")


# ===== 2. Dict 타입 =====
print("\n" + "=" * 50)
print("2. Dict 타입 힌트")
print("=" * 50)

def create_user_profile(name: str, age: int) -> Dict[str, Union[str, int]]:
    """사용자 프로필 딕셔너리 생성"""
    return {
        "name": name,
        "age": age,
        "status": "active"
    }

def get_user_info() -> Dict[str, str]:
    """문자열로만 이루어진 사용자 정보"""
    return {
        "name": "Alice",
        "email": "alice@example.com",
        "role": "admin"
    }

# 사용 예시
profile = create_user_profile("Bob", 25)
print(f"프로필: {profile}")

info = get_user_info()
print(f"사용자 정보: {info}")


# ===== 3. Optional 타입 (중요!) =====
print("\n" + "=" * 50)
print("3. Optional 타입 (None을 반환할 수 있음!)")
print("=" * 50)

def find_user(user_id: int) -> Optional[Dict[str, str]]:
    """
    사용자를 찾아서 반환
    못 찾으면 None 반환!
    """
    # 간단한 예시용 데이터
    users = {
        1: {"name": "Alice", "email": "alice@example.com"},
        2: {"name": "Bob", "email": "bob@example.com"}
    }
    
    return users.get(user_id)  # 없으면 None

def get_email(user_id: int) -> Optional[str]:
    """사용자 이메일 반환, 없으면 None"""
    user = find_user(user_id)
    if user:
        return user["email"]
    return None

# 사용 예시
user1 = find_user(1)
print(f"사용자 1: {user1}")

user999 = find_user(999)
print(f"사용자 999: {user999}")  # None

email = get_email(1)
print(f"이메일: {email}")


# ===== 4. Union 타입 =====
print("\n" + "=" * 50)
print("4. Union 타입 (여러 타입 중 하나)")
print("=" * 50)

def process_value(value: Union[int, str]) -> str:
    """
    정수 또는 문자열을 받아서 처리
    """
    if isinstance(value, int):
        return f"숫자입니다: {value * 2}"
    else:
        return f"문자열입니다: {value.upper()}"

# 사용 예시
print(process_value(10))
print(process_value("hello"))


# ===== 5. 복합 타입 (실전!) =====
print("\n" + "=" * 50)
print("5. 복합 타입 조합 (실전 예시)")
print("=" * 50)

def get_product_list(
    category: str,
    max_price: Optional[int] = None
) -> List[Dict[str, Union[str, int]]]:
    """
    카테고리별 상품 목록 반환
    max_price가 있으면 그 이하만
    """
    # 예시 데이터
    all_products = [
        {"name": "노트북", "category": "전자제품", "price": 1500000},
        {"name": "키보드", "category": "전자제품", "price": 150000},
        {"name": "책상", "category": "가구", "price": 300000},
        {"name": "의자", "category": "가구", "price": 200000},
    ]
    
    # 카테고리 필터링
    filtered = [p for p in all_products if p["category"] == category]
    
    # 가격 필터링 (Optional이므로 None 체크!)
    if max_price is not None:
        filtered = [p for p in filtered if p["price"] <= max_price]
    
    return filtered

# 사용 예시
print("전자제품 전체:")
print(get_product_list("전자제품"))

print("\n전자제품 중 50만원 이하:")
print(get_product_list("전자제품", 500000))


# ===== 학습 정리 =====
print("\n" + "=" * 50)
print("학습 정리")
print("=" * 50)
print("""
typing 모듈에서 가져오는 주요 타입들:

1. List[타입]: 리스트의 원소 타입 지정
   예) List[int], List[str]

2. Dict[키타입, 값타입]: 딕셔너리의 키와 값 타입 지정
   예) Dict[str, int], Dict[str, str]

3. Optional[타입]: None을 반환할 수 있는 함수
   예) Optional[str], Optional[Dict[str, str]]
   → 실무에서 매우 자주 사용!

4. Union[타입1, 타입2]: 여러 타입 중 하나
   예) Union[int, str], Union[List[int], Dict[str, int]]

왜 typing을 쓰나요?
- FastAPI에서 Request/Response 모델 만들 때 필수!
- Pydantic BaseModel에서 필드 타입 지정할 때 사용
- 코드 가독성과 IDE 자동완성에 도움
""")
