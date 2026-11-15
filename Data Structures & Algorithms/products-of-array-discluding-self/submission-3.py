class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [1] * len(nums)
        suffix_array = [1] * len(nums)
        n = len(nums)
        for i in range(1, len(nums)):

            prefix_array[i] = prefix_array[i-1] * nums[i-1]
            suffix_array[n-i-1] = suffix_array[n-i] * nums[n-i]

        res = []
        for i in range(len(nums)):
            res.append(prefix_array[i] * suffix_array[i])
        return res 

        