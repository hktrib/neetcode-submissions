"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        nodeToNewNodes = {}

        curr = head
        while curr:
            nodeToNewNodes[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                nodeToNewNodes[curr].next = nodeToNewNodes[curr.next]
            else:
                nodeToNewNodes[curr].next = None
            if curr.random:
                nodeToNewNodes[curr].random = nodeToNewNodes[curr.random]
            else:
                nodeToNewNodes[curr].random = None
            curr = curr.next

        return nodeToNewNodes[head]