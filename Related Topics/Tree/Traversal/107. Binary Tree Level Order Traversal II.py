# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        queue = [root]
        level = 0
        while queue:
            ans.append([])
            n = len(queue)
            
            for _ in range(n):
                node = queue.pop(0)
                ans[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            level += 1
            
        return ans[::-1]