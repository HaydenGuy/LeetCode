class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # O(n^2)
        # count = nums.count(0)
        
        # while count != 0:
        #     nums.remove(0)
        #     count -= 1
        #     nums.append(0)


        # Two Pointer O(n)
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
        return nums