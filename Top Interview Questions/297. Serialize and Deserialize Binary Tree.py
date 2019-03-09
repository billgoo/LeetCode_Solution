# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return []
        stack = [root]
        result = []
        while stack and set(stack) != {None}:
            node = stack.pop(0)
            if node != None:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            else:
                result.append('null')
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        n = len(data)
        if n == 0:
            return None
        elif n == 1:
            return TreeNode(data[0])
        
        root = TreeNode(data[0])
        queue = [root]
        position = 1
        while queue:
            node = queue.pop(0)
            
            if position > n - 1:
                break
            
            if data[position] != 'null':
                node.left = TreeNode(data[position])
                queue.append(node.left)
            position += 1
            
            if position > n - 1:
                break
                
            if data[position] != 'null':
                node.right = TreeNode(data[position])
                queue.append(node.right)
            position += 1
        return root
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))