import math
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        s = 0 
        for j in range(1,n-i):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                s+=1
        if s==0:
            break
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index =j
        arr[i],arr[min_index] = arr[min_index],arr[i]
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        j = i 
        while j >  0:
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
            else:
                break
            j-=1
def merge_sort(arr):
    n = len(arr)
    if n ==1 :return arr
    m = len(arr)//2 
    L = arr[:m]
    R = arr[m:]
    L= merge_sort(L)
    R = merge_sort(R)
    l,r =0,0
    L_len = len(L)
    R_len  = len(R)
    sorted_arr = [0]*n
    i = 0 
    while l<L_len  and r<R_len:
        if L[l]<R[r]:
            sorted_arr[i] = L[l]
            l+=1
        else:
            sorted_arr[i] = R[r]
            r+=1
        i+=1
    while l<L_len:
        sorted_arr[i] = L[l]
        l+=1
        i+=1
    while r<R_len:
        sorted_arr[i] = R[r]
        r+=1
        i+=1
    return sorted_arr
def quick_sort(arr):
    if len(arr)<=1 : 
        return arr
    p = arr[-1]
    L=[l for l in arr[:-1 ] if l<=p ]
    R = [r for r in arr[:-1] if r>p]
    L = quick_sort(L)
    R = quick_sort(R)
    return L+[p]+R
def counting_sort(arr):
    arr = [abs(i) for i in arr]
    max = arr[0]
    for i in range(1,len(arr)):
        if max < arr[i]:
            max = arr[i]
    couting_arr = [0]*(max+1)
    print(couting_arr)
    for i in arr:
        couting_arr[i] +=1
    i = 0 
    for j in range(len(couting_arr)): 
        while couting_arr[j] > 0 :
            arr[i] = j
            couting_arr[j] -=1
            i+=1

    return arr
# a = [100,-2,8,7,-1,0,15]
# b = ["mohamed",2,True,22.021]
# c = ["mohamed","ahmed","ramadan","iman"]

# c.sort(key=lambda t:t[1] if len(t) > 0 else t[0])
# print(c)
import itertools
values ="123456789TJQK"
shape = "cdha"
cards = []
for value in values:
    for s in shape:
        cards.append(value+s)
subsets = set(itertools.combinations(cards,5))
print(len(subsets))
import math
print( math.factorial(52)/(math.factorial(5)*math.factorial(52-5)))