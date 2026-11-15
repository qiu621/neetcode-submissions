ESCAPE = '@'
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "@")
            res.extend(s)
        return "".join(res) 
        
        


    def decode(self, s: str) -> List[str]:
        
        read_count = 0
        res = []

        i = 0
        while i < len(s):
            # Parse out the prepended number
            length = 0
            while s[i] != ESCAPE:
                length = length*10 + int(s[i])
                i += 1
            
            res.append(s[i+1:i+1+length])
            i += length + 1
        return res    
            
