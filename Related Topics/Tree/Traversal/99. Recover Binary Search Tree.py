# 99. Recover Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.max_node, self.min_node = None, None
        # prev and curr are the node in order of inorder traversal
        # so, prev < curr
        self.prev, self.curr = None, None
        
        self.inorder_traverse(root)
        self.swap(self.max_node, self.min_node)
        
        
    def swap(self, first: Optional[TreeNode], second: Optional[TreeNode]) -> None:
        first.val, second.val = second.val, first.val
        

    def inorder_traverse(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        # left
        self.inorder_traverse(root.left)
        
        # inorder for root
        self.prev, self.curr = self.curr, root
        # if we find one of the reverse order pair
        if self.prev and self.curr and self.prev.val > self.curr.val:
            # check if we have find the max node for root
            # if find max value, just update the min value else both value
            if not self.max_node:
                # no max value
                self.max_node = self.prev
            self.min_node = self.curr
        
        # right
        self.inorder_traverse(root.right)