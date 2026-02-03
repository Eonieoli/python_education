# 2_intermediate_solution.py

"""
Day 3 - 8교시: 종합 실습
🟡 응용 Problem - 학생 성적 관리 시스템 (정답)
"""

# ============================================
# 주어진 데이터
# ============================================

# 학생 성적 데이터 (리스트 안에 딕셔너리)
students = [
    {"name": "홍길동", "scores": [85, 90, 80]},
    {"name": "김철수", "scores": [95, 88, 93]},
    {"name": "이영희", "scores": [72, 80, 82]},
    {"name": "박민수", "scores": [90, 85, 89]}
]


# ============================================
# 정답 코드
# ============================================

# 1. 각 학생의 평균을 저장할 딕셔너리
averages = {}

# 2. 각 학생의 평균 계산하고 출력
print("===== 개별 성적 =====")
for student in students:
    # 학생 이름 가져오기
    name = student["name"]
    # 점수 리스트 가져오기
    scores = student["scores"]
    # 평균 계산
    avg = sum(scores) / len(scores)
    # averages 딕셔너리에 저장
    averages[name] = avg
    # 출력
    print(f"{name} - 평균: {avg}점")

# 3. 우수 학생 찾기 (평균 80점 이상, 리스트 컴프리헨션 사용)
honor_students = [name for name, avg in averages.items() if avg >= 80]
print(f"\n우수 학생 (평균 80점 이상): {honor_students}")

# 4. 전체 평균 계산
total_avg = sum(averages.values()) / len(averages)
print(f"전체 평균: {total_avg:.2f}점")

# 5. 최고 성적 학생 찾기
max_student = max(averages, key=averages.get)
max_score = averages[max_student]
print(f"최고 성적: {max_student} ({max_score:.1f}점)")
