"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        visit={}
        def dfs(node):
            if not node:
                return None
            if node in visit:
                return visit[node]
            copy=Node(node.val)
            for child in node.children:
                copy.children.append(dfs(child))
            return copy
        return dfs(root)