class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # A base case is ALWAYS needed for recursion.
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        # Recursion example below.
        left_sorted = self.sortArray(nums[:mid])   # This PAUSES the current function.
        right_sorted = self.sortArray(nums[mid:])  # This won't run until "left" is completely finished.

        def merge(left, right):
            i, j = 0, 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            # Add any leftovers from left and/or right        
            res.extend(left[i:])
            res.extend(right[j:])
            return res

        return merge(left_sorted, right_sorted)
