import threading
import time
# semphore = threading.Semaphore(value = 8 )
# def access(thread_number):
    
#     print(f"{thread_number} is trying to access")
#     semphore.acquire()
#     print(f"{thread_number} was granted access ")
#     time.sleep(5)
#     print(f"{thread_number} is now realsing")
#     semphore.release()
# for thread_num in range(11):
#     t = threading.Thread(target=access,args=(thread_num,))
#     t.start()
#     time.sleep(5)
# def one():
#     for x in range(1000):
#         print("one")
# def two():
#     for x in range(1000):
#         print("two")

# x = 8192 
# lock = threading.Lock()
# def double():
#     global x,lock
#     lock.acquire()
#     while x < 16384:
#         x*=2 
#         print(x)
#         time.sleep(1)
#     print("reached the maximum number ")
#     lock.release()
# def half():
#     global x ,lock
#     lock.acquire()
#     while x > 1 : 
#         x /=2
#         print(x)
#         time.sleep(1)
#     print("reached the minimum value ")
#     lock.release()
# t1 = threading.Thread(target=double)
# t2 = threading.Thread(target=half)
# t1.start()
# t2.start()

semphore = threading.Semaphore(value=1)

# fact = 1
# number = 5 
# def factorial():
#     global fact,semphore,number
#     i = number
#     semphore.acquire()
#     while i >=1 :
#         fact *=i
#         i-=1
#         print(fact)
#     semphore.release()
#     return fact
# t1 = threading.Thread(target=factorial)
# t2 = threading.Thread(target=factorial)
# t1.start()
# t2.start()


# number = 5
# fact1 = 1
# fact2 = 1

# def partial_fact(start, end, result_holder, index):
#     result = 1
#     for i in range(start, end - 1, -1):
#         result *= i
#         print(threading.current_thread())

#     result_holder[index] = result

# result_holder = [1, 1]

# t1 = threading.Thread(target=partial_fact, args=(6, 4, result_holder, 0))  # 5*4*3
# t2 = threading.Thread(target=partial_fact, args=(3, 1, result_holder, 1))  # 2*1

# t1.start()
# t2.start()
# t1.join()
# t2.join()

# fact = result_holder[0] * result_holder[1]
# print(f"Factorial of {number} is {fact}")
# event = threading.Event()
# def prints():
#     print ( "hello world ")
#     event.wait()
#     print("performing the condition")

# s= input("enter y / n ")
# t1 = threading.Thread(target=prints)
# t1.start()
# if s =="y":
#     event.set()

path = "temp.txt"
text = ""
def readingText():
    global path,text
    while True:
        with open(path,"r") as f:
            text = f.read()
            time.sleep(5)
def printText():
    for i in range(50):
        print(text)
        time.sleep(5)
t1 = threading.Thread(target=readingText,daemon=True)
t2 = threading.Thread(target=printText)
t1.start()
t2.start()