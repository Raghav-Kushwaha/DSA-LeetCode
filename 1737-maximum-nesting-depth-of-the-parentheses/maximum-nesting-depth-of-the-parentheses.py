class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        maxdepth=0
        for i in s:
            prevmax=count
            if i=="(":
                count+=1
                maxdepth=max(count,maxdepth)
            elif i==")":
                count-=1
        return maxdepth