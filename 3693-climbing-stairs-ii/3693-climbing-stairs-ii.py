class Solution:
    def climbStairs(self, n: int, cost: List[int]) -> int:
        prev1=0
        prev3=float('inf')
        prev2=float('inf')
        for j in range(1,n+1):
            step=cost[j-1]
            curr=prev1+1
            curr=min(curr,prev2+4)
            curr=min(curr,prev3+9)
            curr+=step

            prev3=prev2
            prev2=prev1
            prev1=curr
        return prev1