class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        OPEN_TO_CLOSE = {"(" : ")", "{" : "}", "[" : "]"}
        for c in s:
            if c in OPEN_TO_CLOSE:
                stack.append(OPEN_TO_CLOSE[c])
            else:
                if not stack or stack.pop() != c:
                    return False
        return not stack