class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        a=(need1*cost1)+(need2*cost2)
        b=max(need1,need2)*costBoth
        d=min(need1,need2)
        e=d*costBoth+((need1-d)*cost1)+((need2-d)*cost2)
        f=min(a,b,e)
        return f