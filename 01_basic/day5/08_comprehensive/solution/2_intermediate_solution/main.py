"""
main.py - 메인 실행 파일 (해답)

User와 Product 클래스를 사용하여 쇼핑몰 관리 시스템을 테스트합니다.
"""

from models import User, Product


def main() -> None:
    """쇼핑몰 관리 시스템 메인 함수"""
    print("=== 쇼핑몰 관리 시스템 테스트 ===\n")
    
    # 1. 사용자 생성
    print("1. 사용자 생성")
    user1 = User("홍길동", "gildong@example.com", "U001")
    print(user1)
    
    # 2. 상품 생성
    print("\n2. 상품 생성")
    product1 = Product("노트북", 1200000, 10, "P001")
    print(product1)
    
    # 3. 구매 테스트
    print("\n3. 구매 테스트")
    product1.purchase(2)
    total_value = product1.get_total_value()
    print(f"재고 총 가치: {total_value}원")
    
    # 4. 예외 처리 테스트
    print("\n4. 예외 처리 테스트")
    
    # 4-1. 재고 부족 에러
    try:
        product1.purchase(20)  # 현재 재고 8개인데 20개 구매 시도
    except ValueError as e:
        print(f"재고 부족 에러: {e}")
    
    # 4-2. 잘못된 이메일 에러
    try:
        user2 = User("김철수", "invalidemail.com", "U002")  # @ 없음
    except ValueError as e:
        print(f"잘못된 이메일 에러: {e}")
    
    # 4-3. 잘못된 가격 에러
    try:
        product2 = Product("마우스", -10000, 5, "P002")  # 음수 가격
    except ValueError as e:
        print(f"잘못된 가격 에러: {e}")


if __name__ == "__main__":
    main()
