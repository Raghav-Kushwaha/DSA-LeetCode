class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        z=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[z],nums[i]=nums[i],nums[z]
                z+=1
        """
        Do not return anything, modify nums in-place instead.
        """
        