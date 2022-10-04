class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [None] * k
        self.max = k
        self.front, self.last = 0, 0

    def insertFront(self, value: int) -> bool:
        # empty
        if self.q[self.front] is None:
            self.q[self.front] = value
            return True
        else:
            f = (self.front + 1) % self.max
            # not full
            if self.q[f] is None:
                self.front = f
                self.q[f] = value
                return True
            # full
            else:
                return False

    def insertLast(self, value: int) -> bool:
        # empty
        if self.q[self.last] is None:
            self.q[self.last] = value
            return True
        else:
            l = (self.last + self.max - 1) % self.max
            if self.q[l] is None:
                self.last = l
                self.q[l] = value
                return True
            else:
                return False

    def deleteFront(self) -> bool:
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None
            if self.front != self.last:
                self.front = (self.front + self.max - 1) % self.max
            return True

    def deleteLast(self) -> bool:
        if self.q[self.last] is None:
            return False
        else:
            self.q[self.last] = None
            if self.front != self.last:
                self.last = (self.last + 1) % self.max
            return True

    def getFront(self) -> int:
        return -1 if self.q[self.front] is None else self.q[self.front]

    def getRear(self) -> int:
        return -1 if self.q[self.last] is None else self.q[self.last]

    def isEmpty(self) -> bool:
        return self.front == self.last and self.q[self.front] is None

    def isFull(self) -> bool:
        return (self.front + 1) % self.max == self.last

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
