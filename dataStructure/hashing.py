class HashMap:
    def __init__(self,capacity):
        self.cap = capacity
        self.size = 0 
        self.buckets = [[] for _ in range(capacity)]
    def __len__(self):ا
        pass
    def __contains__(self,key):
        index  = self._hash_function(key)
        bucket = self.buckets[index]
        for k,v in bucket:
            if k ==key:
                return True 
        return False
    def put(self,key,value):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                break
        else:
            bucket.append((key,value))
        self.size +=1
    def get(self,key):
        index  = self._hash_function(key)
        bucket = self.buckets[index]
        for k,v in bucket:
            if k == key:
                return v
        raise KeyError("key not found ")
    def remove(self,key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        
        for i ,(k,v) in enumerate(bucket):
            if k ==key:
                del bucket[i]
                self.size -=1
                break
        else : 
            raise KeyError("invalid key ")
    def keys(self):
        return [k for i in self.buckets for k,_ in i]
    def values(self):
        return [v for bucket in self.buckets for _,v in bucket]
    def items (self):
        return [(k,v) for bucket in self.buckets for k,v in bucket]
    def _hash_function(self,key):
        key_string = str(key)
        hash_result = 0 
        for c in key_string:
            hash_result = (hash_result *31+ ord(c))%self.cap
        return hash_result

if __name__ == "__main__":
    import uuid
    import matplotlib.pyplot as plt 
    h = HashMap(3000)
    for i in range(400000):
        h.put(uuid.uuid4(),"mariam")
    x = []
    y = []
    for i ,bucket in enumerate(h.buckets):
        x.append(i)
        y.append(len(bucket))
    print(x)
    plt.bar(x,y)
    plt.show()
