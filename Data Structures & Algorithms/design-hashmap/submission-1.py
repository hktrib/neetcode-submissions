class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.hash_map = [ListNode() for _ in range(1000)]

    def hash(self, key: int) -> int:
        return key % len(self.hash_map)

    def put(self, key: int, value: int) -> None:
        cur = self.hash_map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            else:
                cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.hash_map[self.hash(key)]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.hash_map[self.hash(key)]
        # if cur and cur.key == key:
        #     self.hash_map[self.hash(key)] = cur.next
        #     return

        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)