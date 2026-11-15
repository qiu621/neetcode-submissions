class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        count_to_nums = defaultdict(list)
        max_count = -float('inf')
        for num, count in counts.items():
            max_count = max(count, max_count)
            count_to_nums[count].append(num)

        res = []
        while k > 0:
            if max_count in count_to_nums:
                res.extend(count_to_nums[max_count])
            k -= len(count_to_nums[max_count])
            max_count -= 1
        return res
