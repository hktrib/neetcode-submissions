# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            res = []
            q = deque([root])

            while q:
                # snapshot current B-Tree level in queue
                level_len = len(q)
                for i in range(level_len):
                    node = q.popleft()

                    # image a level of the B-Tree as an array
                    # you want the last element which is rightmost
                    if i == level_len - 1:
                        res.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
            return res
