# 543. Diameter of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.maxDepth(root)
        return self.res

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        self.res = max(self.res, left_max + right_max)
        return 1 + max(left_max, right_max)
