class MinStack:

    def __init__(self):
        self._min_stack = []
        self._stack = []
        

    def push(self, val: int) -> None:
        i = len(self._stack)
        self._stack.append((i, val))
        if not self._min_stack or self._stack[-1][1] < self._min_stack[-1][1]:
            self._min_stack.append((i, val)) 
        

    def pop(self) -> None:
        i, val = self._stack.pop()
        if i == self._min_stack[-1][0]:
            self._min_stack.pop()
        return val
        

    def top(self) -> int:
        return self._stack[-1][1]

    def getMin(self) -> int:
        return self._min_stack[-1][1]
        
