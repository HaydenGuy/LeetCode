class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
         # Create a hashtable
        table = {}
        for number in nums1:
            # Checks if number in table and defaults to 0 if not, increments by 1
            table[number] = table.get(number, 0) + 1

        # Instantiate an empty list for result
        res = []
        for num in nums2:
            if num in table:
                if table[num] > 0:
                    res.append(num)
                    table[num] = table[num] - 1 # decrements the table value by 1
        return res