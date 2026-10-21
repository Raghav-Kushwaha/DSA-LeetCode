class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st=[]
        n=len(asteroids)
        for ast in asteroids:
            alive = True
            while alive and st and st[-1]>0 and ast<0:
                if st[-1]<-ast:
                    st.pop()
                elif st[-1]==-ast:
                    st.pop()
                    alive= False
                else:
                    alive=False
            if alive:
                st.append(ast)
        return st