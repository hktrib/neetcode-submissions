# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode], low=float('-inf'), high=float('inf')) -> bool:
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            
            return dfs(node.left, low, high=node.val) and dfs(node.right, low=node.val, high=high)

        return dfs(root)
                