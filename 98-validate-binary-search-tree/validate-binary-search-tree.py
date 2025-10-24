# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res=True
        prev=float('-inf')
        def inorder(node):
            nonlocal res,prev
            if not node:
                return
            inorder(node.left)
            if prev>=node.val:
                res=False
                return
            prev=node.val
            inorder(node.right)
        inorder(root)
        return res