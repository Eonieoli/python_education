# 3_advanced_solution.py

"""
Day 4 - 8교시: 함수와 타입 힌트 종합 실습
🔴 도전 Problem - *args, **kwargs + 완벽한 타입 힌트 (정답)
"""

from typing import List, Dict, Optional, Any


# ============================================
# 1. 가변 인수 통계 계산
# ============================================

def calculate_stats(*numbers: int) -> Dict[str, float]:
    """
    여러 숫자의 통계를 계산합니다.
    
    Args:
        *numbers: 계산할 숫자들
    
    Returns:
        합계, 평균, 최댓값, 최솟값을 담은 딕셔너리
    """
    total = sum(numbers)
    average = total / len(numbers)
    
    return {
        "sum": total,
        "average": average,
        "max": max(numbers),
        "min": min(numbers)
    }


# ============================================
# 2. 설정 병합 함수
# ============================================

def merge_settings(**settings: Any) -> Dict[str, Any]:
    """
    여러 설정을 하나의 딕셔너리로 병합합니다.
    나중에 전달된 값이 이전 값을 덮어씁니다.
    
    Args:
        **settings: 병합할 설정들
    
    Returns:
        병합된 설정 딕셔너리
    """
    # **kwargs는 이미 딕셔너리이므로 그대로 반환
    return settings


# ============================================
# 3. API 요청 함수
# ============================================

def build_api_request(endpoint: str, **params: Any) -> Dict[str, Any]:
    """
    API 요청 정보를 생성합니다.
    
    Args:
        endpoint: API 엔드포인트 경로
        **params: 쿼리 파라미터들
    
    Returns:
        엔드포인트와 파라미터를 담은 딕셔너리
    """
    return {
        "endpoint": endpoint,
        "params": params
    }


# ============================================
# 결과 확인
# ============================================

if __name__ == "__main__":
    print("=" * 50)
    print("1. 가변 인수 통계 계산")
    print("=" * 50)
    
    stats = calculate_stats(10, 20, 30, 40, 50)
    print(f"숫자: 10, 20, 30, 40, 50")
    print(f"합계: {stats['sum']}")
    print(f"평균: {stats['average']}")
    print(f"최댓값: {stats['max']}")
    print(f"최솟값: {stats['min']}")
    # 출력:
    # 합계: 150
    # 평균: 30.0
    # 최댓값: 50
    # 최솟값: 10
    
    print("\n" + "=" * 50)
    print("2. 설정 병합")
    print("=" * 50)
    
    settings = merge_settings(
        host="localhost",
        port=8000,
        debug=True,
        port=3000  # port 덮어쓰기
    )
    print(f"병합된 설정: {settings}")
    # 출력: 병합된 설정: {'host': 'localhost', 'port': 3000, 'debug': True}
    
    print("\n" + "=" * 50)
    print("3. API 요청 정보 생성")
    print("=" * 50)
    
    request1 = build_api_request("/users", page=1, limit=10)
    print(f"요청 1: {request1}")
    # 출력: 요청 1: {'endpoint': '/users', 'params': {'page': 1, 'limit': 10}}
    
    request2 = build_api_request("/posts", user_id=123, sort="date", order="desc")
    print(f"요청 2: {request2}")
    # 출력: 요청 2: {'endpoint': '/posts', 'params': {'user_id': 123, 'sort': 'date', 'order': 'desc'}}
