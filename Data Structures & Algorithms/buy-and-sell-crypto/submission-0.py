class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        min_so_far = float('inf')
        for price in prices:
            best = max(price - min_so_far, best)
            min_so_far = min(min_so_far, price)
        return best

        