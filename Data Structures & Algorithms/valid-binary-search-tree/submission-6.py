# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lastValue = float('-inf')
        
        def dfs(node) -> bool:
            nonlocal lastValue
            if not node:
                return True
            
            # 1. Check the entire left subtree first
            if not dfs(node.left):
                return False

            # 2. Current node must be strictly greater than the last visited node
            if node.val <= lastValue:
                return False
            lastValue = node.val  # Update lastValue as we move forward

            # 3. Check the entire right subtree
            return dfs(node.right)
        
        return dfs(root)