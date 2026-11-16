class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        bottoms = []

        for i, h in enumerate(height):
            while bottoms and h > bottoms[-1][1]:
                _, bottom = bottoms.pop()
                if bottoms:
                    trapped += (i - bottoms[-1][0] - 1) * (min(h, bottoms[-1][1]) - bottom)
            bottoms.append((i, h))

        return trapped


        