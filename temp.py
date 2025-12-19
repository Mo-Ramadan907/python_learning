class MaxHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)
    def __repr__(self):
        l  = []
        for i in range(len(self.heap)):
            l.append(self.heap[i][1])
        return l
    def heapify(self,elements):
        self.heap = list(elements)
        for i in reversed(range(self._parent(len(self.heap)-1)+1)):
            self._sift_down(i)
    def _sift_up(self,index):
        parent = self._parent(index)
        while parent is not None and self.heap[parent][0] < self.heap[index][0]:
            self.heap[index],self.heap[parent] = self.heap[parent],self.heap[index]
            index = parent
            parent = self._parent(index)
    def extract_max(self):
        if len(self.heap)== 0 : 
            return None
        max = self.heap[0]
        last = self.heap.pop()
        if len(self.heap)>1  :
            self.heap[0] = last
            self._sift_down(0)
        return max
    def insert(self,key,value):
        self.heap.append((key,value))
        self._sift_up(len(self.heap)-1)
    def peak_max(self):
        return self.heap[0] if len(self.heap)>0 else None
    def _sift_down(self,index):
        while True :
            largest = index
            left = self._left(index)
            right = self._right(index)
            if left is not None and self.heap[left][0] >self.heap[largest][0]:
                largest = left 
            if right is not None and self.heap[right][0]> self.heap[largest][0]:
                largest =right
            if largest ==index:
                break
            self.heap[largest],self.heap[index] = self.heap[index],self.heap[largest]
            index = largest
    def _parent(self,index):
        return (index-1)//2 if index!= 0 else None
    def _left(self,index):
        left = 2*index + 1 
        return left if left <len(self.heap) else None
    def _right(self,index):
        right = 2*index + 2 
        return right if right <len(self.heap) else None


s = MaxHeap()
s.insert(1,20)
s.insert(2,30)
s.insert(3,30)
s.insert(4,50)
s.extract_max()

print(s.__repr__())