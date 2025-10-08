class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if len(nums)==k:
            return max(nums)
        
        def canSplit(mid):
            subSum=0
            count=1
            for n in nums:
                subSum+=n
                if subSum>mid:
                    count+=1
                    subSum=n
            return count<=k
        
        l,r=max(nums),sum(nums)

        while l<r:
            m=l+(r-l)//2
            if canSplit(m):
                r=m
            else:
                l=m+1
        return l

        