# 124. Binary Tree Maximum Path Sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# With global variable as result
# 1
# class Solution:
#     def maxPathSum(self, root: TreeNode) -> int:
#         self.max_path = float('-inf')

#         def helper(node):
#             # nonlocal max_path
#             if not node:
#                 return 0
#             left = max(helper(node.left), 0)
#             right = max(helper(node.right), 0)

#             self.max_path = max(self.max_path, node.val + left + right)

#             return node.val + max(left, right)

#         # self.max_path = max(self.max_path, helper(root))
#         helper(root)
#         return self.max_path
# 2
# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         self.res = float("-inf")
#         one_side_res = self.traverse(root)
#         return max(self.res, one_side_res)

#     def traverse(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         left, right = max(0, self.traverse(root.left)), max(0, self.traverse(root.right))
#         self.res = max(left + right + root.val, self.res)

#         return max(left, right) + root.val

# In place change the tree without global variable
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # self.res = float("-inf")
        one_side_res = self.traverse(root)
        # return max(self.res, one_side_res)
        return max(root.val, one_side_res)

    def traverse(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left, right = max(0, self.traverse(root.left)), max(0, self.traverse(root.right))
        # self.res = max(left + right + root.val, self.res)
        temp = root.val
        l = root.left.val if root.left else float("-inf")
        r = root.right.val if root.right else float("-inf")
        root.val = max(left + right + root.val, l, r)

        return max(left, right) + temp