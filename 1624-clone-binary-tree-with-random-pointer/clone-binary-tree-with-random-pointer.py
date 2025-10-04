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
            copy=NodeCopy(node.val)
            visit[node]=copy
            copy.left=buildTree(node.left)
            copy.right=buildTree(node.right)
            return copy

        def setRandom(node):
            if not node:
                return None
            copy=visit[node]
            if node.random:
                copy.random=visit[node.random]
            setRandom(node.left)
            setRandom(node.right)

        copy=buildTree(root)
        setRandom(root)
        return copy      