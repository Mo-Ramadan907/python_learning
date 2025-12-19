class Node:
    def __init__(self,key):
        self.key = key
        self.data = None
        self.left = None
        self.right = None
        self.parent = None
class bst:
    def __init__(self):
        self.root = None
    def __contains__(self,key):
        cur = self.root
        while cur is not None : 
            if cur.key > key:
                cur = cur .left 
            elif cur.key < key:
                cur = cur.right
            else:
                return True 
        return False 
    def __iter__(self):
        for key, _ in self._inorder_traversal(self.root):
            yield key
    def __repr__(self):
           return f"{[pair for pair in self._inorder_traversal(self.root)]}"
    def insert(self,key,value):
        node = Node(key)
        node.data = value
        if self.root is None : 
            node.parent = None
            self.root = node
        else: 
            cur = self.root 
            while True: 
                if key < cur.key:
                    if cur.left is None : 
                        cur.left = node 
                        node.parent = cur
                        break
                    cur = cur.left
                elif key > cur.key:
                    if cur.right  is None:
                        cur.right = node 
                        node.parent = cur
                        break
                    cur = cur.right
                else:
                    cur.data = value
                    break
    def search(self,key):
        current_node = self.root
        while True:
            if current_node is None or current_node.key ==key :
                return current_node
            elif key < current_node.key:
                current_node = current_node.left 
            else:
                current_node = current_node.right
    def delete(self,key):
        node = self.search(key)
        if node is None:
            raise KeyError("invalid key in this tree")
        else: 
            self._delete(node)
    def traverse(self,order):
        if order =="inorder":
            yield from self._inorder_traversal(self.root)
        elif order =="postorder":
            yield from self._postorder_traversal(self.root )
        elif order =="preorder":
            yield from self._preorder_traversal(self.root)
        else: 
            raise ValueError("invalid order ")
    def _delete(self,node):
        if node.left is None and node.right is None: 
            if node.parent is None:
                del node
                self.root = None
            else:
                if node.parent.left ==node : 
                    node.parent.left =None
                else:
                    node.parent.right = None
                del node
        elif node.right is None or node.left is None: 
            child_node = node.left if node.right is None else node.right 
            if node.parent is None: 
                self.root = child_node
                del node
            else: 
                if node.parent.left == node : 
                    node.parent.left =child_node
                else: 
                    node.parent.right = node 
                child_node.parent = node.parent    
                del node
        else: 
            succ = self._successor(node)
            node.key = succ.key
            node.data =succ.data
            del succ
    def _successor(self,node):
        if node is None:
            raise ValueError("you can't send none node ")
        elif node.right is None : 
            return None 
        else:
            cur = node.right
            while cur.left : 
                cur = cur.left 
            return cur 
    def _predecessor(self,node):
        if node is None:
            raise ValueError("not nodes in the tree")
        elif node.left is None:
            return None
        else: 
            cur = node.left 
            while cur.right is not None:
                cur = cur.right
            return cur
    def _inorder_traversal(self,node):
        if node is not None : 
            yield from self._inorder_traversal(node.left )
            yield (node.key,node.data)
            yield from self._inorder_traversal(node.right)
    def _preorder_traversal(self,node):
        if node is not None:
            yield (node.key,node.data)
            yield from self._preorder_traversal(node.left)
            yield from self._preorder_traversal(node.right)
    def _postorder_traversal(self,node):
        if node is not None : 
            yield from self._postorder_traversal(node.left )
            yield from self._postorder_traversal(node.right)
            yield (node.key,node.data)


b = bst()
b.insert(1,"mohamed")
b.insert(10,"mahmoud")
b.insert(0,"ahmed")
b.insert(0.5,"ramadan")
b.insert(-1,"ramy")
b.insert(9,"salah")
b.insert(11,"james")
for i in b.traverse("postorder"):
    print(i)