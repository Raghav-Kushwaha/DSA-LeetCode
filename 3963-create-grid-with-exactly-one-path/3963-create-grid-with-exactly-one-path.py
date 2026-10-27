class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        answer=[]
        answer.append(n*".")
        for i in range (m-1):
            answer.append("#"*(n-1)+".")
        return answer
                          