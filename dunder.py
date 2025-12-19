class Vector: 
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    def __repr__(self):
        return str((self.x,self.y))
    def __len__(self):
        return 2
    def __call__(self, *args, **kwds):
        print("hello world ")
v = Vector(1,3)
v2 = Vector(2,4)
v3 = v+v2
v3 = v-v2
print(v3)
print(len(v3))
v3()