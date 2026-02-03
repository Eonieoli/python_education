# 2_practice.py

"""
Day 5 - 5교시: 예외 처리
Practice (강사와 함께 실습)

학습 목표:
- 안전한 사용자 입력 처리
- 파일 읽기 예외 처리
- 클래스 메서드에서 예외 처리
"""

# ============================================
# 실습 1: 안전한 입력 처리 (전체 타이핑)
# ============================================

def safe_input_number() -> int:
    """사용자로부터 안전하게 숫자를 입력받는 함수"""
    while True:
        try:
            # 입력 받기
            user_input = input("숫자를 입력하세요: ")
            # 정수로 변환 시도
            number = int(user_input)
            return number
        except ValueError:
            # 변환 실패 시
            print("❌ 잘못된 입력입니다. 숫자를 입력하세요.")

# 테스트 (실제로 입력받으려면 주석 해제)
# number = safe_input_number()
# print(f"입력한 숫자: {number}")


# ============================================
# 실습 2: 파일 읽기 예외 처리 (TODO)
# ============================================

def read_user_file(filename: str) -> str:
    """파일을 안전하게 읽는 함수"""
    # TODO: try-except-finally로 파일 읽기를 구현하세요
    # 힌트 1: try 블록에서 파일을 열고 읽기
    # 힌트 2: except FileNotFoundError로 에러 처리
    # 힌트 3: finally에서 파일 닫기
    
    f = None
    try:
        f = open(filename, 'r', encoding='utf-8')
        content = f.read()
        return content
    except FileNotFoundError as e:
        print(f"❌ 파일을 찾을 수 없습니다: {filename}")
        return ""
    finally:
        if f is not None:
            f.close()

# 테스트
print("=== 파일 읽기 ===")
result = read_user_file("test.txt")  # 없는 파일이므로 에러 처리
print()


# ============================================
# 실습 3: 클래스 메서드 예외 처리 (TODO)
# ============================================

class ShoppingCart:
    """장바구니 클래스"""
    
    def __init__(self):
        """빈 장바구니로 시작"""
        self.items: list[str] = []
    
    def add_item(self, item: str) -> None:
        """상품을 장바구니에 추가"""
        # TODO: item이 빈 문자열이면 ValueError 발생
        # 힌트: if not item: raise ValueError("상품명이 비어있습니다")
        
        if not item:
            raise ValueError("상품명이 비어있습니다")
        
        self.items.append(item)
        print(f"✅ '{item}' 추가 완료")
    
    def remove_item(self, item: str) -> None:
        """상품을 장바구니에서 제거"""
        # TODO: item이 items에 없으면 ValueError 발생
        # 힌트 1: if item not in self.items:
        # 힌트 2: raise ValueError(f"'{item}'이(가) 장바구니에 없습니다")
        
        if item not in self.items:
            raise ValueError(f"'{item}'이(가) 장바구니에 없습니다")
        
        self.items.remove(item)
        print(f"✅ '{item}' 제거 완료")

# 테스트
print("=== 장바구니 ===")
cart = ShoppingCart()

try:
    cart.add_item("사과")      # 출력: ✅ '사과' 추가 완료
    cart.add_item("바나나")    # 출력: ✅ '바나나' 추가 완료
    cart.remove_item("딸기")   # ValueError 발생!
except ValueError as e:
    print(f"❌ 오류: {e}")

try:
    cart.add_item("")          # ValueError 발생!
except ValueError as e:
    print(f"❌ 오류: {e}")
