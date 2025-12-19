class Graph:
    def __init__(self,directed=False):
        self.adjecent_list = dict()
        self.directed = directed
    def add_node(self,node):
        if node not in self.adjecent_list:
            self.adjecent_list[node] = set()
    def add_edge(self,from_node,to_node,weight = None):
        if from_node not in self.adjecent_list: 
            self.add_node(from_node)
        if to_node not in self.adjecent_list:
            self.add_node(to_node)
        self.adjecent_list[from_node].add((to_node,weight))
        if not  self.directed:
            self.adjecent_list[to_node].add((from_node,weight))
    def __repr__(self):
        total_graph = ""
        for u,v in self.adjecent_list.items():
            total_graph+=f"{u} --->("
            for i in v:
                total_graph +=f"{i[0]},"
            total_graph+=f")\n"
        return total_graph
    def remove_node(self,node):
        if node not in self.adjecent_list:
            raise ValueError("node doesn't exist ")
        else: 
            for neighbor in self.adjecent_list.values():
                neighbor.discard(node)
            del self.adjecent_list[node]       
    def remove_edge(self,from_node,to_node):
        if from_node not in self.adjecent_list or to_node not in self.adjecent_list:
            return
        else: 
            for u in self.adjecent_list[from_node]:
                if u[0]==to_node:
                    self.adjecent_list[from_node].remove(u)
            if not self.directed: 
                for u in self.adjecent_list[to_node]:
                    if u[0] == from_node:
                        self.adjecent_list[to_node].remove(u)
    def has_node(self,node):
        if node in self.adjecent_list:
            return True
        return False
    def get_neighbors(self,node):
        if node not in self.adjecent_list:
            return []
        return list(self.adjecent_list[node])
    def has_edge(self,from_node,to_node):
        if from_node not in self.adjecent_list or to_node not in self.adjecent_list:
            return False
        for u in self.adjecent_list[from_node]:
            if u[0] == to_node:
                return True
        return False
    def get_nodes(self):
        l = []
        for i in self.adjecent_list:
            l.append(i)
        return l
    def get_edges(self):
        l = []
        for node in self.adjecent_list:
            for u in node:
                l.append((node,u[0],u[1]))
        return l
    def bfs(self,start):
        visited = set()
        order = []
        q = [start]
        while q:
            p = q.pop(0)
            if p not in visited:
                visited.add(p)
                order.append(p)
                neighbor = self.get_neighbors(p)
                for n in neighbor:
                    if n[0] not in visited:
                        q.append(n[0])
        return order
    def dfs(self,start):
        stack = [start]
        visited = set()
        order = []
        while stack:
            p = stack.pop()
            if p not in visited:
                visited.add(p)
                order.append(p)
                neighbors = self.get_neighbors(p)
                for n in neighbors:
                    if n[0] not in visited:
                        stack.append(n[0])
        return order
    def as_matrix(self):
        pass
g = Graph()
g.add_edge(5,10,-1)
g.add_edge(1,3,0)
g.add_edge(2,4,4)
g.add_edge(1,5,100)
g.add_edge(2,3,80)
print(g.bfs(4))