# 1_basic.py

"""
Day 2 - 6교시: 딕셔너리 기초
Basic (강사 시연용)

학습 목표:
- 딕셔너리의 key-value 구조 이해
- 딕셔너리 생성, 접근, 수정, 삭제
- KeyError 이해 및 안전한 접근
- FastAPI JSON 구조의 기초
"""

# ============================================
# 1. 딕셔너리 생성과 기본 구조
# ============================================

# 딕셔너리는 key-value 쌍으로 데이터를 저장합니다
# JSON 구조와 동일하며, FastAPI에서 가장 중요한 자료형입니다!

# 빈 딕셔너리 생성
empty_dict = {}
print(empty_dict)  # 출력: {}

# 학생 정보를 딕셔너리로 저장
student = {
    "name": "김철수",
    "age": 20,
    "major": "컴퓨터공학"
}
print(student)  # 출력: {'name': '김철수', 'age': 20, 'major': '컴퓨터공학'}


# ============================================
# 2. 딕셔너리 접근과 수정
# ============================================

# 대괄호 []로 key를 사용해 value에 접근
student = {"name": "김철수", "age": 20, "major": "컴퓨터공학"}

print(student["name"])  # 출력: 김철수
print(student["age"])   # 출력: 20

# 값 수정 (기존 key에 새로운 value 할당)
student["age"] = 21
print(student["age"])   # 출력: 21

# 여러 값을 한 번에 확인
print(f"{student['name']}님은 {student['age']}세입니다")
# 출력: 김철수님은 21세입니다


# ============================================
# 3. 딕셔너리 추가와 삭제
# ============================================

# 새로운 key-value 추가 (존재하지 않는 key에 값 할당)
student = {"name": "김철수", "age": 20}

student["major"] = "컴퓨터공학"  # 새 항목 추가
student["grade"] = 3            # 새 항목 추가
print(student)
# 출력: {'name': '김철수', 'age': 20, 'major': '컴퓨터공학', 'grade': 3}

# del 키워드로 항목 삭제
del student["grade"]
print(student)
# 출력: {'name': '김철수', 'age': 20, 'major': '컴퓨터공학'}


# ============================================
# 4. KeyError와 안전한 접근
# ============================================

# 존재하지 않는 key에 접근하면 KeyError 발생!
student = {"name": "김철수", "age": 20}

# print(student["email"])  # 주석 해제하면 KeyError 발생!

# 안전하게 확인하는 방법: in 연산자 사용
if "email" in student:
    print(student["email"])
else:
    print("이메일 정보가 없습니다")  # 출력: 이메일 정보가 없습니다

# key 존재 확인
print("name" in student)   # 출력: True
print("phone" in student)  # 출력: False


# ============================================
# 5. 실전 예제: 상품 정보 관리
# ============================================

# 온라인 쇼핑몰의 상품 정보
product = {
    "id": 1001,
    "name": "노트북",
    "price": 1200000,
    "stock": 15
}

# 상품 정보 출력
print(f"상품명: {product['name']}")
print(f"가격: {product['price']:,}원")
print(f"재고: {product['stock']}개")

# 재고 업데이트 (판매 발생)
product["stock"] = product["stock"] - 1
print(f"판매 후 재고: {product['stock']}개")  # 출력: 판매 후 재고: 14개

# 할인 정보 추가
product["discount_rate"] = 0.1  # 10% 할인
discounted_price = product["price"] * (1 - product["discount_rate"])
print(f"할인가: {discounted_price:,.0f}원")  # 출력: 할인가: 1,080,000원
