class MyHashSet:

    def __init__(self):
        self.hashset = []
        

    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset.append(key)

    def remove(self, key: int) -> None:
        removeKey = -1
        for i, val in enumerate(self.hashset):
            if val == key:
                removeKey = i
        if removeKey != -1:
            self.hashset.pop(removeKey)

    def contains(self, key: int) -> bool:
        for val in self.hashset:
            if val == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)