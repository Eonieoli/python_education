# 2_practice.py

"""
Day 4 - 4교시: 키워드 인수 + None 처리
Practice (강사와 함께 실습)

학습 목표:
- 키워드 인수로 함수 호출하기
- None을 활용한 선택적 매개변수 작성하기
- API 스타일 함수 작성하기
"""

# ============================================
# 실습 1: 키워드 인수 기본 (전체 타이핑)
# ============================================

def send_email(to, subject, body, cc=None):
    """이메일 전송 함수 - 키워드 인수 연습"""
    message = f"받는사람: {to}\n제목: {subject}\n내용: {body}"
    
    if cc is not None:
        message += f"\n참조: {cc}"
    
    return message

# 키워드 인수로 명확하게 호출
result = send_email(
    to="user@example.com",
    subject="회의 안내",
    body="내일 오후 2시 회의실 A에서 회의가 있습니다"
)
print(result)


# ============================================
# 실습 2: None으로 선택적 매개변수 (TODO)
# ============================================

# TODO: 상품 정보를 생성하는 함수를 작성하세요
# 함수명: create_product
# 매개변수: name, price, description (기본값 None)
# 반환: 딕셔너리 (name, price, description)
# - description이 None이면 "설명 없음"으로 설정
def create_product(name, price, description=None):
    if description is None:
        description = "설명 없음"
    
    return {
        "name": name,
        "price": price,
        "description": description
    }

# 테스트
product1 = create_product("노트북", 1500000)
print(product1)  # 출력: {'name': '노트북', 'price': 1500000, 'description': '설명 없음'}

product2 = create_product("마우스", 35000, description="무선 마우스")
print(product2)  # 출력: {'name': '마우스', 'price': 35000, 'description': '무선 마우스'}


# ============================================
# 실습 3: API 스타일 함수 (TODO)
# ============================================

# TODO: 사용자 검색 함수를 작성하세요
# 함수명: search_users
# 매개변수: 
#   - keyword: 검색 키워드 (필수)
#   - age_min: 최소 나이 (기본값 None)
#   - age_max: 최대 나이 (기본값 None)
#   - city: 도시 (기본값 None)
# 반환: 검색 조건을 문자열로 반환
def search_users(keyword, age_min=None, age_max=None, city=None):
    conditions = [f"검색어: {keyword}"]
    
    if age_min is not None:
        conditions.append(f"최소나이: {age_min}세")
    
    if age_max is not None:
        conditions.append(f"최대나이: {age_max}세")
    
    if city is not None:
        conditions.append(f"지역: {city}")
    
    return ", ".join(conditions)

# 테스트
result1 = search_users(keyword="개발자")
print(result1)  # 출력: 검색어: 개발자

result2 = search_users(keyword="개발자", age_min=25)
print(result2)  # 출력: 검색어: 개발자, 최소나이: 25세

result3 = search_users(keyword="개발자", age_min=25, age_max=35, city="서울")
print(result3)  # 출력: 검색어: 개발자, 최소나이: 25세, 최대나이: 35세, 지역: 서울
