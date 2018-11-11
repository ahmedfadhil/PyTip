# Implementing maxheap algorithm
# public functions: push, peek and pop
# private functions: __swap, __floatUp, __bubbleDown
class MaxHeap:
    def __init__(self, items=[]):
        super.__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1)

    # Public functions
    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
            return max

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    # Non-public functions
    def __swap(self,i,j):
        pass

    def __floatUp(self,index):
        pass

    def __bubbleDown(self,):
        pass
