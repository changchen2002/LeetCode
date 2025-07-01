class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        dpLeft,dpRight=[0]*(n),[0]*(n)
        dpLeft[0],dpRight[-1]=nums[0],nums[-1]
        for i in range(1,n):
            dpLeft[i]=dpLeft[i-1]+nums[i]
        for i in range(n-2,-1,-1):
            dpRight[i]=dpRight[i+1]+nums[i]
        
        for i in range(n-1):
            if dpLeft[i]>=dpRight[i+1]:
                res+=1
        return res