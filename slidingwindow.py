def maxSubstring(word):
    left = 0 
    right = 0 
    longest = 0
    sett = set()
    for i in range(len(word)):
        if word[right] in sett:
            sett.remove(word[right])
            left += 1
        else:
            sett.add(word[right])
            right +=1 
            longest = max(longest,right-left)
    return longest
print (maxSubstring("abcdmgacbabb"))
def maxAverage(nums,k):
    sum = 0 
    if k > len(nums):
        for i in nums:
            sum +=i
        return sum / len(nums)
    max_avg = -900000000000241407097341
    for i in range(k):
        sum +=nums[i]
    max_avg = max(max_avg,sum/k)
    for i in range(k,len(nums)):
        sum +=nums[i]
        sum -=nums[i-k]
        avg = sum / k 
        max_avg = max(avg,max_avg)
    return max_avg
print(maxAverage([10,11,12,13,14,15],2))



def subsets(nums):
    res , sol = [] , []
    res.append([])
    for i in range(len(nums)):
        res.append(nums[i])
    for i in range(len(nums)):
        sol.append(nums[i])
    res.append(sol)
    
print(subsets([1,2,3,4]))