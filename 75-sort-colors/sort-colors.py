class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=Counter(nums)
        i=0
        while i<len(nums):
            if i<count[0]:
                nums[i]=0
            elif i<count[0]+count[1]:
                nums[i]=1
            else:
                nums[i]=2
            i+=1
