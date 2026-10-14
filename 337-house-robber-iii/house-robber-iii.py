# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dfs(node):
            if not node:
                return [0,0]
            l=dfs(node.left)
            r=dfs(node.right)
            rob=node.val+l[1]+r[1]
            skip=max(l[0],l[1])+max(r[0],r[1])
            return [rob,skip]
        return max(dfs(root))