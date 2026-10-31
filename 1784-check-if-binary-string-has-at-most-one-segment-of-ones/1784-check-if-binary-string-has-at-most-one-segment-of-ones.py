class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seg=0
        prev=s[0]
        for i in s:
            if i!=prev:
                seg+=1
            prev=i
            if seg>1:
                return False
        return True