class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur=sum(nums[:k])
        res=cur/k
        l=0
        for r in range(k,len(nums)):
            cur+=nums[r]
            cur-=nums[l]
            l+=1
            res=max(res,cur/k)

        return res