class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def maxelem(mat,m,n,col):
            maxvalue=-1
            inte=-1
            for i in range(0,n):
                if mat[i][col]>maxvalue:
                    maxvalue=mat[i][col]
                    inde=i
            return inde
        low=0
        m=len(mat[0])
        n=len(mat)
        high=m-1
        while (low<=high):
            mid=(low+high)//2
            row=maxelem(mat,m,n,mid)
            left = mat[row][mid - 1] if mid - 1 >= 0 else -1
            right = mat[row][mid + 1] if mid + 1 < m else -1
            if (mat[row][mid]>left and mat[row][mid]>right):
                return [row,mid]
            elif (mat[row][mid]<left):
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]