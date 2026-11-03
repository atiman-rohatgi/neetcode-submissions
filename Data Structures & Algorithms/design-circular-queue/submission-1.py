class MyCircularQueue:
    """
    - can implement this by usking a list of len k
    - using the mod rule to circle around add and delete
    - have a front and rear pointer to return those values
    - edge - if empty then reuturn -1 either case
    - complexity
        - time = O(1)
        - space = O(n)
    """

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.head = 0
        self.tail = 0
        self.count = 0
        self.length = k

    def enQueue(self, value: int) -> bool:
        #if space then only we add and move the tail pointer
        if not self.isFull():
            self.queue[self.tail] = value
            self.tail = (self.tail+1) % self.length
            self.count += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        #if not empty then only then only we move the head pointer
        if not self.isEmpty():
            self.head = (self.head+1)%self.length
            self.count -= 1
            return True
        else:
            return False
        
    def Front(self) -> int:
        if self.count == 0:
            return -1
        else:
            return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty() == True:
            return -1
        else:
            #as tail points ot the next open spot, we do tail-1
            return self.queue[(self.tail-1) % self.length]
        
    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False
        
    def isFull(self) -> bool:
        if self.count == self.length:
            return True
        else:
            return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()