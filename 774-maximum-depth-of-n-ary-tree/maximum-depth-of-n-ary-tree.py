"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.res=0
        def dfs(node,path):
            if not node:
                return 0
            path+=1
            self.res=max(self.res,path)
            for c in node.children:
                dfs(c,path)

        dfs(root,0)
        return self.res