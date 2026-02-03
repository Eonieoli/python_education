# 2_practice.py

"""
Day 3 - 6교시: while문
Practice (강사와 함께 실습)

학습 목표:
- 숫자 맞추기 게임 만들기
- 메뉴 시스템 구현하기
"""

# ============================================
# 실습 1: 숫자 맞추기 게임 (전체 타이핑)
# ============================================

# 정답 숫자 설정
answer = 7

# 게임 시작
attempts = 0
max_attempts = 5

print("=== 숫자 맞추기 게임 ===")
print(f"1부터 10 사이의 숫자를 맞춰보세요! (기회: {max_attempts}번)")

# 게임 진행 (시연을 위해 하드코딩)
while attempts < max_attempts:
    # 실제로는 input()을 사용하지만 시연을 위해 숫자 지정
    if attempts == 0:
        guess = 5
    elif attempts == 1:
        guess = 8
    else:
        guess = 7
    
    attempts += 1
    print(f"\n{attempts}번째 시도: {guess}")
    
    if guess == answer:
        print(f"🎉 정답입니다! {attempts}번 만에 맞추셨습니다!")
        break
    elif guess < answer:
        print("⬆️ 더 큰 숫자입니다!")
    else:
        print("⬇️ 더 작은 숫자입니다!")
    
    # 마지막 시도인 경우
    if attempts == max_attempts and guess != answer:
        print(f"\n😢 게임 오버! 정답은 {answer}였습니다.")

# 출력:
# === 숫자 맞추기 게임 ===
# 1부터 10 사이의 숫자를 맞춰보세요! (기회: 5번)
# 
# 1번째 시도: 5
# ⬆️ 더 큰 숫자입니다!
# 
# 2번째 시도: 8
# ⬇️ 더 작은 숫자입니다!
# 
# 3번째 시도: 7
# 🎉 정답입니다! 3번 만에 맞추셨습니다!


# ============================================
# 실습 2: 메뉴 시스템 (TODO)
# ============================================

print("\n\n=== 카페 주문 시스템 ===")

# 메뉴와 가격
menu = {
    "1": ("아메리카노", 4000),
    "2": ("카페라떼", 4500),
    "3": ("카푸치노", 5000)
}

# 주문 목록
orders = []
total_price = 0

# TODO: while True로 무한 루프를 만드세요
while True:
    # 메뉴 출력
    print("\n[메뉴]")
    print("1. 아메리카노 (4000원)")
    print("2. 카페라떼 (4500원)")
    print("3. 카푸치노 (5000원)")
    print("0. 주문 완료")
    
    # 선택 (시연을 위한 하드코딩)
    # 실제로는 choice = input("선택: ")
    if len(orders) == 0:
        choice = "1"
    elif len(orders) == 1:
        choice = "2"
    else:
        choice = "0"
    
    print(f"선택: {choice}")
    
    # TODO: choice가 "0"이면 break하세요
    if choice == "0":
        break
    
    # TODO: menu에서 choice를 찾고, orders에 추가하세요
    # 힌트: if choice in menu:
    if choice in menu:
        item_name, item_price = menu[choice]
        orders.append(item_name)
        total_price += item_price
        print(f"✅ {item_name} 추가됨 (가격: {item_price}원)")
    else:
        print("❌ 잘못된 선택입니다!")

# 주문 결과 출력
print("\n=== 주문 내역 ===")
for i, order in enumerate(orders, 1):
    print(f"{i}. {order}")
print(f"총 금액: {total_price}원")

# 출력:
# === 카페 주문 시스템 ===
#
# [메뉴]
# 1. 아메리카노 (4000원)
# 2. 카페라떼 (4500원)
# 3. 카푸치노 (5000원)
# 0. 주문 완료
# 선택: 1
# ✅ 아메리카노 추가됨 (가격: 4000원)
#
# [메뉴]
# ...
# 선택: 2
# ✅ 카페라떼 추가됨 (가격: 4500원)
#
# [메뉴]
# ...
# 선택: 0
#
# === 주문 내역 ===
# 1. 아메리카노
# 2. 카페라떼
# 총 금액: 8500원
