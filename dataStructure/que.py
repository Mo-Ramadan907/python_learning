from dataStructure.linkedlist import Node
class Queue:
    def __init__(self):
        self.list = []
    def enqueue(self,data):
        self.list.append(data)
    def isEmpty(self):
        return len(self.list) ==0
    def dequeue(self):
        if not self.isEmpty():
            s = self.list[0]
            self.list.remove(self.list[0])
            return s
        return None
    def get_size(self):
        return len(self.list)
    def get_first_ele(self):
        if not self.isEmpty():
            return self.list[0]
        return None
    def printQ(self):
        for i in self.list:
            print(i)
class LinkedQueue(Queue):
    def __init__(self):
        self.head = None
        self.size = 0 
    def get_size(self):
        return self.size
    def get_first_ele(self):
        return None if self.isEmpty() else self.head.data
    def enqueue(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
            return 
        cur = self.head 
        while cur.next:
            cur = cur.next
        cur.next = node
        self.size +=1
    def isEmpty(self):
        return self.head is None
    def printQ(self):
        s = self.head
        while s:
            print(s.data)
            s= s.next
    def dequeue(self):
        if not self.isEmpty():
            s = self.head.data
            temp = self.head
            self.head = self.head.next 
            del temp
            self.size -=1
            return s 
        return None
    
q = Queue()
q.enqueue(10)
q.enqueue(12)
q.enqueue(13)
while not q.isEmpty():
    print(q.dequeue())
print("########")
q2 = LinkedQueue()
q2.enqueue(10)
q2.enqueue(12)
q2.enqueue(13)
while not q2.isEmpty():
    print(q2.dequeue())