class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 1
        maxx=float('-inf')
        minn=float('inf')
        maxxind=0
        minnind=0
        for i in range (n):
            if nums[i]>maxx:
                maxx=nums[i]
                maxxind=i
            if nums[i]<minn:
                minn=nums[i]
                minnind=i
        x=min(minnind,maxxind)
        y=max(minnind,maxxind)
        return min(((n-y)+(x+1)),(n-x),(y+1))