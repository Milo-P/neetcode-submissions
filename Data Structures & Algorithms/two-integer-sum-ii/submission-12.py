class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        for i in range(len(numbers)):
            x,y = numbers[l], numbers[r]

            if (x + y) > target:
                r -= 1
            if (x + y) < target:
                l += 1
            if (x + y) == target:
                return [l+1,r+1]