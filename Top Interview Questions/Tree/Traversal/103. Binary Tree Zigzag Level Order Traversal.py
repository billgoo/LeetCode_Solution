# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        q = collections.deque([root])
        res = []
        while q:
            r = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    r.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if len(res) % 2:
                r = r[::-1]
            if r:
                res.append(r)
        return res