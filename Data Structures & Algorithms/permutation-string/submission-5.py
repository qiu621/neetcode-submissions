class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        n = len(s1)
        window = Counter(s2[:n])

        if need == window:
            return True

        
        for j in range(n, len(s2)):
            window[s2[j]] += 1
            window[s2[j-n]] -= 1
            if window == need:
                return True
        return False


                

        
        return False