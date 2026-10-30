class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        value_count = {} # value : count
        frequency = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            value_count[num] = value_count.get(num, 0) + 1
        for num, count in value_count.items():
            frequency[count].append(num)

        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res