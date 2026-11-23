class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            while stack and stack[-1][-1] < val:
                past_index, _ = stack.pop()
                res[past_index] = i - past_index


            stack.append((i, val))             
        return res

        