class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        # O(n^2)
        # output = []
        # for i in range(len(nums)):
        #     counter = 0
        #     for j in range(len(nums)):
        #         if nums[i] > nums[j]:
        #             counter += 1
        #     output.append(counter)

        # return output

        sorted_nums = sorted(nums)
        count_smaller = {}
        for i, v in enumerate(sorted_nums):
            if v not in count_smaller:
                count_smaller[v] = i
        return [count_smaller[num] for num in nums]