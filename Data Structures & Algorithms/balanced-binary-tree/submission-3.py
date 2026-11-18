# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            else:
                left = 1 + dfs(node.left)
                right = 1 + dfs(node.right)

                return max(left, right)


        return abs(dfs(root.left) - dfs(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)