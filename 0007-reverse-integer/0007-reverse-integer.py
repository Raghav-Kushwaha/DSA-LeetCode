class Solution(object):
    def reverse(self, x):
        a=0
        if x>=0:
            x=str(x)
            x=x[::-1]
            x=int(x)
        else :
            x=-x
            x=str(x)
            x=x[::-1]
            x=int(x)
            x=-x
        if x>2147483648:
            return a
        elif x<-2147483648:
            return a
        return x



        