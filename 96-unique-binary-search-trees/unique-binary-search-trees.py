class Solution:
    def numTrees(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):  #有 i 个节点时，一共有多少种 BST
            for j in range(1,i+1): #尝试让第 j 个位置成为根节点。
                dp[i]+=dp[j-1]*dp[i-j] #左子树种数*右子树种数
        return dp[n]