class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I'm thinking of creating a seperate set of letters for each group

        # Now I'm thinking of taking each of the letters from a word, and creating a
        # dictionary entry for it
        
        groups = {} # sorted_string : [string_anagrams]

        for i, string in enumerate(strs):
            sorted_string = ''.join(sorted(string))

            groups.setdefault(sorted_string, []).append(string)
        
        return list(groups.values())