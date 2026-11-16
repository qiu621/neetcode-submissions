class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        best = 0
        while i < j:
            best = max(best, min(heights[i], heights[j]) * (j-i))
            if heights[i] >= heights[j]:
                j -= 1
            else:
                i += 1


        return best
        
        