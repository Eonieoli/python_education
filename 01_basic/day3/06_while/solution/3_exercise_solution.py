# 3_exercise_solution.py

"""
Day 3 - 6교시: while문
Exercise 1 - 비밀번호 재입력 시스템 (정답)
"""

# ============================================
# 정답 코드
# ============================================

# 시연을 위한 데이터
attempts_data = [
    ("1234", "5678"),  # 첫 번째 시도 (불일치)
    ("abcd", "abc"),   # 두 번째 시도 (불일치)
    ("pass", "pass")   # 세 번째 시도 (일치)
]

attempt_count = 0

# 비밀번호 일치할 때까지 반복
while True:
    # 비밀번호 입력
    password1, password2 = attempts_data[attempt_count]
    attempt_count += 1
    
    print(f"비밀번호 입력: {password1}")
    print(f"비밀번호 확인: {password2}")
    
    # 비밀번호 일치 여부 확인
    if password1 == password2:
        print("✅ 비밀번호 설정 완료!")
        break  # 일치하면 종료
    else:
        print("❌ 비밀번호가 일치하지 않습니다. 다시 입력하세요.")
    
    print()

# 출력:
# 비밀번호 입력: 1234
# 비밀번호 확인: 5678
# ❌ 비밀번호가 일치하지 않습니다. 다시 입력하세요.
# 
# 비밀번호 입력: abcd
# 비밀번호 확인: abc
# ❌ 비밀번호가 일치하지 않습니다. 다시 입력하세요.
# 
# 비밀번호 입력: pass
# 비밀번호 확인: pass
# ✅ 비밀번호 설정 완료!


print("\n" + "="*50)
print()


"""
Exercise 2 - 양수 입력받기 (정답)
"""

# ============================================
# 정답 코드
# ============================================

# 시연을 위한 데이터
test_numbers = [-5, 0, -3, 10]
index = 0

# 양수를 입력받을 때까지 반복
while True:
    # 숫자 입력
    number = test_numbers[index]
    index += 1
    
    print(f"숫자 입력: {number}")
    
    # 양수인지 확인
    if number > 0:
        print(f"✅ 입력 완료! 입력한 숫자: {number}")
        break  # 양수면 종료
    else:
        print("❌ 양수를 입력하세요!")
    
    print()

# 출력:
# 숫자 입력: -5
# ❌ 양수를 입력하세요!
# 
# 숫자 입력: 0
# ❌ 양수를 입력하세요!
# 
# 숫자 입력: -3
# ❌ 양수를 입력하세요!
# 
# 숫자 입력: 10
# ✅ 입력 완료! 입력한 숫자: 10
