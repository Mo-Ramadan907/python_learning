class treenode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class binarySearchTree:
    def __init__(self):
        self.root  = None
    def addNode(self,data):
        node = treenode(data)
        if self.root is None:
            self.root = node
            return 
        temp = self.root
        prev = None 
        while  temp:
            prev = temp
            if node.data <temp.data:
                temp = temp.left 
            else :
                temp = temp.right
        if  prev.data > node.data:
            prev.left = node
        else :
            prev.right = node
def printNode(node):
    if not node:
        return
    print(node.data)
    printNode(node.left)
    printNode(node.right)
a =treenode(5)
b= treenode(6)
c = treenode(7)
a.left = b
a.right = c
printNode(a)