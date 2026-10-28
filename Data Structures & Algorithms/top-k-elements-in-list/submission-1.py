class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {} # element : frequency

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        top_k = (sorted(frequencies, key=frequencies.get))
        top_k = top_k[-k:]

        return top_k