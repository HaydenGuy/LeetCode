class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        numbers = {}

        for i, num in enumerate(nums):
            if num in numbers:
                numbers[num] += 1
            else:
                numbers[num] = 1
                
        single = min(numbers, key=numbers.get)

        return single

        # XOR
        # xor = 0
        # for num in nums:
            # xor ^= num
        # 
        # return xor