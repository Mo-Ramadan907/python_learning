import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
    def __len__(self):
        return len(self.heap)
    def __repr__(self):
        s  = []
        for i in range(len(self.heap)):
            s.append(self.heap[i][1])
        return str(s)
    def insert(self,key,value):
        self.heap.append((key,value))
        self._sift_up(len(self.heap)-1)
    def peak_min(self):
        return self.heap[0] if len(self.heap) > 0 else None
    def extract_min(self):
        if len(self.heap)>0:
            min = self.heap[0]
            last = self.heap.pop()
            if len(self.heap)>0:
                self.heap[0] = last
                self._sift_down(0)
            return min
        raise IndexError("invalid removed")
    def heapify(self,elements):
        self.heap = list(elements)
        for i in reversed(range(self._parent(len(self.heap)-1)+1)):
            self._sift_down(i)
    def meld(self,other_heap):
        compound = self.heap + other_heap.heap
        self.heapify(compound)
        return compound
    def _parent(self,index):
        return (index-1)//2 if index!=0 else None
    def _left(self,index):
        left = 2*index+1
        return left if left <len(self.heap) else None
    def _right(self,index):
        right  = 2*index +2
        return right if right <len(self.heap) else None
    def _sift_up(self,index):
        parent = self._parent(index)
        while parent is not None and self.heap[parent][0] > self.heap[index][0]:
            self.heap[parent],self.heap[index] = self.heap[index],self.heap[parent]
            index = parent
            parent = self._parent(index)
    def _sift_down(self,index):
        while True:
            smallest= index
            left = self._left(index)
            right = self._right(index)
            if left is not None and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right is not None and self.heap[right][0] <self.heap[smallest][0]:
                smallest = right
            if smallest ==index:
                break
            self.heap[index],self.heap[smallest] = self.heap[smallest],self.heap[index]
            index= smallest
class MaxHeap:
    def __init__(self):
        self.heap = []
    def insert(self, key, value):
        self.heap.append((key,value))
        self._sift_up(len(self.heap)-1)
    def __len__(self):
        return len(self.heap)
    def extract_max(self):
        if not self.heap is None:
            raise IndexError("empty position")
        max = self.heap[0]
        last = self.heap.pop()
        if len(self.heap) > 0 :
            self.heap[0] = last
            self._sift_down(0)
        return max
    def peak_max(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def __repr__(self):
        s  = []
        for i in range(len(self.heap)):
            s.append(self.heap[i][1])
        return str(s)
    def _sift_up(self,index):
        parent = self._parent(index)
        while parent is not None and self.heap[parent][0] <self.heap[index][0]:
            self.heap[parent],self.heap[index] = self.heap[index],self.heap[parent]
            index = parent
            parent = self._parent(index)
    def _sift_down(self,index):
        while True:
            largest = index
            left = self._left(index)
            right = self._right(index)
            if left is not None and self.heap[left][0] > self.heap[largest][0]:
                largest = left 
            if right is not None and self.heap[right][0] > self.heap[largest][0]:
                largest = right
            if largest ==  index : 
                break
            self.heap[largest],self.heap[index] = self.heap[index],self.heap[largest]
            index = largest
    def _left(self,index):
        left = 2*index +1
        return left if left <len(self.heap) else None
    
    def _right(self,index):
        right = 2*index + 2
        return right if right <len(self.heap) else None 
    def _parent(self,index):
        return (index-1)//2 if index!=0 else None
    def heapify(self,elements):
        elements = list(elements)
        for i in reversed(range(self._parent(len(self.heap)-1)+1)):
            self._sift_down(i)
# a = [10,12,7,8,9.10,123,4]
# def heapsort(arr):
#     heapq.heapify(arr)
#     n = len(arr)
#     new_arr = [0]*n
#     for i in range(n):
#         new_arr[i] = heapq.heappop(arr)
#     return new_arr
# print(heapsort(a))
class minheap2: 
    def __init__(self):
        self.heap = []
    def insert(self,key,data):
        self.heap.append((key,data))
        self._sift_up(len(self.heap)-1)
    def _sift_down(self,index):
        while True : 
            smallest = index 
            left  = self._left(index)
            right = self._right(index)
            if left is not None and self.heap[left][0] < self.heap[index][0]:
                smallest = left 
            if right is not None and self.heap[right][0] < self.heap[index][0]:
                smallest = right 
            if smallest == index:
                break
            self.heap[index],self.heap[smallest] = self.heap[smallest],self.heap[index]
            index = smallest
    def _sift_up(self,index):
        parent = self._parent(index)
        while parent is not None and self.heap[parent][0] > self.heap[index][0]:
            self.heap[parent] , self.heap[index] = self.heap[index] , self.heap[parent]
            index = parent 
            parent = self._parent(index)
    
    def _parent(self,index):
        if index < 0:
            raise ValueError("this unvalid index")
        else:
            return (index-1)//2 if index!=0 else None
    def _left(self,index):
        if index< 0 : 
            raise ValueError("this invalid index")
        else : 
            left = 2*index + 1 
            return left if left < len(self.heap) else None
    def _right(self,index):
        if index < 0 : 
            raise ValueError("invalid index ")
        else : 
            right = 2 * index + 2 
            return right if right < len(self.heap) else None 
    def heapify(self,elements ): 
        self.heap = list(elements)
        for i in reversed(range(self._parent(len(self.heap)-1)+1)):
            self._sift_down(i)
    def peak(self):
        return self.heap[0] if len(self.heap) > 0 else None 
    def extract_min(self):
        if len(self.heap) > 0 : 
            min = self.heap[0]
            last = self.heap.pop()
            if  len(self.heap) > 0 : 
                self.heap[0] = last 
                self._sift_down(0)
            return min
        return None 
    def __repr__(self):
        return str(self.heap)
if __name__ == "__main__":
    s = minheap2()
    s.insert(1,"mohamed")
    s.insert(2,"ahmed")
    s.insert (10 ,"gehad ")
    s.insert (-10,"romio")
    s.extract_min()
    print(s)