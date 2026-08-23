class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        cntleft=0
        sumleft=0
        for i in num[:n//2]:
            if i=="?":
                cntleft+=1
            else:
                sumleft+=int(i)
        cntright=0
        sumright=0
        for i in num[n//2:]:
            if i=="?":
                cntright+=1
            else:
                sumright+=int(i)
        if 2*(sumleft-sumright)==9*(cntright-cntleft):
            return False
        else:
            return True