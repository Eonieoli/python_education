# 3_exercise_solution.py

"""
Day 3 - 5교시: for문 심화
Exercise - 학생 성적 관리 시스템 (정답)
"""

# ============================================
# 문제 1: 합격자 명단 출력 (정답)
# ============================================

students_scores = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "최지원": 65,
    "정다은": 88,
    "한수빈": 58
}

print("=== 합격자 명단 ===")

# 1. 합격자만 리스트로 모으기
passed_students = []
for name, score in students_scores.items():
    if score < 70:
        continue  # 70점 미만이면 건너뛰기
    passed_students.append((name, score))

# 2. enumerate()로 순번을 매겨서 출력
for num, (name, score) in enumerate(passed_students, start=1):
    print(f"{num}번: {name} ({score}점)")
# 출력:
# 1번: 김철수 (85점)
# 2번: 이영희 (92점)
# 3번: 박민수 (78점)
# 4번: 정다은 (88점)


# ============================================
# 문제 2: 반별 평균 점수 계산 (정답)
# ============================================

class_scores = [
    [85, 90, 75, 82, 78],  # 1반
    [70, 88, 72, 80, 80],  # 2반
    [90, 85, 92, 78, 81]   # 3반
]

print("\n=== 반별 평균 점수 ===")

for class_num, scores in enumerate(class_scores, start=1):
    # 각 반의 총점 계산
    total = 0
    for score in scores:
        total += score
    
    # 평균 계산
    average = total / len(scores)
    
    # 결과 출력
    print(f"{class_num}반 평균: {average:.1f}점")
# 출력:
# 1반 평균: 82.0점
# 2반 평균: 78.0점
# 3반 평균: 85.2점


# ============================================
# 보너스: 더 간결한 방법 (sum 함수 사용)
# ============================================

print("\n=== 반별 평균 (간결한 방법) ===")

for class_num, scores in enumerate(class_scores, start=1):
    average = sum(scores) / len(scores)  # sum() 함수 사용
    print(f"{class_num}반 평균: {average:.1f}점")
