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
        def dfs(node,cur):
            if not node:
                return 0
            cur+=node.val
            res=hashmap[cur-targetSum]
            hashmap[cur]+=1
            res+=dfs(node.left,cur)+dfs(node.right,cur)
            hashmap[cur]-=1
            cur-=node.val
            return res
        return dfs(root,0)


