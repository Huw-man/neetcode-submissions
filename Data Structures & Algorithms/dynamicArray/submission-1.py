class DynamicArray:
    
    def __init__(self, capacity: int):
        self.ary = [None]*capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.ary[i]

    def set(self, i: int, n: int) -> None:
        self.ary[i] = n
        
    def pushback(self, n: int) -> None:
        if self.length == len(self.ary):
            self.resize()
        self.set(self.length, n)
        self.length += 1

    def popback(self) -> int:
        val = self.get(self.length - 1)
        self.length -= 1
        return val
 

    def resize(self) -> None:
        new_ary = [None] * (len(self.ary) * 2)
        for i, n in enumerate(self.ary):
            new_ary[i] = n
        self.ary = new_ary


    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return len(self.ary)
