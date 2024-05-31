class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        appear = {}

        for num in nums:
            if num in appear:
                appear[num] += 1
            else:
                appear[num] = 1

        for i in nums[:]:
            if appear.get(i) > 2:
                nums.remove(i)
                appear[i] -= 1