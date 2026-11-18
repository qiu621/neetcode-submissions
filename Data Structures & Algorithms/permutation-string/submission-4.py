class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == "":
            return True

        counts = Counter(s1)
        unique_chars = len(counts)
        
        for j, c in enumerate(s2):
            counts[c] -= 1
            if counts[c] == 0:
                unique_chars -= 1
            elif counts[c] == -1:
                unique_chars += 1 

            if j >= len(s1):
                front_index = j-len(s1)
                counts[s2[front_index]] += 1
                if counts[s2[front_index]] == 1:
                    unique_chars += 1
                elif counts[s2[front_index]] == 0:
                    unique_chars -= 1
                    
            if unique_chars == 0:
                return True
        return False


                

        
        return False