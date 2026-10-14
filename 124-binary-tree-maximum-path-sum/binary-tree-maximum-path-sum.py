# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        res=root.val
        def dfs(node):
            nonlocal res
            if not node:
                return float('-inf')
            if not node.left and not node.right:
                return node.val
            l=dfs(node.left)  
            r=dfs(node.right)
            res=max(res,l,r,node.val,l+node.val,r+node.val,l+node.val+r)
            return max(l+node.val,r+node.val,node.val)
        dfs(root)
        return res
            

# node     l       r          res         return
# -2  
# -1       
# -2       -1      0     