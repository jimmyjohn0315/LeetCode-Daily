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
            return 'X'  # use 'X' represent None 
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        # inorder traversal
        return str(root.val) + ',' + left + ',' + right
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        def buildTree(data):
            val = data.pop(0)
            if val == 'X':
                return None
            root = TreeNode(val)
            root.left = buildTree(data)
            root.right = buildTree(data)
            return root
        return buildTree(data)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
