from collections import defaultdict
from collections import deque


class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None
    
    def __str__(self) -> str:
        return f"{self.key} | {self.val}"
        pass

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._size = 0
        self.cache = dict()
        
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv
        pass

    def _insert(self, node):
        prv, next = self.right.prev, self.right
        prv.next = next.prev = node
        node.next = self.right
        node.prev = prv

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # print(f"Dict: {self.cache}")
        # print(f"Key-Val Pair: {key} | {value}")
        # print(f"Size: {self._size}")
        # print(f"Capacity: {self._capacity}")
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            node.val = value
            self._insert(node)
        else:
            if self._size == self._capacity:
                del self.cache[self.left.next.key]
                self._remove(self.left.next)
                self._size -= 1
            self.cache[key] = Node(key=key, val=value)
            self._insert(self.cache[key])
            self._size += 1
        
