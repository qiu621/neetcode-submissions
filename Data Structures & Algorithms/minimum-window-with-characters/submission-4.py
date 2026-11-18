class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = Counter(t)
        window = Counter()
        if need == window:
            return s

        best_window = None
        i = 0
        
        for j in range(len(s)):
            val = s[j]
            if val in need:
                window[val] += 1

            while i <= j and (s[i] not in need or window[s[i]] > need[s[i]]):
                if s[i] in need:
                    window[s[i]] -= 1
                i += 1
            
            if all(window[c] >= need[c] for c in need):
                if best_window is None:
                    best_window = (i, j+1)
                elif best_window[1] - best_window[0] > j+1-i:
                    best_window = (i, j+1)
        if best_window is None:
            return ""
        return s[best_window[0]:best_window[1]]                


        