class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jewels = {i for i in jewels}
        output = 0
        
        for i in stones:
            if i in jewels:
                output += 1

        return output