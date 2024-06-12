class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # missingno = False
        # nums_set = set(nums)

        # for i in range(0, len(nums)+1):
        #     if i not in nums_set:
        #         missingno = i

        # return missingno
        
        # XOR
        # missing = len(nums)
        # for i, num in enumerate(nums):
        #     missing ^= i ^ num
        # return missing

        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])

        return res