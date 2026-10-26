class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueIndex = {} # value : index

        for i, n in enumerate(nums):
            complement = target - n
            if complement in valueIndex:
                return [valueIndex[complement], i]
            valueIndex[n] = i