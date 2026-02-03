# 2_practice.py

"""
Day 1 - 4교시: 문자열 인덱싱/슬라이싱
Practice (강사와 함께 실습)

학습 목표:
- 첫 글자와 마지막 글자 추출하기
- 전화번호 포맷팅 (010-1234-5678)
- 파일명에서 확장자 추출하기
"""

# ============================================
# 실습 1: 첫 글자와 마지막 글자 추출
# ============================================

# 이름 입력
name = "김철수"

# 첫 글자 추출 (인덱스 0)
first_char = name[0]
print("첫 글자:", first_char)  # 출력: 첫 글자: 김

# 마지막 글자 추출 (음수 인덱스 -1)
last_char = name[-1]
print("마지막 글자:", last_char)  # 출력: 마지막 글자: 수

# 성씨 확인
surname = name[0]
print(f"{name}님의 성씨는 '{surname}' 입니다")
# 출력: 김철수님의 성씨는 '김' 입니다


# ============================================
# 실습 2: 전화번호 포맷팅 (010-1234-5678)
# ============================================

# 전화번호 (숫자만 있는 상태)
phone = "01012345678"

# 슬라이싱으로 나누기
part1 = phone[0:3]    # 010
part2 = phone[3:7]    # 1234
part3 = phone[7:11]   # 5678

# 하이픈으로 연결
formatted_phone = part1 + "-" + part2 + "-" + part3

print("원본:", phone)  # 출력: 원본: 01012345678
print("포맷:", formatted_phone)  # 출력: 포맷: 010-1234-5678


# ============================================
# 실습 3: 파일명에서 확장자 추출
# ============================================

# 파일명
filename = "presentation.pptx"

# 확장자 추출 (마지막 5글자)
extension = filename[-5:]
print("확장자:", extension)  # 출력: 확장자: .pptx

# 파일명만 추출 (확장자 제외)
name_only = filename[:-5]
print("파일명:", name_only)  # 출력: 파일명: presentation

# 다른 예제
filename2 = "photo.jpg"
extension2 = filename2[-4:]  # .jpg
name_only2 = filename2[:-4]  # photo

print(f"{filename2} → 이름: {name_only2}, 확장자: {extension2}")
# 출력: photo.jpg → 이름: photo, 확장자: .jpg
