class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # temp, index
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            
            while stack and stack[-1][0] < temp:
                stack_temp, stack_idx = stack.pop()
                res[stack_idx] = i - stack_idx

            stack.append([temp, i])

        return res