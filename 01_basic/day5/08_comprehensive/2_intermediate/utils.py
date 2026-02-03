"""
utils.py - 검증 함수 모듈

이메일, 가격, 재고 등을 검증하는 유틸리티 함수들을 제공합니다.
"""

from typing import Optional

# TODO 1: validate_email 함수 작성
# 매개변수: email (str)
# 반환값: bool
# 기능: 이메일에 '@'가 포함되어 있으면 True, 아니면 False
# 타입 힌트 필수!


# TODO 2: validate_price 함수 작성
# 매개변수: price (float)
# 반환값: None
# 기능: 
#   - price가 0 이하면 ValueError 발생 ("가격은 0보다 커야 합니다")
#   - 정상이면 아무 동작 안 함
# 타입 힌트 필수!


# TODO 3: validate_stock 함수 작성
# 매개변수: stock (int)
# 반환값: None
# 기능:
#   - stock이 0 미만이면 ValueError 발생 ("재고는 0 이상이어야 합니다")
#   - 정상이면 아무 동작 안 함
# 타입 힌트 필수!


# TODO 4: format_currency 함수 작성 (선택)
# 매개변수: amount (float)
# 반환값: str
# 기능: 금액을 천 단위 콤마가 있는 문자열로 반환
# 예: 1200000 -> "1,200,000원"
# 타입 힌트 필수!
# 힌트: f-string의 {:,} 포맷 사용

