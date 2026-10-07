class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        n=len(intervals)
        count=0
        maxend=0
        for _,i in intervals:
            if i<=maxend:
                count+=1
            else:
                maxend=i
        return n-count

