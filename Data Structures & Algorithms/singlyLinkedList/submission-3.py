class LinkedList:
    class Node:
        def __init__(self, val, next_node):
            self.val = val
            self.next_node = next_node
    
    def __init__(self):
        self.head = None
        self.length = 0

    
    def get(self, index: int) -> int:
        i = 0
        c = self.head
        while i < index and c:
            c = c.next_node
            i +=1
        if c is None:
            return -1
        return c.val
        

    def insertHead(self, val: int) -> None:
        self.head = self.Node(val, self.head)
        self.length += 1
        

    def insertTail(self, val: int) -> None:
        if self.head is None:
            return self.insertHead(val)
        c = self.head
        while c.next_node:
            c = c.next_node
        c.next_node = self.Node(val, None)
        self.length += 1
        

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False
        if index == 0:
            self.head = self.head.next_node
            return True
        
        i = 0
        c = self.head
        while i < index-1:
            c = self.head.next_node
            i +=1
        
        if c.next_node:
            c.next_node = c.next_node.next_node
        return True
        

    def getValues(self) -> List[int]:
        values = []
        c = self.head
        while c:
            values.append(c.val)
            c = c.next_node
        return values
        
