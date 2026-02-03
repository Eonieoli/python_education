# 3_exercise.py

"""
Day 4 - 5교시: 가변 인수 + 언패킹 통합
Exercise - 학생 독립 실습

문제 1: 유연한 계산기
문제 2: 설정 병합 시스템
"""

# ============================================
# Exercise 1: 유연한 계산기
# ============================================

"""
문제:
다양한 연산을 수행하는 계산기 함수를 작성하세요.

함수 이름: calculate
매개변수:
  - operation: 연산 종류 ("add", "multiply", "max", "min")
  - *numbers: 여러 개의 숫자

기능:
  - "add": 모든 숫자의 합
  - "multiply": 모든 숫자의 곱
  - "max": 가장 큰 숫자
  - "min": 가장 작은 숫자

출력 예시:
합계: 150
곱: 120
최댓값: 50
최솟값: 10
"""

# TODO: calculate 함수를 작성하세요
# 힌트 1: operation으로 연산 종류 판단 (if문)
# 힌트 2: *numbers로 여러 개 숫자 받기
# 힌트 3: for문으로 numbers 순회





# 테스트 코드
print("합계:", calculate("add", 10, 20, 30, 40, 50))  # 출력: 합계: 150
print("곱:", calculate("multiply", 2, 3, 4, 5))  # 출력: 곱: 120
print("최댓값:", calculate("max", 10, 25, 50, 30))  # 출력: 최댓값: 50
print("최솟값:", calculate("min", 10, 25, 50, 30))  # 출력: 최솟값: 10


# ============================================
# Exercise 2: 설정 병합 시스템
# ============================================

"""
문제:
여러 설정 딕셔너리를 병합하는 함수를 작성하세요.

함수 이름: merge_settings
매개변수:
  - **settings: 여러 개의 키워드 인수 (설정들)

기능:
  1. 시스템 기본 설정을 정의 (함수 내부)
     {"mode": "normal", "timeout": 30, "retry": 3}
  2. 받은 설정들을 기본 설정에 병합
  3. 병합된 설정 딕셔너리 반환

출력 예시:
병합된 설정: {'mode': 'advanced', 'timeout': 30, 'retry': 5, 'debug': True}
"""

# TODO: merge_settings 함수를 작성하세요
# 힌트 1: 함수 내부에서 기본 설정 딕셔너리 생성
# 힌트 2: {**기본설정, **받은설정} 패턴으로 병합
# 힌트 3: **kwargs로 키워드 인수들 받기




# 테스트 코드
result = merge_settings(mode="advanced", retry=5, debug=True)
print("\n병합된 설정:", result)
# 출력: 병합된 설정: {'mode': 'advanced', 'timeout': 30, 'retry': 5, 'debug': True}


# ============================================
# Exercise 3 (도전): API 요청 함수
# ============================================

"""
문제:
FastAPI 스타일의 유연한 API 요청 함수를 작성하세요.

함수 이름: api_request
매개변수:
  - method: HTTP 메서드 ("GET", "POST" 등)
  - url: 요청 URL
  - **params: 선택적 파라미터들 (headers, data, timeout 등)

기능:
  1. method와 url은 필수로 출력
  2. params가 있으면 "파라미터:" 라벨과 함께 출력
  3. 요청 정보를 담은 딕셔너리 반환

출력 예시:
메서드: POST
URL: /api/users
파라미터: {'headers': {'Authorization': 'Bearer token123'}, 'data': {'name': 'hong'}}
요청 정보: {'method': 'POST', 'url': '/api/users', 'headers': {'Authorization': 'Bearer token123'}, 'data': {'name': 'hong'}}
"""

# TODO: api_request 함수를 작성하세요
# 힌트 1: 일반 매개변수(method, url)와 **kwargs 조합
# 힌트 2: 딕셔너리 언패킹으로 반환값 구성




# 테스트 코드
request = api_request(
    "POST",
    "/api/users",
    headers={"Authorization": "Bearer token123"},
    data={"name": "hong"}
)
print("\n요청 정보:", request)
# 출력: 요청 정보: {'method': 'POST', 'url': '/api/users', 'headers': {...}, 'data': {...}}
