class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator 

        nums = []

        operators = {"+": operator.add,
                     "-": operator.sub,
                     "*": operator.mul,
                     "/": operator.truediv}

        for token in tokens:
            try:
                nums.append(int(token))

            except:
                new_num = int(operators[token](nums[-2], nums[-1]))
                nums.pop()
                nums.pop()
                nums.append(new_num)
            
            # print(f"token: {token}, nums: {nums}")

        return nums[0]