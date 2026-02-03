"""
main.py - FastAPI 스타일 API 시뮬레이션 (해답)

FastAPI 엔드포인트를 흉내낸 함수들을 정의합니다.
실제로는 HTTP 요청을 받지 않고, 함수 호출로 시뮬레이션합니다.
"""

from typing import Dict, Any, Optional
from models import UserCreate, UserResponse


# 간단한 데이터베이스 시뮬레이션 (딕셔너리)
users_db: Dict[int, Dict[str, Any]] = {}
next_id: int = 1


def create_user(user_data: UserCreate) -> UserResponse:
    """
    사용자 생성 (회원가입)
    
    Args:
        user_data: 사용자 생성 정보 (이메일 + 비밀번호)
    
    Returns:
        UserResponse: 생성된 사용자 정보 (이메일 + ID, 비밀번호 제외)
    """
    global next_id
    
    # UserCreate를 딕셔너리로 변환하여 DB에 저장
    user_dict = user_data.to_dict()
    users_db[next_id] = user_dict
    
    # UserResponse 생성 (비밀번호 제외!)
    response = UserResponse(email=user_data.email, id=next_id)
    
    # ID 증가
    next_id += 1
    
    return response


def get_user(user_id: int) -> Optional[UserResponse]:
    """
    사용자 조회
    
    Args:
        user_id: 조회할 사용자 ID
    
    Returns:
        Optional[UserResponse]: 사용자가 존재하면 UserResponse, 없으면 None
    """
    # DB에서 사용자 찾기
    user_data = users_db.get(user_id)
    
    if user_data is None:
        return None
    
    # UserResponse로 변환하여 반환
    return UserResponse(email=user_data["email"], id=user_id)


def main() -> None:
    """API 시뮬레이션 메인 함수"""
    print("=== FastAPI 스타일 API 모델 테스트 ===\n")
    
    # 1. 회원가입 테스트
    print("1. 회원가입 (UserCreate -> UserResponse)")
    
    # UserCreate 객체 생성 (요청 데이터)
    user_create = UserCreate("ADMIN@EXAMPLE.COM", "SecurePass123")
    print(f"요청 데이터: {user_create.to_dict()}")
    
    # API 함수 호출 (회원가입)
    user_response = create_user(user_create)
    print(f"응답 데이터: {user_response.to_dict()}")
    
    # 2. 사용자 조회 테스트
    print("\n2. 사용자 조회 (UserResponse)")
    
    # API 함수 호출 (조회)
    user = get_user(1)
    if user:
        print(f"응답 데이터: {user.to_dict()}")
    
    # 3. 예외 처리 테스트
    print("\n3. 예외 처리 테스트")
    
    # 3-1. 이메일 검증 에러
    try:
        invalid_user = UserCreate("invalidemail.com", "SecurePass123")
    except ValueError as e:
        print(f"이메일 검증 에러: {e}")
    
    # 3-2. 비밀번호 검증 에러 (길이 부족)
    try:
        weak_user = UserCreate("user@example.com", "short")
    except ValueError as e:
        print(f"비밀번호 검증 에러: {e}")
    
    # 3-3. 비밀번호 검증 에러 (대문자 없음)
    try:
        weak_user2 = UserCreate("user@example.com", "lowercase123")
    except ValueError as e:
        print(f"비밀번호 검증 에러: {e}")


if __name__ == "__main__":
    main()
