# 3_advanced_solution.py

"""
Day 3 - 8교시: 종합 실습
🔴 도전 Problem - 숫자 맞추기 게임 (정답)
"""

# ============================================
# 주어진 데이터
# ============================================

import random

# 컴퓨터가 선택한 숫자 (1-100 사이)
answer = random.randint(1, 100)


# ============================================
# 정답 코드
# ============================================

# 게임 시작 메시지
print("===== 숫자 맞추기 게임 =====")
print("1부터 100 사이의 숫자를 맞춰보세요!")

# 최대 시도 횟수
max_tries = 7

# 시도 횟수를 저장할 변수
tries = 0

# 게임 루프
while tries < max_tries:
    # 남은 기회 출력
    remaining = max_tries - tries
    print(f"\n남은 기회: {remaining}번")
    
    # 사용자 입력
    guess = int(input("숫자를 입력하세요: "))
    
    # 시도 횟수 증가
    tries += 1
    
    # 정답 확인
    if guess == answer:
        print(f"정답입니다! {tries}번 만에 맞추셨습니다! 🎉")
        break
    elif guess < answer:
        print("UP! 더 큰 숫자입니다.")
    else:
        print("DOWN! 더 작은 숫자입니다.")
else:
    # while문이 break 없이 종료되면 실행
    print(f"\n아쉽습니다! 정답은 {answer}였습니다.")
