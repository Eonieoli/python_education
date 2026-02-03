# 1_basic.py

"""
Day 4 - 3교시: 매개변수 - 위치와 기본값
Basic (강사 시연용)

학습 목표:
- 위치 인수(positional arguments) 이해
- 기본값(default values) 설정 방법
- 위치 인수와 기본값 조합하기
- 실전에서 기본값 활용하기
"""

# ============================================
# 1. 위치 인수 (Positional Arguments)
# ============================================

# 함수를 호출할 때 인수는 순서대로 매개변수에 전달됩니다
def introduce(name, age):
    return f"제 이름은 {name}이고, {age}살입니다."

# 위치 인수로 호출
result = introduce("김철수", 25)
print(result)  # 출력: 제 이름은 김철수이고, 25살입니다.

# 순서가 중요합니다!
# result = introduce(25, "김철수")  # 순서가 바뀌면 이상한 결과가 나옵니다


# ============================================
# 2. 기본값 - 숫자
# ============================================

# 매개변수에 기본값을 설정할 수 있습니다
def calculate_price(price, tax_rate=0.1):
    """
    상품 가격 계산 함수
    tax_rate 기본값: 0.1 (10%)
    """
    return int(price * (1 + tax_rate))

# 기본값 사용 (tax_rate 생략)
total1 = calculate_price(10000)
print(f"세금 포함 가격: {total1}원")  # 출력: 세금 포함 가격: 11000원

# 기본값 대신 다른 값 전달
total2 = calculate_price(10000, 0.05)
print(f"세금 포함 가격: {total2}원")  # 출력: 세금 포함 가격: 10500원


# ============================================
# 3. 기본값 - 문자열
# ============================================

def greet(name, greeting="안녕하세요"):
    """
    인사 함수
    greeting 기본값: "안녕하세요"
    """
    return f"{greeting}, {name}님!"

# 기본값 사용
message1 = greet("홍길동")
print(message1)  # 출력: 안녕하세요, 홍길동님!

# 다른 인사말 사용
message2 = greet("이영희", "반갑습니다")
print(message2)  # 출력: 반갑습니다, 이영희님!


# ============================================
# 4. 위치 인수와 기본값 조합
# ============================================

def create_user_profile(name, age, city="서울", hobby="독서"):
    """
    사용자 프로필 생성
    - name, age: 필수 매개변수 (기본값 없음)
    - city, hobby: 선택 매개변수 (기본값 있음)
    """
    return f"{name}({age}세)는 {city}에 살며 {hobby}를 좋아합니다."

# 필수 인수만 전달
profile1 = create_user_profile("박민수", 30)
print(profile1)  # 출력: 박민수(30세)는 서울에 살며 독서를 좋아합니다.

# 일부 기본값 변경
profile2 = create_user_profile("최지은", 25, "부산")
print(profile2)  # 출력: 최지은(25세)는 부산에 살며 독서를 좋아합니다.

# 모든 인수 전달
profile3 = create_user_profile("정우성", 28, "인천", "운동")
print(profile3)  # 출력: 정우성(28세)는 인천에 살며 운동을 좋아합니다.


# ============================================
# 5. 실전 예제: 할인 계산 함수
# ============================================

def calculate_discount(price, quantity, discount_rate=0.0, member_discount=0.0):
    """
    할인 적용 가격 계산
    - price: 상품 가격
    - quantity: 수량
    - discount_rate: 일반 할인율 (기본값: 0.0)
    - member_discount: 회원 할인율 (기본값: 0.0)
    """
    # 소계
    subtotal = price * quantity
    
    # 일반 할인 적용
    after_discount = subtotal * (1 - discount_rate)
    
    # 회원 할인 추가 적용
    final_price = after_discount * (1 - member_discount)
    
    return int(final_price)

# 할인 없이 구매
price1 = calculate_discount(10000, 3)
print(f"할인 없음: {price1}원")  # 출력: 할인 없음: 30000원

# 20% 할인만 적용
price2 = calculate_discount(10000, 3, 0.2)
print(f"20% 할인: {price2}원")  # 출력: 20% 할인: 24000원

# 20% 할인 + 10% 회원 할인
price3 = calculate_discount(10000, 3, 0.2, 0.1)
print(f"20% + 회원 10%: {price3}원")  # 출력: 20% + 회원 10%: 21600원
