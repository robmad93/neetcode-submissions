class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        output = [1] * len(nums)
        for i in range(0, len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        for j in range(len(nums) - 1, -1, -1): # Range is exclusive of the stop figure. So to get to index 0, need to set stop at -1.
            output[j] *= postfix
            postfix *= nums[j]
        return output
