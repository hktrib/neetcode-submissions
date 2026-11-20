# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lastSeen = float('-inf')

        def dfs(node):
            nonlocal lastSeen
            
            if not node:
                return True

            if not dfs(node.left):
                return False

            if lastSeen >= node.val:
                return False
            lastSeen = node.val

            # if not dfs(node.right):
            #     return False
            
            # return True
            return dfs(node.right)
        
        return dfs(root)
