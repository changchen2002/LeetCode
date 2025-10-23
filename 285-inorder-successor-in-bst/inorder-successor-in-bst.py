# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        prev=None
        res=None
        def inorder(node):
            nonlocal prev,res
            if not node:
                return        
            inorder(node.left)
            if prev==p and not res:
                res=node
                return
            prev=node
            inorder(node.right)

        inorder(root)
        return res
        

            