class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # My original
        # nums_set = set(nums)
        # best = 0
        # while nums_set:
        #     length = 1
        #     start = end = nums_set.pop() 

        #     while start-1 in nums_set:
        #         nums_set.remove(start-1)
        #         start -= 1
        #         length += 1
        #     while end+1 in nums_set:
        #         nums_set.remove(end+1)
        #         end += 1
        #         length += 1 
    
        #     best = max(best, length)
        # return best



        # Hashset, big trick is a first check that the start isn't in the set
        nums_set = set(nums)

        longest = 0
        for num in nums:
            if num-1 not in nums_set:
                length = 0
                while num in nums_set:
                    length += 1
                    num += 1
                longest = max(longest, length)
        return longest