# 3_exercise_solution.py

"""
Day 4 - 3교시: 매개변수 - 위치와 기본값
Exercise - 성적 등급 계산 함수 (정답)
"""

# ============================================
# 정답 코드
# ============================================

def calculate_grade(score, bonus=0, pass_score=60):
    """
    성적 등급 계산 함수
    
    매개변수:
        score: 기본 점수
        bonus: 가산점 (기본값: 0)
        pass_score: 합격 기준 점수 (기본값: 60)
    
    반환값:
        등급과 합격 여부를 포함한 문자열
    """
    # 1. 최종 점수 계산
    final_score = score + bonus
    
    # 2. 등급 판정
    if final_score >= 90:
        grade = "A"
    elif final_score >= 80:
        grade = "B"
    elif final_score >= 70:
        grade = "C"
    elif final_score >= pass_score:
        grade = "D"
    else:
        grade = "F"
    
    # 3. 합격 여부 판정
    if final_score >= pass_score:
        pass_status = "합격"
    else:
        pass_status = "불합격"
    
    # 4. 결과 문자열 반환
    return f"점수: {final_score}, 등급: {grade}, 합격 여부: {pass_status}"


# ============================================
# 테스트 코드
# ============================================

# 테스트 1: 기본값 사용
result1 = calculate_grade(75)
print(result1)  # 출력: 점수: 75, 등급: C, 합격 여부: 합격

# 테스트 2: 보너스 점수 추가
result2 = calculate_grade(80, 5)
print(result2)  # 출력: 점수: 85, 등급: B, 합격 여부: 합격

# 테스트 3: 불합격 케이스
result3 = calculate_grade(55)
print(result3)  # 출력: 점수: 55, 등급: F, 합격 여부: 불합격

# 테스트 4: 합격 기준 점수 변경
result4 = calculate_grade(68, 2, 70)
print(result4)  # 출력: 점수: 70, 등급: C, 합격 여부: 합격
