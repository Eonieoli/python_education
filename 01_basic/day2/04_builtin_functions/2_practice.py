# 2_practice.py

"""
Day 2 - 4교시: 내장 함수 + 리스트 순수 함수
Practice (강사와 함께 실습)

학습 목표:
- max, min, sum 활용하여 통계 계산
- sort()와 sorted() 비교 실험
- 리스트 복사 방법 이해
"""

# ============================================
# 실습 1: 점수 통계 계산 (전체 타이핑)
# ============================================

# 시험 점수 리스트
test_scores = [78, 92, 85, 88, 95, 72, 90]

# 학생 수
student_count = len(test_scores)

# 최고 점수와 최저 점수
highest_score = max(test_scores)
lowest_score = min(test_scores)

# 총점과 평균
total_score = sum(test_scores)
average_score = total_score / student_count

# 결과 출력
print("=== 시험 성적 통계 ===")
print(f"학생 수: {student_count}명")
print(f"최고 점수: {highest_score}점")
print(f"최저 점수: {lowest_score}점")
print(f"평균 점수: {average_score:.1f}점")


# ============================================
# 실습 2: 정렬 비교 (sort vs sorted)
# ============================================

# 원본 리스트
prices = [15000, 8000, 23000, 12000, 19000]

# TODO: sorted()를 사용하여 정렬된 새 리스트를 만드세요
# 힌트: sorted_prices = sorted(prices)
sorted_prices = sorted(prices)

print("\n원본 prices:", prices)  # 출력: [15000, 8000, 23000, 12000, 19000]
print("sorted_prices:", sorted_prices)  # 출력: [8000, 12000, 15000, 19000, 23000]

# TODO: prices.sort()를 사용하여 원본 리스트를 정렬하세요
# 힌트: prices.sort()
prices.sort()

print("sort() 후 prices:", prices)  # 출력: [8000, 12000, 15000, 19000, 23000]


# ============================================
# 실습 3: 리스트 복사 실험
# ============================================

# 원본 리스트
original_list = [10, 20, 30]

# TODO: 참조 복사 (같은 리스트를 가리킴)
# 힌트: ref_copy = original_list
ref_copy = original_list

# TODO: 얕은 복사 (새로운 리스트 생성)
# 힌트: shallow_copy = original_list[:]
shallow_copy = original_list[:]

# 참조 복사에 값 추가
ref_copy.append(40)

# 얕은 복사에 값 추가
shallow_copy.append(50)

# 결과 확인
print("\noriginal_list:", original_list)  # 출력: [10, 20, 30, 40]
print("ref_copy:", ref_copy)  # 출력: [10, 20, 30, 40]
print("shallow_copy:", shallow_copy)  # 출력: [10, 20, 30, 50]
