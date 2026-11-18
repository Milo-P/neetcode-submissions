class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])
        
        for interval in intervals:
            if not res:
                res.append(interval)
                continue

            if interval[0] <= res[-1][1]:
                res[-1][1] =  max(res[-1][1], interval[1])
                continue

            res.append(interval)

        return res
