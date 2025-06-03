class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    # DP: use Top-Down (recursion + memoization) unless: 	
	# The problem is clearly iterative in nature (e.g. coin change, knapsack)
    # this is like coin change, so we use bottom up

        dp=[True]+ [False]*len(s) #set a beginning and set it true
        for i in range(1,len(s)+1):
            for w in wordDict:
                start=i-len(w)
                if start>=0 and dp[start] and s[start:i]==w:
                    dp[i]=True
                    break
        return dp[-1] #dont mind about the index
