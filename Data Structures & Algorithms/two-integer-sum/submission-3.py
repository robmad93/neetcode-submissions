class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # value : index
        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in seen:
                return [nums.index(needed), i]
        
            seen[nums[i]] = i

        