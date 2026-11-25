class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies = {}
        freq_arr = [[] for i in range(len(nums)+1)]
        result = []

        for nb in nums:
            frequencies[nb] = frequencies.get(nb, 0) + 1

        for nb, freq in frequencies.items():
            freq_arr[freq].append(nb)

        for i in range(len(freq_arr)-1, 0, -1):
            for nb in freq_arr[i]:
                result.append(nb)
                if len(result) == k:
                    return result