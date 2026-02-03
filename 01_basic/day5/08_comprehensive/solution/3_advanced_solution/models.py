"""
models.py - FastAPI 스타일 데이터 모델 (해답)

BaseModel 패턴을 사용한 모델 정의
Pydantic BaseModel을 흉내낸 구조입니다.
"""

from typing import Dict, Optional, Any
from validators import validate_email, validate_password


class BaseModel:
    """
    모든 모델의 기본 클래스
    
    Pydantic의 BaseModel을 단순화한 버전입니다.
    모든 데이터 모델이 이 클래스를 상속받습니다.
    """
    
    def to_dict(self) -> Dict[str, Any]:
        """
        객체의 모든 속성을 딕셔너리로 변환
        
        Returns:
            Dict[str, Any]: 속성명을 키로, 속성값을 값으로 하는 딕셔너리
        """
        return self.__dict__.copy()


class UserBase(BaseModel):
    """
    사용자 기본 모델
    
    모든 사용자 관련 모델의 부모 클래스입니다.
    공통 필드인 email을 포함합니다.
    """
    
    def __init__(self, email: str) -> None:
        """
        사용자 기본 정보 초기화
        
        Args:
            email: 사용자 이메일 (검증 및 소문자 변환됨)
        
        Raises:
            ValueError: 이메일 형식이 올바르지 않을 때
        """
        # 이메일 검증 및 정규화 (소문자 변환)
        self.email = validate_email(email)


class UserCreate(UserBase):
    """
    사용자 생성 모델
    
    회원가입 시 사용하는 모델입니다.
    이메일과 비밀번호를 포함합니다.
    """
    
    def __init__(self, email: str, password: str) -> None:
        """
        사용자 생성 정보 초기화
        
        Args:
            email: 사용자 이메일
            password: 비밀번호 (8자 이상, 대문자 포함)
        
        Raises:
            ValueError: 이메일 또는 비밀번호 검증 실패 시
        """
        # 부모 클래스 초기화 (이메일 검증)
        super().__init__(email)
        
        # 비밀번호 검증
        self.password = validate_password(password)


class UserResponse(UserBase):
    """
    사용자 응답 모델
    
    API 응답 시 사용하는 모델입니다.
    보안을 위해 비밀번호는 포함하지 않고, ID를 포함합니다.
    """
    
    def __init__(self, email: str, id: int) -> None:
        """
        사용자 응답 정보 초기화
        
        Args:
            email: 사용자 이메일
            id: 사용자 고유 ID
        
        Raises:
            ValueError: 이메일 검증 실패 시
        """
        # 부모 클래스 초기화 (이메일 검증)
        super().__init__(email)
        
        # ID 저장
        self.id = id


"""
FastAPI 실전 사용 예시:

from fastapi import FastAPI
from models import UserCreate, UserResponse

app = FastAPI()

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    # UserCreate로 받음 (이메일 + 비밀번호)
    # UserResponse로 응답 (이메일 + ID, 비밀번호 제외)
    
    # 비밀번호 해싱 (실제로는 passlib 사용)
    hashed_password = hash_password(user.password)
    
    # DB에 저장
    user_id = save_to_db(user.email, hashed_password)
    
    # 응답 (비밀번호 없음!)
    return UserResponse(email=user.email, id=user_id)

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    # DB에서 조회
    user_data = get_from_db(user_id)
    
    # UserResponse로 응답
    return UserResponse(email=user_data["email"], id=user_id)
"""
