class Stack():

    def __init__(self) -> None:
        self.stack = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0
    
    def push(self, obj) -> None:
        self.stack.append(obj)

    def pop(self) -> object:
        return self.stack.pop()
    
    def peek(self) -> object:
        return self.stack[-1]
    
    def size(self) -> int:
        return len(self.stack)
    