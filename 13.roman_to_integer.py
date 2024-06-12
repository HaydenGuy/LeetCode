class Solution:
    def romanToInt(self, s: str) -> int:
        
        romans = {
                "I":1,
                "IV":4,
                "V":5,
                "IX":9,
                "X":10,
                "XL":40,
                "L":50,
                "XC":90,
                "C":100,
                "CD":400,
                "D":500,
                "CM":900,
                "M":1000
        }

        number = 0
        i = 0

        while i < len(s):
            if s[i:i+2] in romans:
                two_char = s[i:i+2]
                number += romans[two_char]
                i += 2
            else:
                char = s[i]
                number += romans[char]
                i += 1
        
        return number