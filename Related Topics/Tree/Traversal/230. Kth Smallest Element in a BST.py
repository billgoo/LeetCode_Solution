# 230. Kth Smallest Element in a BST
# 框架
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        return self.traverse(root).val

    def traverse(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 中序遍历
        if not root:
            return None

        node = self.traverse(root.left)
        if node:
            return node

        self.k -= 1
        if self.k == 0:
            return root

        node = self.traverse(root.right)
        if node:
            return node

        return None
# DFS
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         stack = []

#         while True:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             k -= 1
#             if k == 0:
#                 return root.val
#             root = root.right