class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_even=float('inf')
        min_odd=float('inf')
        for i in nums1:
            if i%2==1:
                min_odd=min(min_odd,i)
            else:
                min_even=min(min_even,i)
        if (min_odd==float('inf') or min_even==float('inf')):
            return True
        return min_odd<min_even