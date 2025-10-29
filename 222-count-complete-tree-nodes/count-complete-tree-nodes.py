# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getHeight(node,height):
            while node:
                height+=1
                node=node.left
            return height
        if not root:
            return 0
        left=getHeight(root.left,0)
        right=getHeight(root.right,0)
        if left==right:
            return 2**left+self.countNodes(root.right)
        else:
            return 2**right+self.countNodes(root.left)

            