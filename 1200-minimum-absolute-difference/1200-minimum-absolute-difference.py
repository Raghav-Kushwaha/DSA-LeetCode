class Solution:
    def minimumAbsDifference(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        mindif=float('inf')
        res=[]
        for i in range(1,n):
            mindif=min(mindif,nums[i]-nums[i-1])
        for i in range(1,n):
            if (nums[i]-nums[i-1])==mindif:
                res.append([nums[i-1],nums[i]])
        return res