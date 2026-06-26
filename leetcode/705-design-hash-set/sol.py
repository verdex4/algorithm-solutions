class MyHashSet:

    def __init__(self):
        # Constraints: 0 <= key <= 10^6
        # Using Direct Address Table for trade space O(10^6) to time O(1)
        self.data = [False] * (10**6 + 1)

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]
    
myHashSet = MyHashSet()
myHashSet.add(1)      # set = [1]
myHashSet.add(2)      # set = [1, 2]
myHashSet.contains(1) # return True
myHashSet.contains(3) # return False, (not found)
myHashSet.add(2)      # set = [1, 2]
myHashSet.contains(2) # return True
myHashSet.remove(2)   # set = [1]
myHashSet.contains(2) # return False, (already removed)