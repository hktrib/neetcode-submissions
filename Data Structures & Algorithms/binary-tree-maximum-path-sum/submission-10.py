# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            else:
                # Postorder: get max single-branch gain from children
                # ignoring all negative values since they can't help
                left_gain = max(dfs(node.left), 0)
                right_gain = max(dfs(node.right), 0)

                current_arch = node.val + left_gain + right_gain
                maxSum = max(maxSum, current_arch)

                return node.val + max(left_gain, right_gain)
            
        dfs(root)
        return maxSum
