"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        res=0
        def dfs(node,path):
            nonlocal res
            if not node:
                return 0
            res=max(res,path)
            for child in node.children:
                dfs(child,path+1)
        dfs(root,1)
        return res
