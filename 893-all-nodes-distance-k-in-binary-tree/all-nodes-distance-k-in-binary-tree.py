# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #“深度差” ≠ “路径距离”。
        graph=defaultdict(list)
        def build(node):
            if not node:
                return
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                build(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                build(node.right)
        build(root)

        q=deque([(target,0)])
        vis={target}
        res=[]
        while q:
            for _ in range(len(q)):
                node,dis=q.popleft()
                if dis==k:
                    res.append(node.val)
                elif dis<k:
                    for nei in graph[node]:
                        if nei not in vis:
                            vis.add(nei)
                            q.append((nei,dis+1))
        return res
                