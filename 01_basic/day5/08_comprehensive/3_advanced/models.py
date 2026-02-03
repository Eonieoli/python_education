"""
models.py - FastAPI 스타일 데이터 모델

BaseModel 패턴을 사용한 모델 정의
Pydantic BaseModel을 흉내낸 구조입니다.
"""

from typing import Dict, Optional, Any
# TODO: validators 모듈에서 필요한 함수들을 import하세요


# TODO 1: BaseModel 클래스 작성 (모든 모델의 부모)
# 이것은 FastAPI의 Pydantic BaseModel을 흉내낸 것입니다.
#
# 메서드:
#   - to_dict() -> Dict[str, Any]
#       * 객체의 모든 속성을 딕셔너리로 변환
#       * self.__dict__ 사용
#       * 반환값: {"email": "...", "password": "...", ...} 형태
#
# 타입 힌트 완벽 적용!


# TODO 2: UserBase 클래스 작성 (BaseModel 상속)
# 공통 사용자 필드를 정의하는 부모 클래스
#
# 속성:
#   - email: str
#
# 메서드:
#   - __init__(email: str) -> None
#       * validate_email()로 이메일 검증 및 소문자 변환
#       * 검증된 이메일을 self.email에 저장
#
# 타입 힌트 완벽 적용!


# TODO 3: UserCreate 클래스 작성 (UserBase 상속)
# 회원가입 시 사용하는 모델 (비밀번호 포함)
#
# 추가 속성:
#   - password: str
#
# 메서드:
#   - __init__(email: str, password: str) -> None
#       * super().__init__(email)로 부모 클래스 초기화
#       * validate_password()로 비밀번호 검증
#       * 검증된 비밀번호를 self.password에 저장
#
# 타입 힌트 완벽 적용!


# TODO 4: UserResponse 클래스 작성 (UserBase 상속)
# API 응답 시 사용하는 모델 (비밀번호 없음, ID 포함)
#
# 추가 속성:
#   - id: int
#
# 메서드:
#   - __init__(email: str, id: int) -> None
#       * super().__init__(email)로 부모 클래스 초기화
#       * id를 self.id에 저장
#
# 타입 힌트 완벽 적용!


"""
FastAPI에서는 이렇게 사용합니다:

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    # user는 UserCreate 타입 (이메일 + 비밀번호)
    # 응답은 UserResponse 타입 (이메일 + ID, 비밀번호 제외)
    return UserResponse(email=user.email, id=1)
"""
