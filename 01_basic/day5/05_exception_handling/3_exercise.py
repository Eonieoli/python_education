# 3_exercise.py

"""
Day 5 - 5교시: 예외 처리
Exercise - 사용자 등록 시스템

문제 1: 사용자 정보 검증 함수 만들기
- validate_email() 함수를 작성하세요
- 이메일에 '@'가 없으면 ValueError 발생
- 이메일 길이가 5자 미만이면 ValueError 발생

문제 2: 안전한 사용자 클래스 만들기
- User 클래스의 set_age() 메서드를 완성하세요
- 나이가 0 미만이거나 150 초과면 ValueError 발생
- 유효한 나이만 설정되도록 구현

출력 예시:
=== 이메일 검증 ===
✅ 유효한 이메일: user@example.com
❌ 검증 실패: 이메일에 @가 포함되어야 합니다
❌ 검증 실패: 이메일은 5자 이상이어야 합니다

=== 사용자 나이 설정 ===
✅ 나이 설정 완료: 25세
❌ 나이 설정 실패: 나이는 0 이상이어야 합니다
❌ 나이 설정 실패: 나이는 150 이하여야 합니다
"""

# ============================================
# TODO: 문제 1 - 이메일 검증 함수
# ============================================

def validate_email(email: str) -> None:
    """이메일 주소가 유효한지 검증하는 함수
    
    Args:
        email: 검증할 이메일 주소
        
    Raises:
        ValueError: 이메일이 유효하지 않을 때
    """
    # TODO: '@'가 없으면 ValueError 발생
    # 힌트: if '@' not in email:
    
    
    # TODO: 이메일 길이가 5자 미만이면 ValueError 발생
    # 힌트: if len(email) < 5:
    
    
    print(f"✅ 유효한 이메일: {email}")


# ============================================
# TODO: 문제 2 - 사용자 클래스
# ============================================

class User:
    """사용자 정보를 관리하는 클래스"""
    
    def __init__(self, name: str):
        """사용자 이름으로 초기화"""
        self.name = name
        self.age = 0
    
    def set_age(self, age: int) -> None:
        """나이를 설정하는 메서드
        
        Args:
            age: 설정할 나이
            
        Raises:
            ValueError: 나이가 유효하지 않을 때
        """
        # TODO: 나이가 0 미만이면 ValueError 발생
        # 힌트: if age < 0:
        #       raise ValueError("나이는 0 이상이어야 합니다")
        
        
        # TODO: 나이가 150 초과면 ValueError 발생
        # 힌트: if age > 150:
        
        
        # TODO: 유효한 나이를 self.age에 저장
        
        
        print(f"✅ 나이 설정 완료: {age}세")


# ============================================
# 테스트 코드 (수정하지 마세요)
# ============================================

print("=== 이메일 검증 ===")
try:
    validate_email("user@example.com")
except ValueError as e:
    print(f"❌ 검증 실패: {e}")

try:
    validate_email("invalid")  # @ 없음
except ValueError as e:
    print(f"❌ 검증 실패: {e}")

try:
    validate_email("a@b")  # 5자 미만
except ValueError as e:
    print(f"❌ 검증 실패: {e}")

print()
print("=== 사용자 나이 설정 ===")
user = User("홍길동")

try:
    user.set_age(25)
except ValueError as e:
    print(f"❌ 나이 설정 실패: {e}")

try:
    user.set_age(-5)  # 음수
except ValueError as e:
    print(f"❌ 나이 설정 실패: {e}")

try:
    user.set_age(200)  # 너무 큼
except ValueError as e:
    print(f"❌ 나이 설정 실패: {e}")
