"""
validators.py - 검증 함수 모듈

이메일, 비밀번호 등을 검증하는 함수들을 제공합니다.
FastAPI의 Pydantic validator 패턴을 흉내냅니다.
"""

from typing import Optional

# TODO 1: validate_email 함수 작성
# 매개변수: email (str)
# 반환값: str (검증 후 소문자로 변환된 이메일)
# 기능:
#   - '@'가 없으면 ValueError 발생 ("이메일 형식이 올바르지 않습니다")
#   - 이메일을 소문자로 변환하여 반환
# 타입 힌트 완벽 적용!


# TODO 2: validate_password 함수 작성
# 매개변수: password (str)
# 반환값: str (검증된 비밀번호)
# 기능:
#   - 길이가 8자 미만이면 ValueError 발생 ("비밀번호는 8자 이상이어야 합니다")
#   - 대문자가 하나도 없으면 ValueError 발생 ("비밀번호는 대문자를 포함해야 합니다")
#   - 검증 통과 시 그대로 반환
# 타입 힌트 완벽 적용!
# 힌트: any(c.isupper() for c in password) 활용


# TODO 3: validate_age 함수 작성 (선택)
# 매개변수: age (int)
# 반환값: int
# 기능:
#   - 0 미만이면 ValueError 발생 ("나이는 0 이상이어야 합니다")
#   - 150 초과면 ValueError 발생 ("나이가 너무 많습니다")
#   - 검증 통과 시 그대로 반환
# 타입 힌트 완벽 적용!

