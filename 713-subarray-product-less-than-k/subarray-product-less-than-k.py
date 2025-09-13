class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k==0:
            return 0
        l=res=0  
        curr=1
        for r in range(len(nums)):
            curr*=nums[r] 
            while curr>=k and l<=r: 
                curr/=nums[l]
                l+=1
            res+=r-l+1
        return res