class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res=0
        for i,x in enumerate(nums[:-1]):
            lo=lower-x
            hi=upper-x
            lidx=bisect.bisect_left(nums,lo,i+1) 
            hidx=bisect.bisect_right(nums,hi,i+1) 
            print(lidx,hidx)
            res+=hidx-lidx
        return res