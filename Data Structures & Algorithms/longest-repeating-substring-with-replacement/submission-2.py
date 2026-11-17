class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        best = 0
        i = 0 
        for j, c in enumerate(s):
            counts[s[j]] += 1
            while (j-i+1) - max(counts.values()) > k:
                counts[s[i]] -= 1
                i += 1

            best = max(best, j-i+1)
        return best