class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:

            mid_idx = ((l + r) // 2)

            if nums[mid_idx] == target:
                return mid_idx

            if nums[mid_idx] < target:
                l = mid_idx + 1

            else:
                r = mid_idx - 1
        
        return -1