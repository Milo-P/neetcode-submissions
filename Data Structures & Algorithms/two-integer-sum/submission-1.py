class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for l in range(len(nums)):
                if nums[i] + nums[l] == target and i != l:
                    return [i, l]