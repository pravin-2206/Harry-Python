def firstDuplicate(nums: list[int]) -> int:
    s=set()
    for num in nums:
        if num in s:
            return num
        s.add(num)
    return -1
print(firstDuplicate([1,2,3,3,4,5,5]))