"""
main.py - FastAPI 스타일 API 시뮬레이션

FastAPI 엔드포인트를 흉내낸 함수들을 정의합니다.
실제로는 HTTP 요청을 받지 않고, 함수 호출로 시뮬레이션합니다.
"""

from typing import Dict, Any
# TODO: models 모듈에서 필요한 클래스들을 import하세요


# 간단한 데이터베이스 시뮬레이션 (딕셔너리)
users_db: Dict[int, Dict[str, Any]] = {}
next_id: int = 1


# TODO 1: create_user 함수 작성
# 매개변수: user_data (UserCreate 타입)
# 반환값: UserResponse 타입
# 기능:
#   - global next_id 사용
#   - user_data를 딕셔너리로 변환 (to_dict() 사용)
#   - users_db에 저장 (키: next_id, 값: 딕셔너리)
#   - UserResponse 객체 생성 (email, id)
#   - next_id 증가
#   - UserResponse 반환
# 타입 힌트 완벽 적용!


# TODO 2: get_user 함수 작성
# 매개변수: user_id (int)
# 반환값: UserResponse 또는 None
# 기능:
#   - users_db에서 user_id로 사용자 찾기
#   - 있으면 UserResponse 객체로 변환하여 반환
#   - 없으면 None 반환
# 타입 힌트 완벽 적용!
# 힌트: Optional[UserResponse] 반환 타입 사용


# TODO 3: 메인 함수 작성
def main() -> None:
    """API 시뮬레이션 메인 함수"""
    print("=== FastAPI 스타일 API 모델 테스트 ===\n")
    
    # 1. 회원가입 테스트
    print("1. 회원가입 (UserCreate -> UserResponse)")
    # - UserCreate 객체 생성 (email: "admin@example.com", password: "SecurePass123")
    # - to_dict()로 딕셔너리 변환하여 "요청 데이터: ..." 출력
    # - create_user() 함수 호출
    # - 반환된 UserResponse를 to_dict()로 변환하여 "응답 데이터: ..." 출력
    
    
    # 2. 사용자 조회 테스트
    print("\n2. 사용자 조회 (UserResponse)")
    # - get_user(1) 호출
    # - 결과를 to_dict()로 변환하여 "응답 데이터: ..." 출력
    
    
    # 3. 예외 처리 테스트
    print("\n3. 예외 처리 테스트")
    
    # 3-1. 이메일 검증 에러
    # try-except로 '@' 없는 이메일로 UserCreate 생성 시도
    # - email: "invalidemail.com", password: "SecurePass123"
    
    
    # 3-2. 비밀번호 검증 에러 (길이 부족)
    # try-except로 짧은 비밀번호로 UserCreate 생성 시도
    # - email: "user@example.com", password: "short"
    
    
    # 3-3. 비밀번호 검증 에러 (대문자 없음)
    # try-except로 대문자 없는 비밀번호로 UserCreate 생성 시도
    # - email: "user@example.com", password: "lowercase123"
    


# TODO 4: 메인 함수 실행
if __name__ == "__main__":
    main()


"""
실행 결과 예시:
=== FastAPI 스타일 API 모델 테스트 ===

1. 회원가입 (UserCreate -> UserResponse)
요청 데이터: {'email': 'admin@example.com', 'password': 'SecurePass123'}
응답 데이터: {'email': 'admin@example.com', 'id': 1}

2. 사용자 조회 (UserResponse)
응답 데이터: {'email': 'admin@example.com', 'id': 1}

3. 예외 처리 테스트
이메일 검증 에러: 이메일 형식이 올바르지 않습니다
비밀번호 검증 에러: 비밀번호는 8자 이상이어야 합니다
비밀번호 검증 에러: 비밀번호는 대문자를 포함해야 합니다
"""
