"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        res=0
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            a,b=0,0
            for child in node.children:
                cur=dfs(child)
                if cur>a:
                    a,b=cur,a
                elif cur>b:
                    b=cur
                res=max(res,a+b)
            return max(a,b)+1
        dfs(root)
        return res


            