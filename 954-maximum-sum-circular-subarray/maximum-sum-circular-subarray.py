class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMx=curMn=total=0
        mx=float('-inf')
        mn=float('inf')
        for num in nums:
            curMx=max(curMx+num,num)
            curMn=min(curMn+num,num) 
            mx=max(curMx,mx)
            mn=min(curMn,mn)
            total+=num
        return mx if mx<0 else max(mx,total-mn) 