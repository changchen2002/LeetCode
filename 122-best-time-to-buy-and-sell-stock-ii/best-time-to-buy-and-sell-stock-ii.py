class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=l=0
        for r in range(len(prices)):
            if prices[r]>prices[l]:
                res+=prices[r]-prices[l]
            l=r
        return res