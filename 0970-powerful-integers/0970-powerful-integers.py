class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res=set()
        curr1=1
        cntx=0
        curr2=1
        cnty=0
        while (curr1<bound):
            cntx+=1
            if x==1:
                break
            curr1*=x
            
        while (curr2<bound):
            cnty+=1
            if y==1:
                break
            curr2*=y
            
        for i in range (cntx):
            for j in range (cnty):
                if x**i + y**j <=bound:
                    res.add((x**i)+(y**j))
        return list(res)