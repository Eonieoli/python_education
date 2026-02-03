# 2_practice.py

"""
Day 5 - 3교시: 클래스 심화
Practice (강사와 함께 실습)

학습 목표:
- 장바구니 클래스 구현
- TODO 리스트 클래스 구현
- 타입 힌트 완벽 적용
"""

from typing import List, Dict

# ============================================
# 실습 1: 간단한 장바구니 클래스
# ============================================

class Cart:
    """간단한 장바구니 클래스"""
    
    def __init__(self):
        """장바구니 초기화"""
        self.items: List[str] = []
    
    def add(self, item: str) -> None:
        """상품 추가"""
        self.items.append(item)
        print(f"{item} 추가됨")
    
    def remove(self, item: str) -> None:
        """상품 제거"""
        if item in self.items:
            self.items.remove(item)
            print(f"{item} 제거됨")
        else:
            print(f"{item}이(가) 장바구니에 없습니다")
    
    def show(self) -> None:
        """장바구니 내역 출력"""
        print(f"장바구니: {self.items}")

# 테스트
cart = Cart()
cart.add("사과")     # 출력: 사과 추가됨
cart.add("바나나")   # 출력: 바나나 추가됨
cart.show()          # 출력: 장바구니: ['사과', '바나나']
cart.remove("사과")  # 출력: 사과 제거됨
cart.show()          # 출력: 장바구니: ['바나나']


# ============================================
# 실습 2: TODO 리스트 클래스 (TODO 방식)
# ============================================

class TodoList:
    """할 일 관리 클래스"""
    
    # TODO: __init__ 메서드를 작성하세요
    # 힌트: self.todos를 빈 리스트로 초기화
    def __init__(self):
        """TODO 리스트 초기화"""
        self.todos: List[Dict[str, any]] = []
    
    # TODO: add_todo 메서드를 작성하세요
    # 매개변수: title (str), priority (int, 기본값 1)
    # 힌트: 딕셔너리로 저장 {"title": ..., "priority": ..., "done": False}
    def add_todo(self, title: str, priority: int = 1) -> None:
        """할 일 추가"""
        todo = {
            "title": title,
            "priority": priority,
            "done": False
        }
        self.todos.append(todo)
        print(f"'{title}' 추가됨 (우선순위: {priority})")
    
    # TODO: complete_todo 메서드를 작성하세요
    # 매개변수: title (str)
    # 힌트: todos를 순회하며 title이 일치하면 done을 True로
    def complete_todo(self, title: str) -> None:
        """할 일 완료 처리"""
        for todo in self.todos:
            if todo["title"] == title:
                todo["done"] = True
                print(f"'{title}' 완료!")
                return
        print(f"'{title}'을(를) 찾을 수 없습니다")
    
    # TODO: show_todos 메서드를 작성하세요
    # 힌트: todos를 순회하며 출력
    def show_todos(self) -> None:
        """할 일 목록 출력"""
        print("\n=== TODO 리스트 ===")
        if not self.todos:
            print("할 일이 없습니다")
            return
        
        for i, todo in enumerate(self.todos, 1):
            status = "✓" if todo["done"] else " "
            print(f"{i}. [{status}] {todo['title']} (우선순위: {todo['priority']})")
        print()

# 테스트
todo_list = TodoList()
todo_list.add_todo("FastAPI 공부", 1)     # 출력: 'FastAPI 공부' 추가됨 (우선순위: 1)
todo_list.add_todo("운동하기", 2)         # 출력: '운동하기' 추가됨 (우선순위: 2)
todo_list.add_todo("독서", 3)             # 출력: '독서' 추가됨 (우선순위: 3)
todo_list.show_todos()
# 출력:
# === TODO 리스트 ===
# 1. [ ] FastAPI 공부 (우선순위: 1)
# 2. [ ] 운동하기 (우선순위: 2)
# 3. [ ] 독서 (우선순위: 3)

todo_list.complete_todo("운동하기")       # 출력: '운동하기' 완료!
todo_list.show_todos()
# 출력:
# === TODO 리스트 ===
# 1. [ ] FastAPI 공부 (우선순위: 1)
# 2. [✓] 운동하기 (우선순위: 2)
# 3. [ ] 독서 (우선순위: 3)
