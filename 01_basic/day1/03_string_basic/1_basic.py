# 1_basic.py

"""
Day 1 - 3교시: 문자열 기본
Basic (강사 시연용)

학습 목표:
- 문자열 개념과 생성 방법 이해
- 문자열 연산 (+, *) 활용
- len() 함수로 문자열 길이 구하기
- 실전 예제로 문자열 다루기
"""

# ============================================
# 1. 문자열 생성 - 작은따옴표 vs 큰따옴표
# ============================================

# 문자열은 텍스트 데이터를 저장하는 자료형입니다
# 작은따옴표(')나 큰따옴표(") 둘 다 사용 가능합니다

name1 = 'Alice'
name2 = "Bob"

print(name1)  # 출력: Alice
print(name2)  # 출력: Bob

# 문자열 안에 따옴표를 포함하려면 다른 종류의 따옴표를 사용하세요
message1 = "He said, 'Hello!'"
message2 = 'She said, "Hi!"'

print(message1)  # 출력: He said, 'Hello!'
print(message2)  # 출력: She said, "Hi!"


# ============================================
# 2. 문자열 연산 - 덧셈(+)으로 합치기
# ============================================

# + 연산자로 문자열을 연결(concatenation)할 수 있습니다
first_name = "홍"
last_name = "길동"
full_name = first_name + last_name

print(full_name)  # 출력: 홍길동

# 문자열 사이에 공백을 넣으려면 공백 문자를 추가하세요
greeting = "안녕하세요, " + full_name + "님!"
print(greeting)  # 출력: 안녕하세요, 홍길동님!


# ============================================
# 3. 문자열 연산 - 곱셈(*)으로 반복하기
# ============================================

# * 연산자로 문자열을 반복할 수 있습니다
star = "*"
line = star * 10

print(line)  # 출력: **********

# 여러 글자도 반복 가능합니다
pattern = "==" * 5
print(pattern)  # 출력: ==========

# 실전 예제: 구분선 만들기
separator = "-" * 20
print(separator)  # 출력: --------------------


# ============================================
# 4. len() 함수 - 문자열 길이 구하기
# ============================================

# len() 함수는 문자열의 길이(글자 수)를 반환합니다
message = "Hello"
length = len(message)

print(message)  # 출력: Hello
print(length)  # 출력: 5

# 한글도 똑같이 계산됩니다 (1글자 = 1)
korean = "안녕하세요"
print(len(korean))  # 출력: 5

# 공백도 글자 수에 포함됩니다
sentence = "Hello World"
print(len(sentence))  # 출력: 11 (공백 포함)


# ============================================
# 5. 실전 예제: 상품 정보 표시
# ============================================

# 상품 이름과 설명을 문자열로 관리
product_name = "노트북"
brand = "삼성"
model = "갤럭시북"

# 문자열 연산으로 상품 정보 조합
full_product = brand + " " + model + " " + product_name
print(full_product)  # 출력: 삼성 갤럭시북 노트북

# 구분선으로 보기 좋게 표시
separator = "=" * 30
print(separator)  # 출력: ==============================
print(full_product)
print(separator)

# 상품명 길이 확인
name_length = len(full_product)
print(f"상품명 길이: {name_length}글자")  # 출력: 상품명 길이: 13글자
