# 1_basic.py

"""
Day 4 - 5교시: 가변 인수 + 언패킹 통합
Basic (강사 시연용)

학습 목표:
- *args로 여러 개 인수 받기
- **kwargs로 키워드 인수들 받기
- 리스트/딕셔너리 언패킹
- FastAPI에서의 활용 이해
"""

# ============================================
# 1. *args - 여러 개의 인수 받기
# ============================================

# *args는 여러 개의 인수를 튜플로 받습니다
def add_all(*args):
    """모든 숫자를 더하는 함수"""
    print("받은 인수들:", args)  # 튜플로 출력
    total = 0
    for num in args:
        total += num
    return total

# 인수 개수에 상관없이 호출 가능
print(add_all(1, 2, 3))  # 출력: 6
print(add_all(10, 20, 30, 40, 50))  # 출력: 150
print(add_all(5))  # 출력: 5


# ============================================
# 2. **kwargs - 키워드 인수들 받기
# ============================================

# **kwargs는 키워드 인수들을 딕셔너리로 받습니다
def print_user_info(**kwargs):
    """사용자 정보를 출력하는 함수"""
    print("받은 정보:", kwargs)  # 딕셔너리로 출력
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 키워드 인수를 자유롭게 전달
print_user_info(name="홍길동", age=25, city="서울")
# 출력:
# 받은 정보: {'name': '홍길동', 'age': 25, 'city': '서울'}
# name: 홍길동
# age: 25
# city: 서울

print()
print_user_info(email="test@example.com", phone="010-1234-5678")
# 출력:
# 받은 정보: {'email': 'test@example.com', 'phone': '010-1234-5678'}
# email: test@example.com
# phone: 010-1234-5678


# ============================================
# 3. 리스트 언패킹 (*list)
# ============================================

# 리스트를 개별 인수로 펼치기
numbers = [10, 20, 30]
print(add_all(*numbers))  # add_all(10, 20, 30)과 동일
# 출력: 60

# 여러 리스트 합치기
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, *list2]  # [1, 2, 3, 4, 5, 6]
print("합친 리스트:", combined)  # 출력: 합친 리스트: [1, 2, 3, 4, 5, 6]


# ============================================
# 4. 딕셔너리 언패킹 (**dict)
# ============================================

# 딕셔너리를 키워드 인수로 펼치기
user_data = {"name": "이영희", "age": 30, "city": "부산"}
print_user_info(**user_data)  # print_user_info(name="이영희", age=30, city="부산")과 동일
# 출력:
# 받은 정보: {'name': '이영희', 'age': 30, 'city': '부산'}
# name: 이영희
# age: 30
# city: 부산

# 딕셔너리 병합 (FastAPI 설정에서 자주 사용!)
default_config = {"timeout": 30, "retry": 3}
user_config = {"timeout": 60, "debug": True}
merged_config = {**default_config, **user_config}
print("\n병합된 설정:", merged_config)
# 출력: 병합된 설정: {'timeout': 60, 'retry': 3, 'debug': True}


# ============================================
# 5. *args와 **kwargs 조합
# ============================================

def flexible_function(*args, **kwargs):
    """위치 인수와 키워드 인수를 모두 받는 유연한 함수"""
    print("위치 인수:", args)
    print("키워드 인수:", kwargs)
    
flexible_function(1, 2, 3, name="홍길동", age=25)
# 출력:
# 위치 인수: (1, 2, 3)
# 키워드 인수: {'name': '홍길동', 'age': 25}


# ============================================
# 6. 실전 예제: 로그 함수
# ============================================

def log_message(level, *messages, **details):
    """로그 메시지를 출력하는 함수 (FastAPI 로깅 패턴)"""
    # 레벨 표시
    print(f"[{level}]", end=" ")
    
    # 모든 메시지 출력
    for msg in messages:
        print(msg, end=" ")
    print()  # 줄바꿈
    
    # 상세 정보 출력
    if details:
        print("  세부사항:", details)

# 다양한 방식으로 호출 가능
log_message("INFO", "사용자 로그인 성공")
# 출력: [INFO] 사용자 로그인 성공

log_message("ERROR", "데이터베이스", "연결 실패", error_code=500, retry=True)
# 출력:
# [ERROR] 데이터베이스 연결 실패
#   세부사항: {'error_code': 500, 'retry': True}


# ============================================
# 7. FastAPI 스타일 예제
# ============================================

def create_user(username, email, **extra_fields):
    """사용자 생성 함수 (FastAPI Pydantic 패턴 미리보기)"""
    user = {
        "username": username,
        "email": email,
        **extra_fields  # 추가 필드를 딕셔너리에 병합
    }
    return user

# 필수 필드 + 선택 필드
user1 = create_user("hong", "hong@example.com", age=25, city="서울")
print("\n생성된 사용자:", user1)
# 출력: 생성된 사용자: {'username': 'hong', 'email': 'hong@example.com', 'age': 25, 'city': '서울'}

user2 = create_user("kim", "kim@example.com", phone="010-1234-5678")
print("생성된 사용자:", user2)
# 출력: 생성된 사용자: {'username': 'kim', 'email': 'kim@example.com', 'phone': '010-1234-5678'}
