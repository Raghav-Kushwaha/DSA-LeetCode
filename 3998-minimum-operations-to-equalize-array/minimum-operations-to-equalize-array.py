class Solution:
    def minOperations(self, nums: List[int]) -> int:
        prev=nums[0]
        bit=False
        for i in nums:
            if i!=prev:
                bit = True
            prev=i
        if bit:
            return 1
        else:
            return 0