class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        mid = (l + r) // 2

        current_min = nums[r]

        while l < r:            
            
            mid = (l + r) // 2
            # print(l, r, mid)

            if nums[mid] > nums[r]:
                l = mid + 1

            elif nums[mid] < nums[r]:
                r = mid
                current_min = min(current_min, nums[r])

            # print(current_min)

            
        return current_min




        