# 3_exercise_solution.py

"""
Day 4 - 5교시: 가변 인수 + 언패킹 통합
Exercise - 정답

문제 1: 유연한 계산기
문제 2: 설정 병합 시스템
문제 3: API 요청 함수
"""

# ============================================
# Exercise 1: 유연한 계산기 (정답)
# ============================================

def calculate(operation, *numbers):
    """다양한 연산을 수행하는 계산기"""
    if operation == "add":
        # 모든 숫자의 합
        total = 0
        for num in numbers:
            total += num
        return total
    
    elif operation == "multiply":
        # 모든 숫자의 곱
        result = 1
        for num in numbers:
            result *= num
        return result
    
    elif operation == "max":
        # 가장 큰 숫자
        max_num = numbers[0]
        for num in numbers:
            if num > max_num:
                max_num = num
        return max_num
    
    elif operation == "min":
        # 가장 작은 숫자
        min_num = numbers[0]
        for num in numbers:
            if num < min_num:
                min_num = num
        return min_num

# 테스트 코드
print("합계:", calculate("add", 10, 20, 30, 40, 50))  # 출력: 합계: 150
print("곱:", calculate("multiply", 2, 3, 4, 5))  # 출력: 곱: 120
print("최댓값:", calculate("max", 10, 25, 50, 30))  # 출력: 최댓값: 50
print("최솟값:", calculate("min", 10, 25, 50, 30))  # 출력: 최솟값: 10


# ============================================
# Exercise 2: 설정 병합 시스템 (정답)
# ============================================

def merge_settings(**settings):
    """여러 설정을 기본 설정과 병합"""
    # 시스템 기본 설정
    default_settings = {
        "mode": "normal",
        "timeout": 30,
        "retry": 3
    }
    
    # 기본 설정과 받은 설정 병합
    # 같은 키가 있으면 settings가 우선됨
    merged = {**default_settings, **settings}
    
    return merged

# 테스트 코드
result = merge_settings(mode="advanced", retry=5, debug=True)
print("\n병합된 설정:", result)
# 출력: 병합된 설정: {'mode': 'advanced', 'timeout': 30, 'retry': 5, 'debug': True}


# ============================================
# Exercise 3: API 요청 함수 (정답)
# ============================================

def api_request(method, url, **params):
    """FastAPI 스타일의 유연한 API 요청 함수"""
    # 기본 정보 출력
    print(f"메서드: {method}")
    print(f"URL: {url}")
    
    # 파라미터가 있으면 출력
    if params:
        print(f"파라미터: {params}")
    
    # 요청 정보를 담은 딕셔너리 생성
    request_info = {
        "method": method,
        "url": url,
        **params  # 추가 파라미터들 병합
    }
    
    return request_info

# 테스트 코드
request = api_request(
    "POST",
    "/api/users",
    headers={"Authorization": "Bearer token123"},
    data={"name": "hong"}
)
print("\n요청 정보:", request)
# 출력: 요청 정보: {'method': 'POST', 'url': '/api/users', 'headers': {...}, 'data': {...}}


# ============================================
# 추가 예제: 함수 조합 패턴
# ============================================

def create_response(*messages, **metadata):
    """API 응답 생성 (FastAPI 응답 패턴)"""
    response = {
        "messages": list(messages),  # 메시지들
        "metadata": metadata  # 추가 정보
    }
    return response

# 사용 예시
response = create_response(
    "사용자 생성 완료",
    "이메일 전송 완료",
    user_id=123,
    timestamp="2026-02-03 10:30:00"
)

print("\nAPI 응답:", response)
# 출력: API 응답: {'messages': ['사용자 생성 완료', '이메일 전송 완료'], 'metadata': {'user_id': 123, 'timestamp': '2026-02-03 10:30:00'}}
