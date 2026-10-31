class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            encoded += f'{strs[i]}£'

        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = [""]
        for c in s:
            if c == "£":
                decoded.append("")
            else:
                decoded[-1] += c
        
        decoded.pop()

        return decoded