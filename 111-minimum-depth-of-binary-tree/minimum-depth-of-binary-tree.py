# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res=float('inf')
        def dfs(node,depth):
            nonlocal res
            if not node:
                return 0
            depth+=1
            if not node.left and not node.right:
                res=min(res,depth)
            dfs(node.left,depth)
            dfs(node.right,depth)
        dfs(root,0)
        return res