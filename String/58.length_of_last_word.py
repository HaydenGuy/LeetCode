import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        stripped = re.sub(r'^\s+|\s+$', '', s)

        count = 0

        for i in stripped[::-1]:
            if i == " ":
                return count
            else:
                count += 1

        return count