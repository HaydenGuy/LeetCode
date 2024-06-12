class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        
        output = 0
        t_dict = {char: i for i, char in enumerate(t)}

        for i, char in enumerate(s):
            output += abs(i - t_dict[char])

        return output