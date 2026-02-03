# 3_exercise_solution.py

"""
Day 2 - 1, 2교시 통합: 리스트 기본 + len()
Exercise - 성적 처리 시스템 (정답)
"""

# ============================================
# 주어진 데이터
# ============================================

math_scores = [85, 92, 88, 76, 90, 82, 95, 78]


# ============================================
# 정답 코드
# ============================================

# 1. 전체 학생 수
student_count = len(math_scores)
print(f"전체 학생 수: {student_count}명")
# 출력: 전체 학생 수: 8명


# 2. 첫 번째 학생과 마지막 학생의 점수
first_score = math_scores[0]
last_score = math_scores[-1]
print(f"첫 번째 학생 점수: {first_score}점")
print(f"마지막 학생 점수: {last_score}점")
# 출력: 첫 번째 학생 점수: 85점
# 출력: 마지막 학생 점수: 78점


# 3. 상위 3명의 점수 (처음 3개)
top_three = math_scores[:3]
print(f"상위 3명 점수: {top_three}")
# 출력: 상위 3명 점수: [85, 92, 88]


# 4. 하위 3명의 점수 (마지막 3개)
bottom_three = math_scores[-3:]
print(f"하위 3명 점수: {bottom_three}")
# 출력: 하위 3명 점수: [82, 95, 78]


# 5. 전체 점수의 합계
total_score = sum(math_scores)
print(f"총점: {total_score}점")
# 출력: 총점: 680점


# 6. 평균 점수
average_score = total_score / student_count
print(f"평균: {average_score}점")
# 출력: 평균: 85.0점


# 7. 점수를 역순으로 출력
reversed_scores = math_scores[::-1]
print(f"역순 점수: {reversed_scores}")
# 출력: 역순 점수: [78, 95, 82, 90, 76, 88, 92, 85]
