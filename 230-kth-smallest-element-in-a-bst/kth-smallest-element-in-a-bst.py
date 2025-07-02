# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[None]
        i=[0]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            i[0]+=1
            if i[0]==k:
                res[0]=root.val
                return
            dfs(root.right)
        dfs(root)
        return res[0]