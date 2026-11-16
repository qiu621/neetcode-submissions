class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            start = i+1
            end = len(nums) - 1
            while start < end:
                if nums[start] + nums[end] < target:
                    start += 1
                elif nums[start] + nums[end] > target:
                    end -= 1
                else:
                    res.append([-target, nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[start-1] == nums[start]:
                        start += 1
                    while start < end and nums[end+1] == nums[end]:
                        end -= 1
        return res
        