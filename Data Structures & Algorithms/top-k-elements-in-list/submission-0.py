class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies = {}

        result = []

        for nb in nums:
            frequencies[nb] = frequencies.get(nb, 0) + 1

        frequencies = dict(sorted(frequencies.items(), key=lambda x:x[1], reverse=True))

        keys = list(frequencies.keys())
        for i in range(k):
            result.append(keys[i])

        return result