def sortedSequres(nums):
    left = 0 
    right = len(nums)-1 
    for i in range(len(nums)):
        nums[i] = nums[i] **2 
    l = []
    while left <=right: 
        if nums[left] > nums[right]:
            l.append(nums[left])
            left +=1 
        else: 
            l.append(nums[right])
            right -= 1 
    l.reverse()
    for i in range(len(l)):
        nums[i] = l[i] 
nums = [-2,-1,0,1,2,4,5,7]
sortedSequres(nums)
print(nums)
