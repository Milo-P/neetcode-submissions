class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l, r = 1, len(nums) -1
        res = set()

        # print("sorted nums:", nums)
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and nums[i] > 0:
                continue

            l, r = i + 1, len(nums) -1
            
            while l < r:
                # print(i, l, r)
                # print(f"i: {nums[i]} l: {nums[l]} r: {nums[r]}")
                if (nums[i] + nums[l] + nums[r]) == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    # print("success!", res)
                    l += 1
                    continue
                
                elif (nums[i] + nums[l] + nums[r]) > 0:
                    r -= 1
                    continue

                elif (nums[i] + nums[l] + nums[r]) < 0:
                    l += 1
                    continue
            # print("l == r")

        return list(res)