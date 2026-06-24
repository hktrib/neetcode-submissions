# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
            We search the position of root (from preorder[0]) in
            the inorder array recursively. To save compute time O(n^2)
            otherwise, we can make a hashmap for O(1) * n lookup of the root
        '''
        indices = {val: idx for idx, val in enumerate(inorder)}


        def dfs (pre, inor, in_start) -> Optional[TreeNode]:
            if not pre or not inor:
                return None

            root = TreeNode(pre[0])
            adjustedMid = indices[pre[0]] - in_start

            root.left = dfs(pre[1: adjustedMid + 1], inor[: adjustedMid], in_start)
            root.right = dfs(pre[adjustedMid + 1 : ], inor[adjustedMid + 1:], indices[pre[0]] + 1)
            return root
        
        return dfs(preorder, inorder, 0)
