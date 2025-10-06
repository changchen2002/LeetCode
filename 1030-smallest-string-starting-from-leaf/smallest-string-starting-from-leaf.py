# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res="~"
        def dfs(node,path):
            nonlocal res
            if not node:
                return
            path.append(chr(ord('a')+node.val))
            if not node.left and not node.right:
                s="".join(reversed(path))
                res=min(res,s)                
            dfs(node.left,path)
            dfs(node.right,path)
            path.pop()
        
        dfs(root,[])
        return res