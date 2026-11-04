class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums = sorted(nums)
        
        i, l, r = 0, 1, len(nums) - 1

        while i != len(nums) - 1:
            # print(f"i: {i}, l: {l}, r: {r}")
            if l == r:
                # print("l == r, next iter")
                i += 1
                l, r = i + 1, len(nums) - 1
                continue
            
            if nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            
            elif nums[i] + nums[l] + nums[r] < 0:
                l += 1
            
            elif nums[i] + nums[l] + nums[r] == 0:
                if sorted([nums[i], nums[l], nums[r]]) not in res:
                    res.append(sorted([nums[i], nums[l], nums[r]]))
                l += 1
                
                # print("match")

        return res