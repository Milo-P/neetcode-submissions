class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = defaultdict(list)

        all_nums = set(nums)
        
        for num in all_nums:
            # print(num)
            if ((num - 1) not in all_nums):
                longest_sequence[num].append(num)
                # print(f"{num} appended")
                
                current_num = num + 1
                while (current_num) in all_nums:
                    # print(f"{current_num} appended to {num} key")
                    longest_sequence[num].append(current_num)
                    current_num += 1

        leng = max((len(v) for v in longest_sequence.values()), default=0)
        return leng