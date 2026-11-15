class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = nums[i-1] * res[i-1]
        
        end_product = 1
        for j in range(n-1, -1, -1):
            res[j] *= end_product
            end_product *= nums[j]
        return res
