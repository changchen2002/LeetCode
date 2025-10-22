class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        hold,sold,rest=-prices[0],0,0
        for p in prices[1:]:
            preHold,preSold,preRest=hold,sold,rest
            hold=max(preHold,preRest-p) #不卖出/买入剩下的钱
            sold=preHold+p  #今天卖出
            rest=max(preRest,preSold) #今天的休息来源于昨天休息或昨天刚卖出
        
        return max(sold,rest)
