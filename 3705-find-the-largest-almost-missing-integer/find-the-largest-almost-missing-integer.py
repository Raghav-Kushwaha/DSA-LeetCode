class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k==len(nums):
            return max(nums)
        
        if k==1:
            res=-1
            for num in nums:
                if nums.count(num)==1:
                    res=max(res,num)
            return res
        
        if nums[0]==nums[-1]:
            return -1

        c0=nums.count(nums[0])
        c1=nums.count(nums[-1])

        if (c0==1 and c1==1):
            return max(nums[0],nums[-1])
        elif (c1>1 and c0==1):
            return nums[0]
        elif (c0>1 and c1==1):
            return nums[-1]
        return -1
        