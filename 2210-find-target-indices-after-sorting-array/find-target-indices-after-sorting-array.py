class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n):
            if nums[i]==target:
                res.append(i)
        return res