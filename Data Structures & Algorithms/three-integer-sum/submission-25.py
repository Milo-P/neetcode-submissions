class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l, r = 1, len(nums) -1
        res = []

        # print("sorted nums:", nums)
        for i, num in enumerate(nums):
            if num == nums[i-1] and i > 0:
                continue

            l, r = i + 1, len(nums) -1
            
            while l < r:
                # print(i, l, r)
                # print(f"i: {nums[i]} l: {nums[l]} r: {nums[r]}")
                
                if (num + nums[l] + nums[r]) == 0:
                    if [num, nums[l], nums[r]] not in res:
                        res.append([num, nums[l], nums[r]])
                    # print("success!", res)
                    l += 1
                    continue
                
                elif (num + nums[l] + nums[r]) > 0:
                    r -= 1
                    continue

                elif (num + nums[l] + nums[r]) < 0:
                    l += 1
                    continue
            # print("l == r")

        return res