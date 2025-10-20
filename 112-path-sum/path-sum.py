# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,path):
            if not node:
                return False
            path+=node.val
            if not node.left and not node.right:
                if path==targetSum:
                    return True
                else:
                    return False

            return dfs(node.left,path) or dfs(node.right,path)
        return dfs(root,0)