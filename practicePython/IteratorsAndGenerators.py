import random
# class myRange:
#     def __init__(self,end,start= 0 ):
#         self.start_value = start
#         self.end_value = end 
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start_value >= self.end_value:
#             raise StopIteration
#         current = self.start_value
#         self.start_value+=1
#         return current
# def my_range(start,end):
#     current = start
#     while current < end: 
#         yield current
#         current +=1 
# temp2 = my_range(1,10)
# for i in temp2:
#     print(i)
# temp  =myRange(10,1)
# for i in temp:
#     print(i)
# nums = ["mohamed",'ahmed',"ramy"]
# i_nums = iter(nums)

# while True : 
#     try:
#         it = next(i_nums)
#         print(it)
#         print("------")
#     except StopIteration:
#         break


#------ even numbers only get yielded from this generator------------
def evenGenerator(number):
    current = 0 
    while current <= number:
        if current % 2 ==0 :
            yield current
        current += 1

#==== stream of numbers yields by the generator and then you can you use the square generator and filter generator
def numbers():
    current = 0 
    while True : 
        yield current
        current +=1
def square(stream):
    for i in stream:
        yield i*i
def filter_big(stream):
    for i in stream:
        if i > 50 :
            yield i
def double(num):
    current = num
    while True:
        yield current
        current *=2
n = filter_big(square(numbers()))
for i in range(10):
    print(next(n))


# file iterator class that used as iterator to load the file line by line not at once ---
class fileIterator:

    def __init__(self,fileName):
        self.file = open(fileName,"r+") 
    def __iter__(self):
        return self
    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line
file = fileIterator("/home/mo/Projects/study_program/practicePython/temp.txt")





#----- sliding widown in ai machine learning can be used as masked -------
def sliding_window(seq, size):
    for i in range(len(seq) - size + 1):
        yield seq[i : i + size]

lst = [1,2,3,4,5,6,7,8]
ls = [i for i in sliding_window(lst,4)]
print(ls)

#------countdown generator ------------------------------
def countDown(Number):
    current = Number
    while current >= 0 : 
        yield current
        current -=1


# class batch of data iterator
class batchIterator:
    def __init__(self,data,batch_size):
        self.data = data
        self.batch_size = batch_size
        self.index = 0 
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        batch  = self.data[self.index:self.index+self.batch_size]
        self.index +=self.batch_size
        return batch

batched_data = batchIterator([10,11,12,13,14,15,16],6)
# for i in batched_data:
#     print(i)

#-----tokens generator

def tokenize(strings):
    for i in strings.split():
        yield i
p = tokenize("hello world this is my name ")


#---random vector by specify the size of the vector
def random_vector(size):
    while True:
        yield [int(random.random()*10)+1 for _ in range(size)]

s = random_vector(10)
print(next(s))

# class myBatchSize:
#     def __init__(self,data,batch_size):
#         self.data = data
#         self.batchSize = batch_size
#         self.index = 0 
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         batched_data = self.data[self.index:self.index+self.batchSize]
#         self.index +=self.batchSize
#         return batched_data
# myBatch = myBatchSize([10,11,12,13,14,15,77,88],2)
# m = list(iter(myBatch))
# print(m)
