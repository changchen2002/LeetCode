# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap={num:index for index,num in enumerate(inorder)}
        preidx=0
        def construct(left,right):
            nonlocal preidx
            if left>right:
                return None
            node=TreeNode(preorder[preidx])
            idx=hashmap[preorder[preidx]]
            preidx+=1
            node.left,node.right=construct(left,idx-1),construct(idx+1,right)
            return node

        return construct(0,len(inorder)-1)