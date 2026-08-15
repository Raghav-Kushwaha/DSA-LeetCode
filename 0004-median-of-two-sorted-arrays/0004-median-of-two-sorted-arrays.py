class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1 = nums1 + nums2
        nums1.sort()
        l=len(nums1)
        if l%2==1:
            return nums1[(l-1)/2]
        else :
            return (float(nums1[(l/2)])+float(nums1[(l/2)-1]))/2
        
