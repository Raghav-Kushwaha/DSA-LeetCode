class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        def checkNGE(arr1,x):
            st=-1
            for i in arr1:
                if i==x and st==-1:
                    st=x
                if st==x and i>x:
                    return i
            return -1
        res=[]
        for j in nums1:
            res.append(checkNGE(nums2,j))
        return res