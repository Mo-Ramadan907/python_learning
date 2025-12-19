import copy 
import time
import math
lst1 = [1,2,3,4,[10,12,13,[22,33,3]]]
lst2 = lst1.copy()

def add_person(func):
    def wrapper(*argc,**kwargs):
        print("added person")
        func(*argc,**kwargs)
        print("End of the function call ")
    return wrapper
@add_person
def sayHello_persons(salute ="hi",FName = "unknown"):
    print(f"{salute} : {FName}")

def add_two_nums(num1,num2):
    return num1+num2

def greeter(func):
    def wrapper(*argc,**kwargc):
        print("Hello!")
        func(*argc,**kwargc)
        print("Goodbye!")
@greeter
def say_name():
    print("My name is Mohamed")


def count_calls(func):
    count = 0 
    def wrapper(*argc,**kwargc):
        nonlocal count
        func(*argc,**kwargc)
        count+=1
        print(f"function greet was called{count} times")
    return wrapper
@count_calls
def greet():
    print("Hi!")

def timer(func):
    def wrapper(*argc,**kwagrc):
        start = time.time()
        func(*argc,**kwagrc)
        end = time.time()
        taken = end-start
        print(f"the function take {(taken / 1000):.4f} s ")
    return wrapper
@timer
def slow_function():
    for _ in range(100):
        print("*__________________________________________________-")
        for i in range(10):
            print("*****")

if __name__ == "__main__":
    slow_function()