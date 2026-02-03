# 3_exercise_solution.py

"""
Day 1 - 4교시: 문자열 인덱싱/슬라이싱
Exercise - 이메일 처리 및 문자열 역순 (정답)
"""

# ============================================
# 문제 1: 이메일에서 사용자 이름 추출
# ============================================

# 주어진 이메일 주소
email = "john.doe@company.com"

# @ 기호의 위치
at_position = 8

# @ 앞부분만 슬라이싱
username = email[:at_position]

# 결과 출력
print("이메일:", email)
print("사용자 이름:", username)  # 출력: 사용자 이름: john.doe


# ============================================
# 문제 2: 문자열 역순 출력
# ============================================

# 주어진 문자열
text = "Python"

# 문자열을 역순으로 뒤집기
reversed_text = text[::-1]

# 결과 출력
print("원본:", text)
print("역순:", reversed_text)  # 출력: 역순: nohtyP


# ============================================
# 추가 도전: 회문(palindrome) 확인
# ============================================

# 회문 단어
word = "level"

# 역순으로 뒤집기
reversed_word = word[::-1]

# 원본과 역순이 같은지 비교
is_palindrome = word == reversed_word

# 결과 출력
print(f"단어: {word}")
print(f"역순: {reversed_word}")
print(f"회문 여부: {is_palindrome}")  # 출력: 회문 여부: True
