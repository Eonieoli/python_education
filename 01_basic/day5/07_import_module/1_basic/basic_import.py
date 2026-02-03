"""
Day 5 - 07교시: import 완전 정복
Basic 단계 - 표준 라이브러리 import 시연

학습 목표:
1. import 기본 문법 이해
2. from import 사용법
3. 별칭(as) 사용법
4. 표준 라이브러리 활용
"""

# ===== 1. import 기본 =====
print("=" * 50)
print("1. import 기본")
print("=" * 50)

# json 모듈 전체를 import
import json

# 딕셔너리를 JSON 문자열로 변환
user_data = {"name": "Alice", "age": 25, "email": "alice@example.com"}
json_string = json.dumps(user_data, indent=2)
print("JSON 문자열:")
print(json_string)

# JSON 문자열을 딕셔너리로 변환
parsed_data = json.loads(json_string)
print("\n파싱된 데이터:", parsed_data)
print("이름:", parsed_data["name"])


# ===== 2. from import (특정 함수만 가져오기) =====
print("\n" + "=" * 50)
print("2. from import (특정 함수만 가져오기)")
print("=" * 50)

# json 모듈에서 dumps와 loads만 가져오기
from json import dumps, loads

# 이제 json. 없이 바로 사용 가능!
product = {"name": "노트북", "price": 1500000, "stock": 10}
product_json = dumps(product, ensure_ascii=False, indent=2)  # json.dumps 대신 dumps
print("상품 JSON:")
print(product_json)


# ===== 3. 별칭(as) 사용 =====
print("\n" + "=" * 50)
print("3. 별칭(as) 사용")
print("=" * 50)

# math 모듈을 m이라는 짧은 이름으로 import
import math as m

# m.함수() 형태로 사용
radius = 5
area = m.pi * m.pow(radius, 2)  # π * r²
print(f"반지름 {radius}인 원의 넓이: {area:.2f}")
print(f"π 값: {m.pi:.4f}")
print(f"5의 제곱근: {m.sqrt(25)}")


# ===== 4. 표준 라이브러리 - datetime =====
print("\n" + "=" * 50)
print("4. 표준 라이브러리 - datetime")
print("=" * 50)

from datetime import datetime, timedelta

# 현재 시각
now = datetime.now()
print(f"현재 시각: {now}")
print(f"포맷팅: {now.strftime('%Y년 %m월 %d일 %H:%M:%S')}")

# 3일 후
after_3days = now + timedelta(days=3)
print(f"3일 후: {after_3days.strftime('%Y-%m-%d')}")

# 날짜 차이 계산
birthday = datetime(2024, 12, 25)
days_until = (birthday - now).days
print(f"크리스마스까지 {days_until}일 남았습니다")


# ===== 5. 표준 라이브러리 - random =====
print("\n" + "=" * 50)
print("5. 표준 라이브러리 - random")
print("=" * 50)

import random

# 랜덤 정수
dice = random.randint(1, 6)
print(f"주사위 결과: {dice}")

# 리스트에서 랜덤 선택
fruits = ["사과", "바나나", "오렌지", "포도", "딸기"]
selected = random.choice(fruits)
print(f"선택된 과일: {selected}")

# 리스트 섞기
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"섞인 숫자: {numbers}")

# 랜덤 샘플 (중복 없이 여러 개 선택)
winners = random.sample(fruits, 2)
print(f"당첨자 2명: {winners}")


# ===== 실행 결과 설명 =====
print("\n" + "=" * 50)
print("학습 정리")
print("=" * 50)
print("""
1. import 모듈명: 모듈 전체를 가져옴 (모듈명.함수() 형태로 사용)
2. from 모듈명 import 함수명: 특정 함수만 가져옴 (함수() 직접 사용)
3. import 모듈명 as 별칭: 긴 이름을 짧게 (별칭.함수() 형태로 사용)
4. Python 표준 라이브러리는 설치 없이 바로 사용 가능!
   - json: JSON 데이터 처리
   - math: 수학 함수
   - datetime: 날짜/시간 처리
   - random: 랜덤 값 생성
""")
