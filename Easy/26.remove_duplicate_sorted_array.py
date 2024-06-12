class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # Empty list case
                return 0

        k = 1  # Initialize the count of unique elements

        for i in range(1, len(nums)):  # Start from the second element
            if nums[i] != nums[i - 1]:  # If current element is different from previous unique element
                nums[k] = nums[i]  # Move the current element to the next position after the last unique element
                k += 1  # Increment count of unique elements

        return k