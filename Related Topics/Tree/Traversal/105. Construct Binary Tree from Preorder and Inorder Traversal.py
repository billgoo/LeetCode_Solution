# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = TreeNode(val=preorder[0])

        in_root = inorder.index(preorder[0])
        left_inorder, right_inorder = inorder[:in_root], inorder[in_root + 1:]

        in_left = len(left_inorder)
        left_preorder, right_preorder = preorder[1:1 +
                                                 in_left], preorder[1 + in_left:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
# [麻烦]labuladong 框架解法
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         tree_len = len(preorder)
#         if tree_len == 0:
#             return None
#         elif tree_len == 1:
#             return TreeNode(preorder[0])

#         inorder_index_map = {val: index for (index, val) in enumerate(inorder)}
#         return self.build(preorder, inorder, inorder_index_map,
#                           0, tree_len - 1, 0, tree_len - 1)

#     def build(self, preorder: List[int], inorder: List[int], inorder_index_map: Dict[int, int],
#               preleft: int, preright: int, inleft: int, inright: int) -> Optional[TreeNode]:
#         if preleft > preright:
#             return None

#         # get root
#         root_val = preorder[preleft]
#         root_inorder_index = inorder_index_map[root_val]
#         root = TreeNode(root_val)

#         # pre-order traverse to build left and right
#         root.left = self.build(preorder, inorder, inorder_index_map,
#                                preleft + 1, preleft + root_inorder_index - inleft,
#                                inleft, root_inorder_index - 1)
#         root.right = self.build(preorder, inorder, inorder_index_map,
#                                 preleft + root_inorder_index - inleft + 1, preright,
#                                 root_inorder_index + 1, inright)

#         return root
