class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        # Initialize variables
        break_point = 0  # This keeps track of the start of the current range
        k = 0  # This keeps track of the previous element's index
        l = []  # This will store the resulting list of ranges

        # Handle the edge case where there's only one element in nums
        if len(nums) == 1:
            l.append(f"{nums[0]}")  # If there's only one element, it's its own range

        # Iterate over the nums list starting from the second element
        for i in range(1, len(nums)):
            
            # Check if the current element is not consecutive with the previous element
            if nums[i] - nums[k] > 1:
                # If the start and end of the current range are the same, it's a single number
                if nums[break_point] == nums[k]:
                    l.append(f"{nums[k]}")  # Append the single number
                else:
                    l.append(f"{nums[break_point]}->{nums[k]}")  # Append the range
                # Update the break_point to the current index
                break_point = i

            # Check if we are at the last element of the list
            if i == len(nums) - 1:
                # Handle the last range or single number
                if nums[break_point] == nums[i]:
                    l.append(f"{nums[i]}")  # Append the single number
                else:
                    l.append(f"{nums[break_point]}->{nums[i]}")  # Append the range

            # Move to the next element
            k += 1

        return l