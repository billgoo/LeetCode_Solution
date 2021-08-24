# 111. Minimum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # init base queue
        depth = 1
        q = [root]

        while q:
            n = len(q)
            # iter for each level
            for i in range(n):
                node = q.pop(0)
                # terminal
                if not node.left and not node.right:
                    return depth
                # expand for neighbor
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # next level
            depth += 1

        return depth