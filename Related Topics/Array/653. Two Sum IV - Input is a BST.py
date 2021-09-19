# 653. Two Sum IV - Input is a BST
#
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/106061/Java-Simple-AC-with-Time-O(n)-Space-O(log-n)-in-Average
# (3) Use the stack and search just like 2sum without dumping all the value out in the beginning.
# -- Time/Space: n/logn in average
# If I have to choose one from them, I would prefer the third one because it takes advantage of the property of BST and is with lower space complexity in average. Its code is shown below.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # time n space logn
        if not root:
            return False

        stack_left, stack_right = [root], [root]

        l, r = root, root
        # push left
        while l.left:
            stack_left.append(l.left)
            l = l.left
        # push right
        while r.right:
            stack_right.append(r.right)
            r = r.right

        while stack_left and stack_right and stack_left[-1].val != stack_right[-1].val:
            sum_ = stack_left[-1].val + stack_right[-1].val
            if sum_ == k:
                return True
            elif sum_ > k:
                # sum > tar, pop the top value and push the left children of it
                node = stack_right.pop()
                if node.left:
                    # push left root
                    stack_right.append(node.left)
                    node = node.left
                    # push right child tree of left root at the top of right stack
                    # -> top > bottom of stack
                    while node.right:
                        stack_right.append(node.right)
                        node = node.right
            elif sum_ < k:
                # sum < tar, pop the top value and push the right children of it
                node = stack_left.pop()
                if node.right:
                    # push right root
                    stack_left.append(node.right)
                    node = node.right
                    # push left child tree of right root at the top of left stack
                    # -> top < bottom of stack
                    while node.left:
                        stack_left.append(node.left)
                        node = node.left

        return False