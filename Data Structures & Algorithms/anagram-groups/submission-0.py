class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        letters = defaultdict(list)

        for word in strs:
            sortedWord = "".join(sorted(word))
            letters[sortedWord].append(word)

        return list(letters.values())
