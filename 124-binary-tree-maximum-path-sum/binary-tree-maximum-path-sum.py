# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res=float('-inf')
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            l=dfs(node.left) if node.left else float('-inf')
            r=dfs(node.right) if node.right else float('-inf')
            res=max(res,l,r,l+r+node.val,node.val,l+node.val,r+node.val)
            return max(l+node.val,r+node.val,node.val)
        dfs(root)
        return res if res!=float('-inf') else root.val