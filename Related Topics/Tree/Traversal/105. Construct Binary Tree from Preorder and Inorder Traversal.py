# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        
        root = TreeNode(val=preorder[0])
        
        in_root = inorder.index(preorder[0])
        left_inorder, right_inorder = inorder[:in_root], inorder[in_root + 1:]
        
        in_left = len(left_inorder)
        left_preorder, right_preorder = preorder[1:1 + in_left], preorder[1 + in_left:]
        
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root