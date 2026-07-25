"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = dict()
        def clone(node: Optional['Node']) -> Optional['Node']:
            if node == None:
                return None
            elif node.neighbors == None:
                return node
            elif node in visited:
                return visited[node]
            else:
                newNode = Node(node.val, None)
                visited[node] = newNode

                for neighbor in node.neighbors:
                    newNode.neighbors.append(clone(neighbor))

                return newNode

            pass

        return clone(node)
        
