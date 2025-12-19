import sys
def mygenerator(n):
    for x in range(n):
        yield x**3
s = mygenerator(20)


print(sys.getsizeof(mygenerator(100000000)))
print(sys.getsizeof(s))