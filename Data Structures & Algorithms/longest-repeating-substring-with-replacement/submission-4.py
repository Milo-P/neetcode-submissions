class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0

        counts = {}
        longest_window = 0

        while r < len(s):

            counts[s[r]] = counts.get(s[r], 0) + 1
            largest_val = max(counts, key=counts.get) 
            window_size = (r - l) + 1

            # print(f"window size: {window_size}, counts[largest_val]: {counts[largest_val]}")
            valid = (window_size - (counts[largest_val])) <= k
            # print(valid)
            # print(l, r)

            while not valid:
                # print(longest_window)
                counts[s[l]] -= 1
                l += 1

                largest_val = max(counts, key=counts.get) 
                window_size = (r - l) + 1
                valid = (window_size - counts[largest_val]) <= k

                continue

            longest_window = max((r + 1) - l, longest_window)

            r += 1
        


        return longest_window