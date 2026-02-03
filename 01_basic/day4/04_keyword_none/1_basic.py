# 1_basic.py

"""
Day 4 - 4교시: 키워드 인수 + None 처리
Basic (강사 시연용)

학습 목표:
- 키워드 인수 사용법 이해하기
- None을 활용한 선택적 매개변수 패턴
- FastAPI 쿼리 파라미터 스타일 미리보기
"""

# ============================================
# 1. 키워드 인수 기본
# ============================================

def introduce(name, age, city):
    """키워드 인수로 호출할 수 있는 함수"""
    return f"{name}님은 {age}세이고 {city}에 살고 있습니다"

# 위치 인수로 호출
result1 = introduce("홍길동", 25, "서울")
print(result1)  # 출력: 홍길동님은 25세이고 서울에 살고 있습니다

# 키워드 인수로 호출 - 순서를 바꿔도 됨!
result2 = introduce(city="부산", name="김철수", age=30)
print(result2)  # 출력: 김철수님은 30세이고 부산에 살고 있습니다


# ============================================
# 2. 위치 인수와 키워드 인수 혼합
# ============================================

def create_profile(name, age, email="미입력", phone="미입력"):
    """일부는 위치, 일부는 키워드 인수로 호출"""
    return f"이름: {name}, 나이: {age}, 이메일: {email}, 전화번호: {phone}"

# 필수 매개변수는 위치로, 선택 매개변수는 키워드로
result3 = create_profile("이영희", 28, email="young@example.com")
print(result3)  # 출력: 이름: 이영희, 나이: 28, 이메일: young@example.com, 전화번호: 미입력

# 모두 키워드로 호출 (가장 명확!)
result4 = create_profile(name="박민수", age=35, email="park@example.com", phone="010-1234-5678")
print(result4)  # 출력: 이름: 박민수, 나이: 35, 이메일: park@example.com, 전화번호: 010-1234-5678


# ============================================
# 3. None 기본값 패턴 - 선택적 매개변수
# ============================================

def create_user(name, bio=None):
    """bio가 None이면 기본값을 설정하는 패턴"""
    # None 체크 후 기본값 설정
    if bio is None:
        bio = "소개가 없습니다"
    
    return {
        "name": name,
        "bio": bio
    }

# bio를 제공하지 않으면 None이 전달됨
user1 = create_user("홍길동")
print(user1)  # 출력: {'name': '홍길동', 'bio': '소개가 없습니다'}

# bio를 제공하면 그 값이 사용됨
user2 = create_user("김철수", bio="Python 개발자입니다")
print(user2)  # 출력: {'name': '김철수', 'bio': 'Python 개발자입니다'}


# ============================================
# 4. None 처리 - 값 없음 표현
# ============================================

def get_user_by_id(user_id, default=None):
    """사용자를 찾지 못하면 None 또는 default를 반환"""
    # 간단한 사용자 데이터베이스
    users = {
        1: "홍길동",
        2: "김철수",
        3: "이영희"
    }
    
    # 사용자가 없으면 default 반환
    if user_id not in users:
        return default
    
    return users[user_id]

# 사용자를 찾으면 이름 반환
result5 = get_user_by_id(1)
print(f"사용자 1: {result5}")  # 출력: 사용자 1: 홍길동

# 사용자를 못 찾으면 None 반환
result6 = get_user_by_id(999)
print(f"사용자 999: {result6}")  # 출력: 사용자 999: None

# 사용자를 못 찾으면 기본값 반환
result7 = get_user_by_id(999, default="알 수 없는 사용자")
print(f"사용자 999: {result7}")  # 출력: 사용자 999: 알 수 없는 사용자


# ============================================
# 5. FastAPI 스타일 - API 매개변수 패턴
# ============================================

def search_products(keyword, min_price=None, max_price=None):
    """FastAPI 쿼리 파라미터처럼 동작하는 함수"""
    # 검색 조건 문자열 생성
    conditions = [f"키워드: {keyword}"]
    
    if min_price is not None:
        conditions.append(f"최소가격: {min_price}원")
    
    if max_price is not None:
        conditions.append(f"최대가격: {max_price}원")
    
    return ", ".join(conditions)

# 키워드만 검색
result8 = search_products(keyword="노트북")
print(result8)  # 출력: 키워드: 노트북

# 키워드 + 최소가격
result9 = search_products(keyword="노트북", min_price=500000)
print(result9)  # 출력: 키워드: 노트북, 최소가격: 500000원

# 키워드 + 최소가격 + 최대가격
result10 = search_products(keyword="노트북", min_price=500000, max_price=1500000)
print(result10)  # 출력: 키워드: 노트북, 최소가격: 500000원, 최대가격: 1500000원

# FastAPI에서 이렇게 사용됩니다:
# @app.get("/products")
# def search(keyword, min_price=None, max_price=None):
#     ...
