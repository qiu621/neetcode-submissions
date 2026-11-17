class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        max_count = 0
        best = 0
        i = 0 
        for j, c in enumerate(s):
            counts[s[j]] += 1
            max_count = max(counts[s[j]], max_count)
            while (j-i+1) - max_count > k:
                counts[s[i]] -= 1
                i += 1

            best = max(best, j-i+1)
        return best