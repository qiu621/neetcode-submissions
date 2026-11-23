class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0

        for i, h in enumerate(heights):
            while stack and stack[-1][1] > h:
                _, height = stack.pop()  
                left = -1 if not stack else stack[-1][0]     
                best = max(best, (i-left-1) * height)
            stack.append((i, h))
            
        while stack:
            _, height = stack.pop()
            left = -1 if not stack else stack[-1][0]
            best = max(best, (len(heights)-left-1) * height)
        return best
