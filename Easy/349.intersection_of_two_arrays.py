class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        output = []

        for num in set_nums1:
            if num in set_nums2:
                output.append(num)

        return output

        # Can be one line using the & for sets which returns all same present values
        # return set(nums1) & set(nums2)
