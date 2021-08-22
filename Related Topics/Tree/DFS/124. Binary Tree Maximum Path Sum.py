# 124. Binary Tree Maximum Path Sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path = float('-inf')
        
        def helper(node):
            # nonlocal max_path
            if not node:
                return 0
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)
            
            self.max_path = max(self.max_path, node.val + left + right)
            
            return node.val + max(left, right)
        
        # self.max_path = max(self.max_path, helper(root))
        helper(root)
        return self.max_path