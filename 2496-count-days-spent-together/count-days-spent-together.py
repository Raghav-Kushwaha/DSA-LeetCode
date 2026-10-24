class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days=[31,28,31,30,31,30,31,31,30,31,30,31]
        def func(date):
            m=int(date[:2])
            d=int(date[3:])
            return sum(days[:m-1])+d
        a1=func(arriveAlice)
        a2=func(leaveAlice)
        b1=func(arriveBob)
        b2=func(leaveBob)

        start=max(a1,b1)
        end=min(a2,b2)
        return max(0,end-start+1)