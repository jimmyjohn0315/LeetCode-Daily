# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = [(root,0)]
        res = 0
        while queue:
            arr = []
            for _ in range(len(queue)):
                node,pos = queue.pop(0)
                arr.append(pos)
                if node.left:
                    queue.append((node.left,pos*2))
                if node.right:
                    queue.append((node.right,pos*2+1))
            
            res = max(res,1+arr[-1]-arr[0])
        
        return res
