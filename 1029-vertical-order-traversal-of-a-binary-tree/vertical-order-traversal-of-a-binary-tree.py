# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque([(root,0,0)])
        nodes=[]
        while q:
            node,r,c=q.popleft()
            if node:
                nodes.append((c,r,node.val))
                q.append((node.left,r+1,c-1))
                q.append((node.right,r+1,c+1))
        
        nodes.sort()
        res=defaultdict(list)
        for c,r,val in nodes:
            res[c].append(val)
        
        return [res[c] for c in sorted(res)]

