# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def BST(root,low,high):
            if not root:
                return True
            if not low<root.val<high:
                return False
            return (BST(root.left,low,root.val) and
                    BST(root.right,root.val,high))
        return BST(root,float('-inf'),float('inf'))