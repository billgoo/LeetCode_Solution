# 337. House Robber III
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.memo = dict()
        return self.helper(root)

    def helper(self, root):
        if not root:
            return 0
        if root in self.memo:
            return self.memo[root]

        is_rob = root.val
        if root.left:
            is_rob += self.helper(root.left.left) + self.helper(root.left.right)
        if root.right:
            is_rob += self.helper(root.right.left) + self.helper(root.right.right)

        not_rob = self.helper(root.left) + self.helper(root.right)

        self.memo[root] = max(is_rob, not_rob)
        return self.memo[root]