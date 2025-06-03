class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res=curmax=curmin=nums[0]
        for num in nums[1:]:
            if num<0:
                curmax,curmin=curmin,curmax
            curmax=max(num,curmax*num) #
            curmin=min(num,curmin*num)
            #对每个位置 i，只保留以 i 结尾的最大/最小乘积，并尝试更新全局最大值。
            res=max(res,curmax)
        return res
