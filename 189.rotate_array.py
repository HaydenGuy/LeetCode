class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # O(n^2)
        # while k != 0:
            # nums.insert(0, nums.pop())
            # k -= 1

        # O(n)
        k %= len(nums)
    
        nums[:] = nums[-k:] + nums[:-k]