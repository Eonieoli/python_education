"""
Day 5 - 07교시: import 완전 정복
Practice 단계 - grade_utils.py

성적 처리를 위한 유틸리티 함수들을 정의합니다.
TODO 부분을 완성하세요!
"""

from typing import List


def calculate_class_average(grades: List[int]) -> float:
    """
    반 전체 평균 계산
    
    Args:
        grades: 성적 리스트
        
    Returns:
        평균 점수 (성적이 없으면 0.0)
    """
    # TODO: 반 전체 평균 계산
    # 힌트: if grades가 비어있지 않으면
    #       sum(grades) / len(grades)
    pass  # 이 줄을 삭제하고 코드 작성


def find_highest_grade(grades: List[int]) -> int:
    """
    최고 점수 찾기
    
    Args:
        grades: 성적 리스트
        
    Returns:
        최고 점수 (성적이 없으면 0)
    """
    if not grades:
        return 0
    return max(grades)


def find_lowest_grade(grades: List[int]) -> int:
    """
    최저 점수 찾기
    
    Args:
        grades: 성적 리스트
        
    Returns:
        최저 점수 (성적이 없으면 0)
    """
    # TODO: 최저 점수 찾기
    # 힌트: find_highest_grade와 비슷하지만 min() 사용
    pass  # 이 줄을 삭제하고 코드 작성


def count_passing_students(grades: List[int], passing_score: int = 60) -> int:
    """
    합격자 수 계산
    
    Args:
        grades: 성적 리스트
        passing_score: 합격 기준 점수 (기본값 60)
        
    Returns:
        합격자 수
    """
    # TODO: 합격자 수 세기
    # 힌트: passing_score 이상인 점수가 몇 개인지 세기
    #       리스트 컴프리헨션과 len() 사용
    pass  # 이 줄을 삭제하고 코드 작성


def get_grade_distribution(grades: List[int]) -> dict:
    """
    등급 분포 계산
    
    Args:
        grades: 성적 리스트
        
    Returns:
        등급별 학생 수 딕셔너리 {"A": 3, "B": 5, ...}
    """
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    for grade in grades:
        if grade >= 90:
            distribution["A"] += 1
        elif grade >= 80:
            distribution["B"] += 1
        elif grade >= 70:
            distribution["C"] += 1
        elif grade >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1
    
    return distribution


def format_grade_report(
    total_students: int,
    average: float,
    highest: int,
    lowest: int
) -> str:
    """
    성적 리포트 문자열 생성
    
    Args:
        total_students: 총 학생 수
        average: 평균 점수
        highest: 최고 점수
        lowest: 최저 점수
        
    Returns:
        포맷팅된 리포트 문자열
    """
    # TODO: f-string으로 리포트 생성
    # 힌트: 여러 줄 문자열 사용
    # 예시 형식:
    # 총 학생 수: 30명
    # 평균 점수: 75.5점
    # 최고 점수: 98점
    # 최저 점수: 45점
    pass  # 이 줄을 삭제하고 코드 작성


# 직접 실행 시 테스트
if __name__ == "__main__":
    print("=" * 50)
    print("grade_utils 함수 테스트")
    print("=" * 50)
    
    # 테스트 데이터
    test_grades = [85, 92, 78, 95, 88, 76, 90, 82, 70, 65]
    
    print(f"테스트 성적: {test_grades}\n")
    
    # 각 함수 테스트
    avg = calculate_class_average(test_grades)
    print(f"반 평균: {avg:.1f}점")
    
    highest = find_highest_grade(test_grades)
    print(f"최고 점수: {highest}점")
    
    lowest = find_lowest_grade(test_grades)
    print(f"최저 점수: {lowest}점")
    
    passing = count_passing_students(test_grades)
    print(f"합격자 수: {passing}명")
    
    distribution = get_grade_distribution(test_grades)
    print(f"\n등급 분포:")
    for grade_letter, count in distribution.items():
        print(f"  {grade_letter}: {count}명")
    
    # 리포트 생성
    print("\n" + "=" * 50)
    print("성적 리포트")
    print("=" * 50)
    report = format_grade_report(
        len(test_grades),
        avg,
        highest,
        lowest
    )
    print(report)
