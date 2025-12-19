import time
def mydecrator(function):
    def wrapper(*argc,**kwargs):
        print("i am decorating the function ")
        return function(*argc,**kwargs)
    return wrapper
@mydecrator
def hello_world(person):
    print("this is mo ")
    return "hello world {0}".format(person)

print(hello_world("mohamed"))



def logged(function):
    def wrapper(*argc,**kwargc):
        value = function(*argc,**kwargc)
        with open("logfile.txt","a+") as f : 
            fname  = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value} \n")
    return wrapper
@logged
def add(x,y):
    return x+y 

def timed(function):
    def wrapper(*argc,**kwargc):
        before = time.time()
        value = function(*argc,**kwargc)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before}seconds ")
        return value
    return wrapper
@timed
def myfun(x):
    result = 1
    for i in range(x):
        result+=i 
    return result
