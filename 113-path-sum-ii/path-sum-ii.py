# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res=[]
        def dfs(node,path,s):
            if not node:
                return
            path.append(node.val)
            s+=node.val
            if not node.left and not node.right:
                if s==targetSum:
                    res.append(path[:])
            dfs(node.left,path,s)
            dfs(node.right,path,s)
            path.pop()

        dfs(root,[],0)
        return res

# node   path          s     res
# 1       [1]          1     []
# 2       [1,2]        3
# 1       [1]          1
# 3       [1,3]        4  
# 1

