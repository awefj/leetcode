class MyHashMap:
    def __init__(self):
        self.h = {}

    def put(self, key: int, value: int) -> None:
        self.h[key] = value

    def get(self, key: int) -> int:
        try:
            return self.h[key] if self.h[key] is not None else -1
        except KeyError:
            return -1

    def remove(self, key: int) -> None:
        try:
            self.h[key] = None
        except KeyError:
            pass


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

t = MyHashMap()
print(t.put(1, 1))
print(t.put(2, 2))
print(t.get(1))
print(t.get(3))
print(t.put(2, 1))
print(t.get(2))
print(t.remove(2))
print(t.get(2))
