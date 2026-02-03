"""
Day 5 - 07교시: import 완전 정복
Practice 단계 - student_model.py

학생 정보를 관리하는 Student 클래스를 정의합니다.
TODO 부분을 완성하세요!
"""

from typing import List, Optional


class Student:
    """학생 클래스"""
    
    def __init__(self, name: str, student_id: str, grades: Optional[List[int]] = None):
        """
        학생 생성
        
        Args:
            name: 학생 이름
            student_id: 학번
            grades: 성적 리스트 (선택, 기본값은 빈 리스트)
        """
        self.name = name
        self.student_id = student_id
        # grades가 None이면 빈 리스트로 초기화
        self.grades = grades if grades is not None else []
    
    def add_grade(self, grade: int) -> None:
        """
        성적 추가
        
        Args:
            grade: 추가할 성적 (0~100)
        """
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print(f"경고: {grade}는 유효하지 않은 점수입니다 (0~100 사이여야 함)")
    
    def get_average(self) -> float:
        """
        평균 성적 계산
        
        Returns:
            평균 점수 (성적이 없으면 0.0)
        """
        # TODO: 평균 계산 로직 작성
        # 힌트: if self.grades가 비어있지 않으면
        #       sum(self.grades) / len(self.grades)
        #       비어있으면 0.0 반환
        pass  # 이 줄을 삭제하고 코드 작성
    
    def get_grade_letter(self) -> str:
        """
        평균 점수를 기준으로 등급 반환
        
        Returns:
            등급 문자열 (A, B, C, D, F)
        """
        # TODO: 등급 계산 로직 작성
        # 힌트: 평균을 구한 후
        #       90점 이상: "A"
        #       80점 이상: "B"
        #       70점 이상: "C"
        #       60점 이상: "D"
        #       60점 미만: "F"
        pass  # 이 줄을 삭제하고 코드 작성
    
    def get_info(self) -> str:
        """
        학생 정보 문자열 반환
        
        Returns:
            학생 정보 (이름, 학번, 평균, 등급)
        """
        avg = self.get_average()
        grade = self.get_grade_letter()
        return f"{self.name} ({self.student_id}) - 평균: {avg:.1f}점 ({grade})"


# 직접 실행 시 테스트
if __name__ == "__main__":
    print("=" * 50)
    print("Student 클래스 테스트")
    print("=" * 50)
    
    # 학생 생성
    student1 = Student("김철수", "2024001", [85, 90, 78])
    student2 = Student("이영희", "2024002")
    
    # 성적 추가
    student2.add_grade(92)
    student2.add_grade(88)
    student2.add_grade(95)
    
    # 정보 출력
    print(student1.get_info())
    print(student2.get_info())
    
    # 잘못된 점수 추가 시도
    print("\n잘못된 점수 추가 테스트:")
    student1.add_grade(105)  # 경고 메시지 출력
    student1.add_grade(-10)  # 경고 메시지 출력
