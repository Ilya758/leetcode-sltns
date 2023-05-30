class MyHashSet:

    def __init__(self):
        self.hashset = dict()

    def add(self, key: int) -> None:
        self.hashset[key] = key

    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.pop(key)

    def contains(self, key: int) -> bool:
        if key in self.hashset:
            return True


# Hashset object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.remove(1)
param_3 = obj.contains(1)
