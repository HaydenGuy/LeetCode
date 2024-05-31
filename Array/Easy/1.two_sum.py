class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # O(n^2)
        # for i in range(len(nums)):
            # for j in range(i+1, len(nums)):
                # if nums[i] + nums[j] == target:
                    # return [i, j]

        # 0(n^2)
        # for i in range(len(nums)):
            # j = target - nums[i]
            # 
            # if j in nums[i+1:]:
                # return [i, nums.index(j, i+1)]

        sums = {}  # Dictionary to store complements and their indices
        for i, num in enumerate(nums):
            j = target - num  # Calculate the complement
            if j in sums:
                return [i, sums[j]]
            sums[num] = i  # Store the current number and its index in the sums dictionary
