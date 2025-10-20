# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def dfs(node,path,pathSum):
            if not node:
                return
            pathSum+=node.val      #
            path.append(node.val)  #这个判断条件老是写到if not node.left and not node.right后面
            if not node.left and not node.right and pathSum==targetSum:
                res.append(path[:])
            dfs(node.left,path,pathSum)
            dfs(node.right,path,pathSum)
            path.pop()
        
        dfs(root,[],0)
        return res