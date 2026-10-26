class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countNums = {}

        for i in range(len(nums)):
            countNums[nums[i]] = i

        for i in range(len(nums)):
            indiceTwo = countNums.get((target - nums[i]), -1)
            if indiceTwo != -1 and i != indiceTwo:
                return [i, indiceTwo]