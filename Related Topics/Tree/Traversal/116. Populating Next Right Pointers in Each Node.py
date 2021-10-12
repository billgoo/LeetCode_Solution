#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (51.62%)
# Likes:    4482
# Dislikes: 199
# Total Accepted:    570.2K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5,6,7]'
#
# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following
# definition:
# 
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function
# should populate each next pointer to point to its next right node, just like
# in Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2^12 - 1].
# -1000 <= Node.val <= 1000
# 
# 
# 
# Follow-up:
# 
# 
# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not
# count as extra space for this problem.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

""" 前序遍历解法 """
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        # 前序遍历解法
        self.connectNeighbors(root.left, root.right)
        return root

    def connectNeighbors(self, left: 'Node', right):
        if not left or not right:
            return

        # 前序遍历 root 处理位置
        left.next = right

        # traverse left sub
        self.connectNeighbors(left.left, left.right)
        # traverse right sub
        self.connectNeighbors(right.left, right.right)
        # traverse left and right with diff predecessor
        self.connectNeighbors(left.right, right.left)
# @lc code=end

""" 层次遍历解法 """
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or (not root.left):
            return root

        q = [root.left, root.right]
        while q:
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                if i < n - 1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root

