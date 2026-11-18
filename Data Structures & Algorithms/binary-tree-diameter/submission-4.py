# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            left = self.height(root.left)
            right = self.height(root.right)

            diameter = left + right
            subTreeMax = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

            return max(diameter, subTreeMax)
        
    def height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        else:
            return max(self.height(node.left) + 1, self.height(node.right) + 1)


            
        