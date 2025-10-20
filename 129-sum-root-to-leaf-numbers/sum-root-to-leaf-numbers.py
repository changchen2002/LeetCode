# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node,cur):
            if not node:
                return 0
            cur=cur*10+node.val
            if not node.left and not node.right:
                return cur
            l=dfs(node.left,cur)
            r=dfs(node.right,cur)  
            return l+r
        
        return dfs(root,0)

    
# node   cur    l    r
# 1       10    12  
# 2       12    0    0
# null               