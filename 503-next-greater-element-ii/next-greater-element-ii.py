class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        nums=nums+nums
        n=len(nums)
        nge=[0]*n
        st=[]
        for i in range (n-1,-1,-1):
            while(len(st)>0 and st[-1]<=nums[i]):
                st.pop()
            if len(st)==0:
                nge[i]=-1
            else:
                nge[i]=st[-1]
            st.append(nums[i])
        return nge[0:n//2]