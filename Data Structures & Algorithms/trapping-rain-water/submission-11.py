class Solution:
    def trap(self, height: List[int]) -> int:
        # bottoms
        # trapped = 0
        # bottoms = []

        # for i, h in enumerate(height):
        #     while bottoms and h > bottoms[-1][1]:
        #         _, bottom = bottoms.pop()
        #         if bottoms:
        #             trapped += (i - bottoms[-1][0] - 1) * (min(h, bottoms[-1][1]) - bottom)
        #     bottoms.append((i, h))

        # return trapped

        # Trapped at i is min largest left of i, largest right of i

        # n = len(height)
        # largest_left = [0] * len(height)
        # largest_right = [0] * len(height)

        # for i in range(1, len(height)):
        #     largest_left[i] = max(largest_left[i-1], height[i-1])
        #     largest_right[n-i-1] = max(largest_right[n-i], height[n-i])

        # trapped = 0
        # for i in range(len(height)):
        #     trapped += max(min(largest_left[i], largest_right[i]) - height[i],0)
        # return trapped 
        left, right = 0, len(height) - 1
        trapped = 0
        largest_left, largest_right = height[0], height[-1]
        while left < right:
            if height[left] < height[right]:
                largest_left = max(largest_left, height[left])
                trapped += max(largest_left - height[left], 0)
                left += 1
            else:
                largest_right = max(largest_right, height[right])
                trapped += max(largest_right- height[right], 0)
                right -= 1
        return trapped


        