class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            nums[i]=nums[i]**2
        nums.sort()
        s=0
        for i in range(n//2):
            s+=nums[i]
        d=0
        for i in range((n//2),n):
            d+=nums[i]
        return d-s
