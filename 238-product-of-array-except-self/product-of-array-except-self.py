class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        prev=1
        for i in range(n):
            res[i]=prev
            prev*=nums[i]
        
        prev=1
        for i in range(n-1,-1,-1):
            res[i]*=prev
            prev*=nums[i]
        return res