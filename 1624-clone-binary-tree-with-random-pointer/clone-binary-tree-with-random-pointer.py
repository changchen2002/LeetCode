# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        visit={}
        def buildTree(node):
            if not node:
                return None
            if node in visit:
                return visit[node]
            copy=NodeCopy(node.val)
            visit[node]=copy
            copy.left=buildTree(node.left)
            copy.right=buildTree(node.right)
            copy.random=buildTree(node.random)
            return copy

        return buildTree(root)
