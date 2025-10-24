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
            nonlocal res,prev #prev必须在外面,不然回到上一层就没了. 以及res,prev都得写nonlocal
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