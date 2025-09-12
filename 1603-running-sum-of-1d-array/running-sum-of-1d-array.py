class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        cur=0
        for n in nums:
            cur+=n
            res.append(cur)
        return res