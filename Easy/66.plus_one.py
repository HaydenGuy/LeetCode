class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        total = ""
        
        for i in digits:
            total += str(i)

        total = int(total) + 1

        total = list(str(total))

        for i, num in enumerate(total):
            total[i] = int(num)
        
        return total