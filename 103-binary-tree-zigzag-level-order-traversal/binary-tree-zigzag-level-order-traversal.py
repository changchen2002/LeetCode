# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        left2right=True
        res=[]
        q=deque([root])
        while q:
            cur=deque()
            for _ in range(len(q)):
                node=q.popleft()
                if left2right:
                    cur.append(node.val)   
                else:
                    cur.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(list(cur))
            left2right=not left2right
        return res