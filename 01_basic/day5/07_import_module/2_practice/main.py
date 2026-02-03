"""
Day 5 - 07교시: import 완전 정복
Practice 단계 - main.py

student_model과 grade_utils를 import해서 사용합니다.
TODO 부분을 완성하세요!
"""

# ===== TODO: 필요한 모듈 import =====
# student_model.py에서 Student 클래스를 import하세요
# grade_utils.py에서 필요한 함수들을 import하세요
# 힌트: from student_model import Student
#       from grade_utils import calculate_class_average, ...


print("=" * 50)
print("학생 성적 관리 시스템")
print("=" * 50)


# ===== 1. 학생 정보 입력 =====
print("\n1. 학생 정보 생성")
print("-" * 50)

# TODO: Student 클래스로 학생 3명 생성
# 힌트: students = [
#           Student("김철수", "2024001", [85, 90, 88]),
#           Student("이영희", "2024002", [92, 88, 95]),
#           Student("박민수", "2024003", [78, 82, 80])
#       ]


# 각 학생 정보 출력
print("생성된 학생 정보:")
# TODO: for문으로 각 학생의 get_info() 출력
# 힌트: for student in students:
#           print(student.get_info())


# ===== 2. 반 전체 성적 통계 =====
print("\n2. 반 전체 성적 통계")
print("-" * 50)

# TODO: 모든 학생의 성적을 하나의 리스트로 만들기
# 힌트: all_grades = []
#       for student in students:
#           all_grades.extend(student.grades)


print(f"전체 성적: {all_grades}")

# TODO: grade_utils의 함수들을 사용해서 통계 계산
# 힌트: avg = calculate_class_average(all_grades)
#       highest = find_highest_grade(all_grades)
#       lowest = find_lowest_grade(all_grades)
#       passing = count_passing_students(all_grades)


# TODO: 결과 출력
# print(f"반 평균: {avg:.1f}점")
# print(f"최고 점수: {highest}점")
# print(f"최저 점수: {lowest}점")
# print(f"합격자 수: {passing}명 (60점 이상)")


# ===== 3. 등급 분포 =====
print("\n3. 등급 분포")
print("-" * 50)

# TODO: grade_utils의 get_grade_distribution 함수 사용
# 힌트: distribution = get_grade_distribution(all_grades)


# TODO: 등급별 인원 출력
# 힌트: for grade_letter, count in distribution.items():
#           print(f"{grade_letter}: {count}명")


# ===== 4. 성적 리포트 생성 =====
print("\n4. 성적 리포트")
print("-" * 50)

# TODO: format_grade_report 함수로 리포트 생성
# 힌트: report = format_grade_report(
#           len(students),  # 총 학생 수
#           avg,            # 평균
#           highest,        # 최고 점수
#           lowest          # 최저 점수
#       )


# TODO: 리포트 출력
# print(report)


# ===== 5. 새 학생 추가 =====
print("\n5. 새 학생 추가")
print("-" * 50)

# TODO: 새 학생 생성 (성적은 비어있는 상태)
# 힌트: new_student = Student("최지우", "2024004")


# TODO: add_grade()로 성적 3개 추가
# new_student.add_grade(88)
# new_student.add_grade(92)
# new_student.add_grade(85)


# TODO: 새 학생 정보 출력
# print(f"새 학생: {new_student.get_info()}")


# TODO: 학생 리스트에 추가
# students.append(new_student)


# TODO: 업데이트된 전체 학생 수 출력
# print(f"\n총 학생 수: {len(students)}명")


# ===== 학습 정리 =====
print("\n" + "=" * 50)
print("학습 정리")
print("=" * 50)
print("""
이 예제에서 배운 것:

1. 모듈 분리
   - student_model.py: Student 클래스
   - grade_utils.py: 성적 처리 함수들
   - main.py: 두 모듈을 import해서 사용

2. import 활용
   - from student_model import Student
   - from grade_utils import 함수들...
   - 클래스와 함수를 조합해서 사용

3. 실전 패턴
   - 데이터 모델(클래스)과 유틸리티(함수)를 분리
   - FastAPI에서도 이렇게 models/ 와 utils/ 로 분리!
""")
