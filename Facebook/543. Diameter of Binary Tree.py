# 543. Diameter of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.re = 1

        def depth(node):
            if not node:
                return 0

            l = depth(node.left)
            r = depth(node.right)
            self.re = max(self.re, l + r + 1)

            return max(l, r) + 1

        depth(root)

        return self.re - 1