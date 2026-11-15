class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
        tuple_to_anagrams = defaultdict(list)
        for s in strs:
            s_counter = Counter(s)
            char_map = tuple((i, s_counter[i]) for i in ALPHABET)
            tuple_to_anagrams[char_map].append(s)
        
        return list(tuple_to_anagrams.values())

        