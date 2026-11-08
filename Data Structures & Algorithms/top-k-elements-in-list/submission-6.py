class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {} # element : frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num, freq in counts.items():
            # print(buckets)
            buckets[freq].append(num)

        # print(buckets)

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res

        return res