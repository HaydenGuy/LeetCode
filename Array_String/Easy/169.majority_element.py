class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = {}

        for i, num in enumerate(nums):
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        highest = max(counter, key=counter.get)

        return highest


        # nums.sort()
        # n = len(nums)
        # return nums[n//2]