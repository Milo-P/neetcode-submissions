class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        cum_product = 1
        product_arr = [1] * len(nums)

        for i in range(len(nums)):
            product_arr[i] = cum_product
            cum_product = nums[i] * cum_product

        # print(product_arr)
    
        cum_product = 1
        for i in range(len(nums) -1, -1, -1):

            product_arr[i] *= cum_product
            cum_product *= nums[i]

        # print(product_arr)

        return product_arr