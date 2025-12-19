from dataStructure.linkedlist import Node
class stack:
    def __init__(self):
        self.list = []
    def push(self,data):
        self.list.append(data)
    def pop(self):
        if not self.isEmpty():
            return self.list.pop()
        return None
    def isEmpty(self):
        return len(self.list)==0
    def peak(self):
        if not self.isEmpty():
            return self.list[-1]
    def getSize(self):
        return len(self.list)
class linkedStack:
    def __init__(self):
        self.head = None 
    def push(self,data):
        node =Node(data) 
        if self.head is not None : 
            self.head = node 
            return
        node.next = self.head
        self.head = node
    def pop(self):
        if self.head is None : 
            return None
        data = self.head.data
        temp = self.head 
        self.head = temp.next
        del temp
        return data
    def peak(self):
        if self.head is None : 
            return None 
        return self.head.data
    