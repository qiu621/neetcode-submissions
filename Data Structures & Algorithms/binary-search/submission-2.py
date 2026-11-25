class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)

        while low < high:
            mid = (low + high ) // 2
            print(low, mid, high)
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1

        return low if low < len(nums) and nums[low] == target else -1