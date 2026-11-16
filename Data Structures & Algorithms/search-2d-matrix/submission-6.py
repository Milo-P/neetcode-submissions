class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            # print(row)
            if row[0] <= target and row[len(row) - 1] >= target:
                
                l, r = 0, len(row) - 1
                
                while l <= r:

                    mid_idx = ((r - l) // 2) + l 
                    # print(l, r, mid_idx)

                    if row[mid_idx] == target:
                        return True

                    if row[mid_idx] < target:
                        l = mid_idx + 1
                    
                    else:
                        r = mid_idx - 1

        return False