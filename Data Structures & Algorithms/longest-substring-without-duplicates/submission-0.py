class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        best = 0
        i = 0
        for j, c in enumerate(s):
            if c in seen:
                while c in seen:
                    seen.remove(s[i])
                    i += 1
            seen.add(c)
            best = max (j-i+1, best)
        return best         