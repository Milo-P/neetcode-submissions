class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])
        
        for interval in intervals:
            if not res:
                res.append(interval)
                continue

            if interval[0] >= res[-1][0] and interval[0] <= res[-1][1]:
                pop_l, pop_r = res.pop()
                res.append([pop_l, max(pop_r, interval[1])])
                continue

            res.append(interval)

        return res
