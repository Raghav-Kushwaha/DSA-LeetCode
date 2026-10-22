class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        st=[]
        n=len(nums)
        for i in range(n):
            while (len(st)>0 and k>0 and (st[-1])>nums[i]):
                st.pop()
                k=k-1
            st.append(nums[i])
        while(k>0):
            st.pop()
            k=k-1
            #3rd Edge case
        if (len(st)==0):
            return '0'
            #1st Edge CASE
        res=""
        while(len(st)>0):
            res=res+st[-1]
            st.pop()
        while len(res)!=0 and res[-1]=='0':
            res=res[:-1]
        res=res[::-1]
        if len(res)==0:
            return '0'
        else:
            return res