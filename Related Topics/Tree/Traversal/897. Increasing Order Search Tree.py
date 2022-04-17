# 897. Increasing Order Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        left = self.increasingBST(root.left)
        root.left = None
        root.right = self.increasingBST(root.right)

        if not left:
            return root
        else:
            p = left
            while p.right:
                p = p.right
            p.right = root
            return left
