class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_units = 0

        for i in range(len(heights)):
            # print(f"index l:{l}, index r:{r}")
            # print(f"height l:{heights[l]}, height r:{heights[r]}")

            if (r-l) * min(heights[l], heights[r]) > max_units:
                max_units = (r-l) * min(heights[l], heights[r])
                # print("new max: ", max_units)
            
            if r == l:
                return max_units

            if heights[r] < heights[l]:
                # print("l larger")
                r -= 1
                continue

            if heights[r] >= heights[l]:
                # print("r larger")
                l += 1
                continue
            

        return max_units
