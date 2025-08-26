class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=set(nums)
        res=1
        for n in nums:
            if n-1 not in nums:
                cur=1
                while n+1 in nums:
                    cur+=1
                    n+=1
                res=max(res,cur)
        return res