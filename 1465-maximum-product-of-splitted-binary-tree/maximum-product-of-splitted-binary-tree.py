# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        modulo=10**9+7
        res=float('-inf')
        def getSum(node):
            if not node:
                return 0
            return getSum(node.left)+getSum(node.right)+node.val

        total=getSum(root)
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            l=dfs(node.left)
            r=dfs(node.right)
            res=max(res,(total-l)*l,(total-r)*r)
            return l+r+node.val
        dfs(root)
        return res%modulo
            