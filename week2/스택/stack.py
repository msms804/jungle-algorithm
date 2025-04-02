class Stack:
    def __init__(self):
        self.items =[]
        self.ptr = -1
    
    def push(self, item):
        self.items.append(item)
        self.ptr += 1
    
    def pop(self):
        """스택에서 요소를 제거하고 반환 (비어있으면 None 반환)"""
        if not self.is_empty():
            self.ptr -= 1
            return self.items.pop()
        return None
    
    def peek(self):
        """스택의 최상단 요소를 반환 (비어있으면 None 반환)"""
        if not self.is_empty():
            return self.items[self.ptr]
        return None
    
    def is_empty(self):
        """스택이 비어있는지 확인"""
        return self.ptr == -1
    
    def size(self):
        """스택의 크기 반환"""
        return self.ptr + 1
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.peek())
print(stack.is_empty())
print(stack.size())