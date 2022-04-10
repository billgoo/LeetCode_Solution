# 337. House Robber III
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # dp with memo: time and space O_n
    # def rob(self, root: Optional[TreeNode]) -> int:
    #     self.memo = dict()
    #     return self.helper(root)

    # def helper(self, root):
    #     if not root:
    #         return 0
    #     if root in self.memo:
    #         return self.memo[root]

    #     is_rob = root.val
    #     if root.left:
    #         is_rob += self.helper(root.left.left) + self.helper(root.left.right)
    #     if root.right:
    #         is_rob += self.helper(root.right.left) + self.helper(root.right.right)

    #     not_rob = self.helper(root.left) + self.helper(root.right)

    #     self.memo[root] = max(is_rob, not_rob)
    #     return self.memo[root]

    # dp with no memo: simplify time O_n and space just recursive stack O_1
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.rob_house(root))

    def rob_house(self, root: Optional[TreeNode]) -> List[int]:
        """
        返回一个大小为 2 的数组 arr
        arr[0] 表示不抢 root 的话，得到的最大钱数
        arr[1] 表示抢 root 的话，得到的最大钱数
        """
        if not root:
            return [0, 0]
        rob_left = self.rob_house(root.left)
        rob_right = self.rob_house(root.right)

        # 抢 root
        rob_root = root.val + rob_left[0] + rob_right[0]
        # 不抢 root，子节点可抢可不抢
        not_rob_root = max(rob_left) + max(rob_right)

        return [not_rob_root, rob_root]
