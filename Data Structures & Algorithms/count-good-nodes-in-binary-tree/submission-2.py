# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal) -> int:
            if not node:
                return 0
            else:
                goodNodes = 0
                if node.val >= maxVal:
                    maxVal = node.val
                    goodNodes += 1
                
                goodNodes += dfs(node.left, maxVal)
                goodNodes += dfs(node.right, maxVal)
                return goodNodes
            pass

        return dfs(root, root.val)