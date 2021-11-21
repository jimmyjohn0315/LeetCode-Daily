# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        split = inorder.index(root.val)
        leftInorder = inorder[:split]
        rightInorder = inorder[split + 1:]
        leftPostorder = postorder[:len(leftInorder)]
        rightPostorder = postorder[len(leftInorder):len(leftInorder) + len(rightInorder)]
        root.left = self.buildTree(leftInorder, leftPostorder)
        root.right = self.buildTree(rightInorder, rightPostorder)
        
        return root
