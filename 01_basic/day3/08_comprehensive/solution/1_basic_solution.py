# 1_basic_solution.py

"""
Day 3 - 8교시: 종합 실습
🟢 기초 Problem - 간단한 메뉴 선택 시스템 (정답)
"""

# ============================================
# 주어진 데이터
# ============================================

# 메뉴와 가격 (딕셔너리)
menu = {
    1: {"name": "아메리카노", "price": 4000},
    2: {"name": "카페라떼", "price": 4500},
    3: {"name": "카푸치노", "price": 5000}
}


# ============================================
# 정답 코드
# ============================================

# 주문 목록을 저장할 빈 리스트
orders = []

# 총 금액을 저장할 변수 (0으로 초기화)
total = 0

# while문으로 반복 (무한 루프)
while True:
    # 메뉴 출력
    print("\n===== 카페 메뉴 =====")
    for num, item in menu.items():
        print(f"{num}. {item['name']} - {item['price']}원")
    
    print("0. 주문 완료")
    print("=====================")
    
    # 사용자 입력 받기
    choice = int(input("메뉴 번호를 선택하세요: "))
    
    # 0을 입력하면 주문 종료
    if choice == 0:
        break
    
    # 메뉴에 있는 번호인지 확인
    if choice in menu:
        # 해당 메뉴를 주문 목록에 추가
        orders.append(menu[choice]["name"])
        # 총 금액에 가격 더하기
        total += menu[choice]["price"]
        # 주문 확인 메시지
        print(f"{menu[choice]['name']}를 주문했습니다.")
    else:
        # 잘못된 번호
        print("잘못된 메뉴 번호입니다.")

# 주문 내역 출력
print("\n===== 주문 내역 =====")
print(", ".join(orders))
print(f"총 금액: {total}원")
