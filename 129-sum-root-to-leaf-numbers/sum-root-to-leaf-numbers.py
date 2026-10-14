# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        s=0
        def dfs(node,num):
            nonlocal s
            if not node:
                return
            num=10*num+node.val
            if not node.left and not node.right:
                s+=num
                return
            dfs(node.left,num)
            dfs(node.right,num)
        dfs(root,0)
        return s

# node    num    s    
# 1        1     0
# 2        12    12
# 3        13    25

