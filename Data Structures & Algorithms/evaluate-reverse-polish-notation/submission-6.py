class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if val == '*':
                curr = stack.pop() * stack.pop()
            elif val == "+":
                curr = stack.pop() + stack.pop()
            elif val == "-":
                second, first = stack.pop(), stack.pop()
                curr = first - second
            elif val == "/":
                second, first = stack.pop(), stack.pop()
                curr = int(first / second)
            else:
                curr = int(val)
            stack.append(curr)
        return stack[-1]
        