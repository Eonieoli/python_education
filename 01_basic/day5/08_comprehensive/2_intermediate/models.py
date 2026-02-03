"""
models.py - 데이터 모델 클래스들

User와 Product 클래스를 정의합니다.
utils 모듈의 검증 함수들을 활용합니다.
"""

from typing import Optional
# TODO: utils 모듈에서 필요한 함수들을 import하세요
# from utils import ...


# TODO 1: User 클래스 작성
# 속성:
#   - name: str (사용자 이름)
#   - email: str (이메일)
#   - user_id: str (사용자 ID)
#
# 메서드:
#   - __init__(name: str, email: str, user_id: str) -> None
#       * validate_email()로 이메일 검증
#       * 검증 실패 시 ValueError 발생 ("이메일 형식이 올바르지 않습니다")
#   - __str__() -> str
#       * "사용자: {name} ({email}), ID: {user_id}" 형식
#
# 타입 힌트 완벽 적용!


# TODO 2: Product 클래스 작성
# 속성:
#   - name: str (상품명)
#   - price: float (가격)
#   - stock: int (재고)
#   - product_id: str (상품 ID)
#
# 메서드:
#   - __init__(name: str, price: float, stock: int, product_id: str) -> None
#       * validate_price()로 가격 검증
#       * validate_stock()로 재고 검증
#   
#   - purchase(quantity: int) -> None
#       * quantity가 0 이하면 ValueError 발생
#       * 재고가 부족하면 ValueError 발생 
#         ("재고가 부족합니다 (현재: {stock}개, 요청: {quantity}개)")
#       * 재고 감소
#       * f-string으로 "{quantity}개 구매 완료! 남은 재고: {stock}개" 출력
#   
#   - restock(quantity: int) -> None
#       * quantity가 0 이하면 ValueError 발생
#       * 재고 증가
#       * f-string으로 "{quantity}개 입고 완료! 현재 재고: {stock}개" 출력
#   
#   - get_total_value() -> float
#       * 재고 총 가치 반환 (price * stock)
#   
#   - __str__() -> str
#       * "상품: {name} - {price}원, 재고: {stock}개, ID: {product_id}" 형식
#
# 타입 힌트 완벽 적용!

