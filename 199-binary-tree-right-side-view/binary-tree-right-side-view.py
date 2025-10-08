# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque([root])
        res=[]
        while q:
            add=True
            for i in range(len(q)-1,-1,-1):
                node=q.popleft()
                if add:
                    res.append(node.val)
                    add=False
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return res