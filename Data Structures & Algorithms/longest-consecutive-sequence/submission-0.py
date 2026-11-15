class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best = 0
        while nums_set:
            length = 1
            start = end = nums_set.pop() 

            while start-1 in nums_set:
                nums_set.remove(start-1)
                start -= 1
                length += 1
            while end+1 in nums_set:
                nums_set.remove(end+1)
                end += 1
                length += 1 
    
            best = max(best, length)
        return best



        