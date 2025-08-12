# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def toTree(l,r):
            if l>r:
                return None
            m=l+(r-l)//2
            node=TreeNode(nums[m])
            node.left,node.right=toTree(l,m-1),toTree(m+1,r)
            return node

        return toTree(0,len(nums)-1)