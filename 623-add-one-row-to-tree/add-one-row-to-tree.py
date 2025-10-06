# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            return TreeNode(val,root)

        def dfs(node,depth):
            if not node:
                return None
            depth-=1
            if depth==1:
                newl=TreeNode(val,node.left)
                newr=TreeNode(val,None,node.right)
                node.left=newl
                node.right=newr
            else:
                dfs(node.left,depth)
                dfs(node.right,depth)
        dfs(root,depth)
        return root