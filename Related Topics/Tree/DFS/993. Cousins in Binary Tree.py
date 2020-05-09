# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        
        stack = [[root, 0, -1]]
        cousins = []
        
        # use for prune
        depth = -1
        
        while stack:
            [node, h, parent] = stack.pop()
            
            if node.val == x or node.val == y:
                # early stop
                if len(cousins):
                    if h != cousins[0][0] or parent == cousins[0][1]:
                        return False
                    else:
                        return True
                    
                depth = h
                cousins.append([h, parent])
                continue
            
            # prune
            if h == depth:
                continue
            
            if node.right:
                stack.append([node.right, h + 1, node.val])
            if node.left:
                stack.append([node.left, h + 1, node.val])
            
        return False