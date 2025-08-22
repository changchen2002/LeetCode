class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmx=curmn=mx=mn=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>0:
                curmx,curmn=max(curmx*nums[i],nums[i]),min(curmn*nums[i],nums[i])
            else:
                curmx,curmn=max(curmn*nums[i],nums[i]),min(curmx*nums[i],nums[i]) 
            mx=max(mx,curmx)
            mn=min(mn,curmn)
        return mx