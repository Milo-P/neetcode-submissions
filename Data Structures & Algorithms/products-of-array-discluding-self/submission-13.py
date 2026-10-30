class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total = 1
        num_zeros = 0
        for num in nums:
            if num != 0:
                total *= num
            else:
                num_zeros += 1


        output = []
        for num in nums:
            if num != 0 and num_zeros == 0:
                output.append(int(total/num))
            elif num == 0 and num_zeros == 1:
                output.append(int(total))
            else:
                output.append(0)


        return output