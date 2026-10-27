class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # Sort the array
        for i, a in enumerate(nums):
            # Skip duplicate values for the first element
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Early break: if 'a' is positive, we can never sum to 0
            if a > 0:
                break
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1 # Sum is too big, make it smaller
                elif three_sum < 0:
                    l += 1 # Sum is too small, make it bigger
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate values for the Left pointer
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res


