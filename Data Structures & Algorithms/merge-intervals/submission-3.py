class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])
        
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
                continue

            if intervals[i][0] >= res[-1][0] and intervals[i][0] <= res[-1][1]:
                pop_l, pop_r = res.pop()
                res.append([pop_l, max(pop_r, intervals[i][1])])
                continue

            res.append(intervals[i])

        return res
