# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS level order
        if not root:
            return []
        
        result = []
        
        level = 0
        queue = [root]
        
        while queue:
            result.append([])
            n = len(queue)
            
            for i in range(n):
                node = queue.pop(0)
                
                result[level].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            level += 1
            
        return result
        