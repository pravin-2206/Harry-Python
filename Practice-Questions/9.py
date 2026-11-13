def findMax(nums: list[int]) -> int:
    # Write your solution here
    max=nums[0]
    for i in nums:
        if i>max:
            max=i
    return max
print(findMax([10,1,21,34,11]))
print(findMax([10,1,1,3,11]))
print(findMax([10,1,2,4,1,31,99]))