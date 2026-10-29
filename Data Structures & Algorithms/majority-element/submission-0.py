class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) / 2
        elements = defaultdict(int)
        for i in nums:
            elements[i] += 1
            if elements[i] > majority:
                return i
        
