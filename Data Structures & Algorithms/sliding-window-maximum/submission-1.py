class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        # algo: append (index, val)
        # if new val >= front val, or front stale, popleft
        res = []
        for i, num in enumerate(nums): 
            while d and d[0][0] <= i - k:
                d.popleft()
                
            while d and d[-1][1] <= num:
                d.pop()

            d.append((i, num))
                
            if i >= k - 1:
                res.append(max(d[0][1], d[-1][1]))
        return res

            
                
        