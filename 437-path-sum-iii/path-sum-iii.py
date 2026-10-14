# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefixSum=defaultdict(int)
        prefixSum[0]=1
        res=0
        def dfs(node,cur):
            nonlocal res
            if not node:
                return
            cur+=node.val
            res+=prefixSum[cur-targetSum]
            prefixSum[cur]+=1
            dfs(node.left,cur)
            dfs(node.right,cur)
            prefixSum[cur]-=1

        dfs(root,0)
        return res
            