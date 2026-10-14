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
                return 0
            if not node.left and not node.right:
                res=max(res,node.val)
                return node.val
            l=max(dfs(node.left),0) 
            r=max(dfs(node.right),0)
            res=max(res,l+node.val+r)
            return max(l,r)+node.val
        dfs(root)
        return res
            

# node     l       r          res         return
# -2  
# -1       
# -2       -1      0     