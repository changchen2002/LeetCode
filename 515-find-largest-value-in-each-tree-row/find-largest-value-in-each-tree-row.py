# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=collections.deque()
        q.append(root)
        largest=float('-inf')
        while q:
            for _ in range(len(q)):
                node=q.popleft()
                if node:
                    largest=max(largest,node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if largest!=float('-inf'):
                res.append(largest)
            largest=float('-inf')
        return res