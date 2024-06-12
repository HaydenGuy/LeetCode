class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        end = len(needle)
        
        if haystack == needle:
            return 0

        if len(haystack) < end:
            return -1

        if len(haystack) == end and haystack != needle:
            return -1
           
        i = 0

        while i < len(haystack):
            check = haystack[i:end]

            if check == needle:
                return i
            elif end > len(haystack):
                return -1
            else:
                i += 1
                end += 1

        return -1