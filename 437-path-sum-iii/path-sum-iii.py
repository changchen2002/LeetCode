# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        hashmap=defaultdict(int)
        hashmap[0]=1
        res=0
        def dfs(node,cur):
            nonlocal res
            if not node:
                return
            cur+=node.val
            res+=hashmap[cur-targetSum]
            hashmap[cur]+=1
            dfs(node.left,cur)
            dfs(node.right,cur)
            hashmap[cur]-=1
        dfs(root,0)
        return res