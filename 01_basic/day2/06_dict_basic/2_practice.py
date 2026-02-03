# 2_practice.py

"""
Day 2 - 6교시: 딕셔너리 기초
Practice (강사와 함께 실습)

학습 목표:
- 학생 정보를 딕셔너리로 관리하기
- 상품 데이터 추가, 수정, 삭제하기
"""

# ============================================
# 실습 1: 학생 정보 딕셔너리 (전체 타이핑)
# ============================================

# 학생 정보를 딕셔너리로 생성
student = {
    "name": "이영희",
    "student_id": "2024001",
    "major": "경영학과",
    "grade": 2
}

# 학생 정보 출력
print(f"이름: {student['name']}")
print(f"학번: {student['student_id']}")
print(f"전공: {student['major']}")
print(f"학년: {student['grade']}학년")

# 연락처 정보 추가
student["phone"] = "010-1234-5678"
student["email"] = "yhlee@university.ac.kr"

# 학년 업데이트 (진급)
student["grade"] = 3

# 최종 정보 확인
print("\n=== 업데이트된 학생 정보 ===")
print(student)


# ============================================
# 실습 2: 상품 데이터 관리 (TODO)
# ============================================

# 상품 정보 생성
product = {
    "name": "무선 이어폰",
    "price": 89000,
    "brand": "삼성",
    "stock": 50
}

# TODO: 상품명과 가격을 출력하세요
# 힌트: f-string과 딕셔너리 접근 사용
print(f"상품명: {product['name']}")
print(f"가격: {product['price']:,}원")

# TODO: 할인율 10%를 추가하고 할인가를 계산하세요
# 힌트: product["discount_rate"] = 0.1
product["discount_rate"] = 0.1
discounted_price = product["price"] * (1 - product["discount_rate"])
print(f"할인가: {discounted_price:,.0f}원")

# TODO: 재고가 5개 판매되었습니다. 재고를 업데이트하세요
# 힌트: product["stock"] = product["stock"] - 5
product["stock"] = product["stock"] - 5
print(f"남은 재고: {product['stock']}개")

# TODO: 색상 정보를 추가하세요 (예: "화이트")
# 힌트: product["color"] = "화이트"
product["color"] = "화이트"

# 최종 상품 정보 확인
print("\n=== 최종 상품 정보 ===")
print(product)
