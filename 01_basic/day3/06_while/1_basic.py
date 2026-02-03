# 1_basic.py

"""
Day 3 - 6교시: while문
Basic (강사 시연용)

학습 목표:
- while문의 기본 문법 이해
- break와 continue 사용법
- 재시도 로직 패턴 익히기
- for문과의 차이점 이해
"""

# ============================================
# 1. while문 기본
# ============================================

# while문은 조건이 True인 동안 반복합니다
count = 1
while count <= 5:
    print(f"{count}번째 반복")
    count += 1  # 반드시 조건을 변경해야 합니다!
# 출력:
# 1번째 반복
# 2번째 반복
# 3번째 반복
# 4번째 반복
# 5번째 반복

print()  # 빈 줄

# for문과 while문 비교
# for문: 반복 횟수를 알 때
for i in range(1, 6):
    print(f"for: {i}")

print()

# while문: 조건이 만족될 때까지
num = 1
while num <= 5:
    print(f"while: {num}")
    num += 1


# ============================================
# 2. break - 반복문 즉시 종료
# ============================================

print("\n=== break 예제 ===")

# 사용자 입력을 받다가 'quit'을 입력하면 종료
count = 0
while True:  # 무한 루프
    count += 1
    print(f"{count}번째 시도")
    
    # 5번 시도하면 종료
    if count >= 5:
        print("5번 시도 완료!")
        break  # while문 즉시 종료
# 출력:
# 1번째 시도
# 2번째 시도
# 3번째 시도
# 4번째 시도
# 5번째 시도
# 5번 시도 완료!


# ============================================
# 3. continue - 다음 반복으로 건너뛰기
# ============================================

print("\n=== continue 예제 ===")

# 1부터 10까지 중 홀수만 출력
num = 0
while num < 10:
    num += 1
    
    # 짝수면 건너뛰기
    if num % 2 == 0:
        continue  # 아래 코드를 실행하지 않고 다음 반복으로
    
    print(num)  # 홀수만 출력됨
# 출력: 1 3 5 7 9


# ============================================
# 4. 실전 예제: 재시도 로직 (로그인 시스템)
# ============================================

print("\n=== 실전 예제: 로그인 시스템 ===")

# 로그인 정보
correct_password = "1234"
max_attempts = 3  # 최대 시도 횟수

# 로그인 시도
attempts = 0
while attempts < max_attempts:
    # 비밀번호 입력 (실제로는 input() 사용)
    # 여기서는 시연을 위해 하드코딩
    if attempts == 0:
        password = "0000"  # 첫 번째 시도 (틀림)
    elif attempts == 1:
        password = "9999"  # 두 번째 시도 (틀림)
    else:
        password = "1234"  # 세 번째 시도 (맞음)
    
    attempts += 1
    print(f"\n{attempts}번째 시도: {password}")
    
    if password == correct_password:
        print("✅ 로그인 성공!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"❌ 비밀번호가 틀렸습니다. (남은 횟수: {remaining}회)")
        else:
            print("❌ 로그인 실패! 횟수 초과")

# 출력:
# 1번째 시도: 0000
# ❌ 비밀번호가 틀렸습니다. (남은 횟수: 2회)
# 
# 2번째 시도: 9999
# ❌ 비밀번호가 틀렸습니다. (남은 횟수: 1회)
# 
# 3번째 시도: 1234
# ✅ 로그인 성공!
