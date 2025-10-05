# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        def backtrack(node,path):
            if not node:
                return
            path.append(str(node.val))

            if not node.left and not node.right:
                res.append("->".join(path[:]))
            backtrack(node.left,path)
            backtrack(node.right,path)
            path.pop()
        backtrack(root,[])
        return res
