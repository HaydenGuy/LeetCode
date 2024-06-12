class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        elif len(nums) == 2:
            if nums[0] != nums[1]:
                return 0
            else:
                return 1
        
        output = 0

        for i, num in enumerate(nums):
            if i == len(nums):
                break

            for j in range(i+1, len(nums)):
                if nums[j] == nums[i] and i < j:
                    output += 1
                else:
                    pass

        return output


        # Using formula C(n,2)
        class Solution:
            def numIdenticalPairs(self, nums: List[int]) -> int:
                count = {}
                for num in nums:
                    count[num] = count.get(num, 0) + 1

                tp = 0      

                for key in count:
                    tp = tp + (count[key] * (count[key] - 1)) // 2

                return tp