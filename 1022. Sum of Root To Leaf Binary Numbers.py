class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(root, cur):
            if not root:
                return
            
            cur = cur * 2 + root.val
            if not root.left and not root.right:
                self.res += cur
                return
            
            dfs(root.left, cur)
            dfs(root.right, cur)
            
        dfs(root, 0)
        return self.res
