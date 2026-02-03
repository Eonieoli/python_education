# 3_exercise_solution.py

"""
Day 2 - 4교시: 내장 함수 + 리스트 순수 함수
Exercise - 성적 분석 시스템 (정답)
"""

# ============================================
# 주어진 데이터
# ============================================

math_scores = [78, 92, 85, 88, 95, 72]


# ============================================
# 정답 코드
# ============================================

# 1. 학생 수
student_count = len(math_scores)  # 6

# 2. 최고 점수
highest = max(math_scores)  # 95

# 3. 최저 점수
lowest = min(math_scores)  # 72

# 4. 총점
total = sum(math_scores)  # 510

# 5. 평균
average = total / student_count  # 85.0

# 6. 내림차순 정렬
sorted_desc = sorted(math_scores, reverse=True)  # [95, 92, 88, 85, 78, 72]

# 7. 상위 3명
top_3 = sorted_desc[0:3]  # [95, 92, 88]


# ============================================
# 결과 출력
# ============================================

print("=== 수학 성적 분석 ===")
print(f"학생 수: {student_count}명")
print(f"최고 점수: {highest}점")
print(f"최저 점수: {lowest}점")
print(f"평균 점수: {average:.1f}점")
print()
print(f"상위 3명 점수: {top_3}")
print(f"원본 유지 확인: {math_scores}")
