# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        # DFS O_n time and O_n space
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        
        while stack:
            root, low, up = stack.pop()
            if not root:
                continue
            
            if root.val <= low or root.val >= up:
                return False
            
            stack.append((root.left, low, root.val))
            stack.append((root.right, root.val, up))

        return True            
        """
        
        # in-order traverse O_n time and O_n space
        stack = []
        low = float('-inf')
        
        while stack or root:
            # go down to left
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if root.val <= low:
                return False

            low = root.val
            root = root.right

        return True
