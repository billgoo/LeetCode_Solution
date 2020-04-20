# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # Recursion O_n time and space
        """
        root = TreeNode(preorder[0])
        
        i = 1
        n =  len(preorder)
        while i < n and preorder[i] < preorder[0]:
            i += 1
        
        if i - 1 > 0:
            root.left = self.bstFromPreorder(preorder[1:i])
        if i < n:
            root.right = self.bstFromPreorder(preorder[i:])
            
        return root
        """
        
        # Iteration O_n time and space
        """
        The recursion above could be converted into the iteration with the help of stack.
            Use for loop to iterate along the elements of preorder array :
                Pick the last element of the stack as a parent node, and the the current 
                    element of preorder as a child node.
                Adjust the parent node : 
                    pop out of stack all elements with the value smaller than the child value. 
                    Change the parent node at each pop node = stack.pop().
                If node.val < child.val - put the child as a right child : node.right = child.
                Else - as a left child : node.left = child.
                Push child node into the stack.
            Return root.
        """
        n = len(preorder)
        root = TreeNode(preorder[0])
        stack = [root]
        
        for i in range(1, n):
            parent, child = stack[-1], TreeNode(preorder[i])
            while stack and stack[-1].val < child.val:
                parent = stack.pop()
                
            if parent.val < child.val:
                parent.right = child
            else:
                parent.left = child
            
            stack.append(child)
            
        return root
