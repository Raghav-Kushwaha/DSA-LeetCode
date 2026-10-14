class Solution:
    def maxSumOfSquares(self, num: int, total: int) -> str:
        if total>num*9:
            return ""
        result=[]
        for i in range(num):
            digit=min(9,total)
            result.append(str(digit))
            total-=digit
        return "".join(result)