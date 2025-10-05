# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node,add):
            # nonlocal add
            if not node:
                return 0
            add=add*10+node.val
            if not node.left and not node.right:
                print("leaf:",node.val,add)
                return add
            print("enter:", node.val, add)
            l=dfs(node.left,add)
            print("left done:",node.val, l)
            r=dfs(node.right,add)
            print("right done:", node.val, r)
            print("return:", node.val,l+r)
            return l+r
        return dfs(root,0)
        

            