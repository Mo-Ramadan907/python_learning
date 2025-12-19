class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class doubleNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def insert_at_position(self, data, pos):
        if pos > self.size or pos < 0:
            return
        node = Node(data)
        if pos == 0:
            node.next = self.head
            self.head = node
        else:
            cur = self.head
            for i in range(pos - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node
        self.size += 1
    def __len__(self):
        return self.size
    
    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def delete_at_pos(self, pos):
        if pos >= self.size or pos < 0 or self.head is None:
            return
        if pos == 0:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            prev = self.head
            for i in range(pos - 1):
                prev = prev.next
            temp = prev.next
            prev.next = temp.next
            del temp
        self.size -= 1

    def __repr__(self):
        s = self.head
        while s:
            print(s.data)
            s = s.next
class doubleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0 
    def insert_at_beginning(self,data):
        node = doubleNode(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head 
            if self.head.next :
                self.head.prev = node 
            self.head = node
        self.size +=1
    def delete_at_pos(self,pos):
        if pos >self.size or pos< 0 or self.head is None:
            return None
        else:
            if pos==0:
                temp = self.head
                if self.head.next : 
                    self.head.next.prev = None
                self.head  = self.head.next
                del temp
            else:
                cur = self.head 
                for i in range(pos-1):
                    cur = cur.next
                temp = cur.next 
                if temp.next :
                    temp.next.prev = cur
                cur.next = temp.next
                del temp
    def printD(self):
        s = self.head
        while s :
            print(s.data)
            s = s.next
    def insert_at_pos(self,data,pos):
        if pos > self.size or pos < 0:
            return
        node = doubleNode(data)
        if pos == 0:
            node.next = self.head
            if self.head.next:
                self.head.prev = node 
            self.head = node
        else:
            cur = self.head
            for i in range(pos - 1):
                cur = cur.next
            node.next = cur.next
            node.prev = cur
            if cur.next:
                cur.next.prev = node
            cur.next = node
        self.size += 1
# Test
# l = LinkedList()
# l.insert_at_beginning(10)
# l.insert_at_beginning(11)
# l.insert_at_beginning(12)
# l.insert_at_position(13, 0)
# l.insert_at_position(14, 1)
# l.printL()
# l.delete_at_pos(1)
# l.delete_at_pos(2)
# print("##########")
# l.printL()

# print("####")
# s = doubleLinkedList()
# s.insert_at_beginning(10)
# s.insert_at_pos(11,0)
# s.insert_at_pos(12,1)
# s.insert_at_pos(13,3)
# s.delete_at_pos(2)
# s.printD()
print (18%10)
print(18//10)
print(9999999+9999)
