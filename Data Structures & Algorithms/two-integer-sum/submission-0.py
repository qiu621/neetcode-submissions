class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, val in enumerate(nums):
            if target - val in num_to_index:
                return [num_to_index[target-val], i]
            num_to_index[val] = i

        