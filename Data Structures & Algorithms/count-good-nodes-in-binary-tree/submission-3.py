# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        q = deque([[root, root.val]])

        while q:
            pair = q.popleft()

            if pair[0] and pair[0].val >= pair[1]:
                pair[1] = pair[0].val
                res += 1
            if pair[0].left:
                q.append([pair[0].left, pair[1]])
            if pair[0].right:
                q.append([pair[0].right, pair[1]])
            
        return res
            
        