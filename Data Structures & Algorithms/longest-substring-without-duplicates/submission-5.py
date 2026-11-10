class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sub = 0

        current_chars = ""

        for c in s:
            # If character is already in current_chars, update longest_sub
            # find the index of the duplicate character, and slice the current_chars
            # string from that char + 1, maintaining the chars in front of it.
            if c in current_chars:
                if len(current_chars) > longest_sub:
                    longest_sub = len(current_chars)
                # print("c:", c)
                # print("before prefix removed:", current_chars)
                removal_idx = current_chars.find(c)
                current_chars = current_chars[removal_idx + 1:]
                # print("after pref removed:", current_chars)
            current_chars += c
        
            # print(f"c: {c}, current_chars: {current_chars}")
            # print(f"longest_sub: {longest_sub}\n")
        
        if len(current_chars) > longest_sub:
                    longest_sub = len(current_chars)

        return longest_sub