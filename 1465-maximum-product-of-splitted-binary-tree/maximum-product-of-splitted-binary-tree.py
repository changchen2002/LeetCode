# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total=0
        def calculateSum(node):
            nonlocal total
            if not node:
                return 0
            total+=node.val
            calculateSum(node.left)
            calculateSum(node.right)       
        calculateSum(root)

        res=float('-inf')
        def subTreeSum(node):
            nonlocal res
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            l=subTreeSum(node.left)
            r=subTreeSum(node.right)
            sub=node.val+l+r
            res=max(res,(total-l)*l,(total-r)*r,(total-sub)*sub)
            return sub
        subTreeSum(root)

        return res%(10**9+7)

