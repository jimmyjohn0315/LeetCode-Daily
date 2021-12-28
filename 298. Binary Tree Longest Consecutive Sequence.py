# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [(root, 1)]
        while stack:
            node, count = stack.pop()
            res = max(res, count)
            if node.left:
                stack.append((node.left, count + 1 if node.val + 1 == node.left.val else 1))
            if node.right:
                stack.append((node.right, count + 1 if node.val + 1 == node.right.val else 1))
        return res
