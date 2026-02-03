# 2_practice.py

"""
Day 4 - 5교시: 가변 인수 + 언패킹 통합
Practice (강사와 함께 실습)

학습 목표:
- *args로 합계 함수 만들기
- **kwargs로 로그 함수 만들기
- 딕셔너리 언패킹으로 설정 병합하기
"""

# ============================================
# 실습 1: *args로 합계 함수 만들기
# ============================================

# 여러 개의 숫자를 받아 합계를 반환하는 함수
def calculate_sum(*numbers):
    """모든 숫자의 합계를 계산"""
    total = 0
    for num in numbers:
        total += num
    return total

# 테스트
print(calculate_sum(1, 2, 3, 4, 5))  # 출력: 15
print(calculate_sum(10, 20))  # 출력: 30
print(calculate_sum(100))  # 출력: 100


# ============================================
# 실습 2: **kwargs로 로그 함수 만들기 (TODO)
# ============================================

# TODO: **kwargs를 사용하여 로그 정보를 출력하는 함수를 작성하세요
# 함수 이름: log_info
# 기능: 받은 모든 키워드 인수를 "키: 값" 형식으로 출력

def log_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 테스트
print("=== 로그 정보 ===")
log_info(user="홍길동", action="로그인", timestamp="2026-02-03 10:30:00")
# 출력:
# user: 홍길동
# action: 로그인
# timestamp: 2026-02-03 10:30:00


# ============================================
# 실습 3: 리스트 언패킹 (TODO)
# ============================================

# 주어진 데이터
scores = [85, 90, 78, 92, 88]

# TODO: scores 리스트를 언패킹하여 calculate_sum 함수로 전달하고
# 총점을 계산하세요
total_score = calculate_sum(*scores)

print(f"\n총점: {total_score}")  # 출력: 총점: 433


# ============================================
# 실습 4: 딕셔너리 병합 (언패킹) (TODO)
# ============================================

# 기본 설정
default_settings = {
    "theme": "light",
    "language": "ko",
    "notifications": True
}

# 사용자 설정
user_settings = {
    "theme": "dark",
    "font_size": 14
}

# TODO: 딕셔너리 언패킹을 사용하여 두 설정을 병합하세요
# 힌트: {**default_settings, **user_settings}
# 같은 키가 있으면 나중 값(user_settings)이 우선됩니다
final_settings = {**default_settings, **user_settings}

print("\n최종 설정:", final_settings)
# 출력: 최종 설정: {'theme': 'dark', 'language': 'ko', 'notifications': True, 'font_size': 14}


# ============================================
# 실습 5: *args와 **kwargs 조합 (TODO)
# ============================================

# TODO: *args와 **kwargs를 모두 받는 함수를 작성하세요
# 함수 이름: create_product
# 기능:
#   - *args: 태그들 (문자열)
#   - **kwargs: 상품 정보 (이름, 가격 등)
#   - 딕셔너리를 반환하되 tags 키에 args를 리스트로 저장

def create_product(*tags, **product_info):
    # 상품 정보 딕셔너리 생성
    product = {
        "tags": list(tags),  # 튜플을 리스트로 변환
        **product_info  # 나머지 정보 병합
    }
    return product

# 테스트
product = create_product(
    "전자제품", "할인", "베스트",
    name="무선 이어폰",
    price=89000,
    brand="테크"
)

print("\n생성된 상품:", product)
# 출력: 생성된 상품: {'tags': ['전자제품', '할인', '베스트'], 'name': '무선 이어폰', 'price': 89000, 'brand': '테크'}
