# 3_exercise_solution.py

"""
Day 5 - 5교시: 예외 처리
Exercise - 사용자 등록 시스템 (정답)
"""

# ============================================
# 문제 1: 이메일 검증 함수 (정답)
# ============================================

def validate_email(email: str) -> None:
    """이메일 주소가 유효한지 검증하는 함수"""
    # '@'가 없으면 예외 발생
    if '@' not in email:
        raise ValueError("이메일에 @가 포함되어야 합니다")
    
    # 이메일 길이가 5자 미만이면 예외 발생
    if len(email) < 5:
        raise ValueError("이메일은 5자 이상이어야 합니다")
    
    print(f"✅ 유효한 이메일: {email}")


# ============================================
# 문제 2: 사용자 클래스 (정답)
# ============================================

class User:
    """사용자 정보를 관리하는 클래스"""
    
    def __init__(self, name: str):
        """사용자 이름으로 초기화"""
        self.name = name
        self.age = 0
    
    def set_age(self, age: int) -> None:
        """나이를 설정하는 메서드"""
        # 나이가 0 미만이면 예외 발생
        if age < 0:
            raise ValueError("나이는 0 이상이어야 합니다")
        
        # 나이가 150 초과면 예외 발생
        if age > 150:
            raise ValueError("나이는 150 이하여야 합니다")
        
        # 유효한 나이 저장
        self.age = age
        print(f"✅ 나이 설정 완료: {age}세")


# ============================================
# 테스트 코드
# ============================================

print("=== 이메일 검증 ===")
try:
    validate_email("user@example.com")  # 출력: ✅ 유효한 이메일: user@example.com
except ValueError as e:
    print(f"❌ 검증 실패: {e}")

try:
    validate_email("invalid")  # ValueError: 이메일에 @가 포함되어야 합니다
except ValueError as e:
    print(f"❌ 검증 실패: {e}")

try:
    validate_email("a@b")  # ValueError: 이메일은 5자 이상이어야 합니다
except ValueError as e:
    print(f"❌ 검증 실패: {e}")

print()
print("=== 사용자 나이 설정 ===")
user = User("홍길동")

try:
    user.set_age(25)  # 출력: ✅ 나이 설정 완료: 25세
except ValueError as e:
    print(f"❌ 나이 설정 실패: {e}")

try:
    user.set_age(-5)  # ValueError: 나이는 0 이상이어야 합니다
except ValueError as e:
    print(f"❌ 나이 설정 실패: {e}")

try:
    user.set_age(200)  # ValueError: 나이는 150 이하여야 합니다
except ValueError as e:
    print(f"❌ 나이 설정 실패: {e}")
