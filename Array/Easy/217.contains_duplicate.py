class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        numbers = {}

        for num in nums:
            if num not in numbers:
                numbers[num] = 1
            else:
                return True
        
        return False
