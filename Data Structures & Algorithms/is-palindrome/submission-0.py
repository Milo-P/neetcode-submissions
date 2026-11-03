class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []

        for c in s:
            if c.isalnum():
                word.append(c)

        reversed_word = word.copy()
        reversed_word.reverse()

        word = ''.join(word)
        reversed_word = ''.join(reversed_word)

        
        if word.lower() == reversed_word.lower():
            return True

        return False