class Solution:
    def checkDivisibility(self, n: int) -> bool:
        add=0
        mult=1
        temp=n
        while (temp>0):
            digit=temp%10
            add+=digit
            mult*=digit
            temp=temp//10
        if n%(add+mult)==0:
            return True
        else:
            return False