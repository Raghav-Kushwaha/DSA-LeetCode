class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n=len(nums)
        if n==0:
            return -1
        if n==1:
            return 0
        total=sum(nums)
        left=0
        for i in range(n):
            right=total-left-nums[i]
            if right==left:
                return i
            left+=nums[i]
        return -1