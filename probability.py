import random
from tqdm import tqdm
import math
trialls = 100000


def experiment(target_value):
    ev = 0  
    for i in tqdm(range(trialls)):
        s = get_sum()
        if s == target_value:
            ev +=1
    prob = ev/trialls
    print(prob)
    print(1/36)

def get_sum():
    first = dice_roll()
    second = dice_roll()
    return first+second
def dice_roll():
    return random.choice([1,2,3,4,5,6])
# import itertools,math
# from tqdm import tqdm
# def factorail(number):
#     result = 1 
#     for i in tqdm(range(number,0,-1)): 
#         result *= i
#     return result
# print(factorail(1000000))
# experiment(2)
s = [1,10,2 , -10,3]
s.sort()
print(s)
def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    s = [(i,j) for i,j in enumerate(nums)]
    s = sorted(s,key=lambda x : x[1])
    print(s)
    # l = 0 
    # r = len(nums)-1 
    # while l < r : 
    #     if nums[l] + nums[r] == target:
    #         return [l,r]
    #     if nums[l] + nums[r] > target:
    #         r-=1
    #         continue
    #     if nums[l] + nums[r] < target:
    #         l+=1
    #         continue 
s = "1"
for i in s:
    print(int(i))
def myAtoi( s):
    """
    :type s: str
    :rtype: int
    """
    negative = False 
    s = s.strip()
    num = 0 
    for i in range(len(s)):
        if i != 0 and  not s[i].isdigit():
            break
        if i == 0 and s[i] == "-":
            negative = True 
            continue 
        num = num *10 
        num = num + int(s[i])
    if (negative ):
        num *= -1 
    return num
print(myAtoi("words and 987"))