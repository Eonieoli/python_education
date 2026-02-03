# 1_basic.py

"""
Day 2 - 4교시: 내장 함수 + 리스트 순수 함수
Basic (강사 시연용)

학습 목표:
- 핵심 내장 함수 사용법 (len, max, min, sum, sorted)
- 리스트 메서드 vs 순수 함수 차이 이해
- sort()와 sorted()의 차이점 이해
- 얕은 복사 개념 이해
"""

# ============================================
# 1. 핵심 내장 함수
# ============================================

# 숫자 리스트
scores = [85, 92, 78, 95, 88]

# len(): 리스트 길이 (복습)
print("학생 수:", len(scores))  # 출력: 학생 수: 5

# max(): 최댓값
print("최고 점수:", max(scores))  # 출력: 최고 점수: 95

# min(): 최솟값
print("최저 점수:", min(scores))  # 출력: 최저 점수: 78

# sum(): 합계
print("총점:", sum(scores))  # 출력: 총점: 438

# 평균 계산 (sum과 len 조합)
average = sum(scores) / len(scores)
print("평균:", average)  # 출력: 평균: 87.6


# ============================================
# 2. sorted(): 정렬된 새 리스트 반환
# ============================================

# 원본 리스트
numbers = [5, 2, 8, 1, 9]

# sorted()는 정렬된 새 리스트를 반환 (원본 유지)
sorted_numbers = sorted(numbers)

print("원본:", numbers)  # 출력: 원본: [5, 2, 8, 1, 9]
print("정렬:", sorted_numbers)  # 출력: 정렬: [1, 2, 5, 8, 9]

# 내림차순 정렬
sorted_desc = sorted(numbers, reverse=True)
print("내림차순:", sorted_desc)  # 출력: 내림차순: [9, 8, 5, 2, 1]


# ============================================
# 3. sort() vs sorted() 차이점
# ============================================

# sort(): 제자리 정렬 (원본 변경, None 반환)
numbers1 = [5, 2, 8, 1, 9]
result = numbers1.sort()  # 원본을 정렬하고 None을 반환

print("sort() 후 numbers1:", numbers1)  # 출력: [1, 2, 5, 8, 9]
print("sort() 반환값:", result)  # 출력: None

# sorted(): 새 리스트 반환 (원본 유지)
numbers2 = [5, 2, 8, 1, 9]
result = sorted(numbers2)  # 새 리스트를 반환

print("sorted() 후 numbers2:", numbers2)  # 출력: [5, 2, 8, 1, 9]
print("sorted() 반환값:", result)  # 출력: [1, 2, 5, 8, 9]


# ============================================
# 4. 얕은 복사 개념
# ============================================

# 리스트 복사 방법 1: 대입 (참조 복사)
original = [1, 2, 3]
reference = original  # 같은 리스트를 가리킴

reference.append(4)
print("original:", original)  # 출력: [1, 2, 3, 4] (함께 변경!)
print("reference:", reference)  # 출력: [1, 2, 3, 4]

# 리스트 복사 방법 2: 슬라이싱 (얕은 복사)
original = [1, 2, 3]
copy = original[:]  # 새로운 리스트 생성

copy.append(4)
print("original:", original)  # 출력: [1, 2, 3] (변경 안됨)
print("copy:", copy)  # 출력: [1, 2, 3, 4]


# ============================================
# 5. 실전 예제: 성적 처리 시스템
# ============================================

# 학생 점수 데이터
student_scores = [88, 92, 76, 95, 84, 90, 78]

# 통계 계산
total_students = len(student_scores)
highest = max(student_scores)
lowest = min(student_scores)
total = sum(student_scores)
average = total / total_students

# 정렬 (원본 유지)
sorted_scores = sorted(student_scores, reverse=True)

# 결과 출력
print("\n=== 성적 처리 결과 ===")
print(f"총 학생 수: {total_students}명")
print(f"최고 점수: {highest}점")
print(f"최저 점수: {lowest}점")
print(f"평균 점수: {average:.1f}점")
print(f"점수 순위: {sorted_scores}")
