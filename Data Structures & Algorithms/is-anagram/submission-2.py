class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        letters_s = {}
        letters_t = {}

        for x in s:
            if x in letters_s:
                letters_s[x] += 1
            else:
                letters_s[x] = 0

        for x in t:
            if x in letters_t:
                letters_t[x] += 1
            else:
                letters_t[x] = 0

        return letters_s == letters_t