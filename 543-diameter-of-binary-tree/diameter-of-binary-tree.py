# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            l,r=0,0
            l+=dfs(node.left)
            r+=dfs(node.right)
            res=max(res,l+r)
            return max(l,r)+1
        dfs(root)
        return res
    
# node     path      l      r       res
# 1                  2      1
# 2                  1      1
# 4 
# 5
# 3                                    