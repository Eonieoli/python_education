# 3_exercise_solution.py

"""
Day 2 - 3교시: 리스트 수정 (메서드)
Exercise - 학생 명단 관리 시스템 (정답)
"""

# ============================================
# 문제 1: 학생 명단 관리
# ============================================

# 초기 학생 명단
students = ["김민준", "이서윤", "박도윤"]
print("초기 명단:", students)

# 1. 새로운 학생 3명 추가
students.append("최서준")
students.append("정하은")
students.append("강지우")
print("학생 추가 후:", students)

# 2. 맨 앞에 반장 추가
students.insert(0, "이준호")
print("반장 추가 후:", students)

# 3. 인덱스 3번 학생 이름 수정
students[3] = "박서연"
print("이름 수정 후:", students)

# 4. 전학간 학생 제거
students.remove("최서준")
print("전학 후:", students)


print("\n" + "="*50)
print("문제 2: 재고 목록 관리")
print("="*50 + "\n")

# ============================================
# 문제 2: 재고 목록 관리
# ============================================

# 현재 재고 목록
inventory = ["노트북", "마우스", "키보드", "모니터"]
print("현재 재고:", inventory)

# 1. 신규 상품 2개 추가
inventory.append("헤드셋")
inventory.append("웹캠")
print("신규 추가 후:", inventory)

# 2. 품절 상품 제거 (pop으로 제거하며 기록)
sold = inventory.pop(3)
print(f"품절 제거: {sold}")
print("제거 후:", inventory)

# 3. 상품 교체
inventory[2] = "기계식 키보드"
print("교체 후:", inventory)
