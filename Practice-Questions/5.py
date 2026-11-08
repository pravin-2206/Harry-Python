# frequency counter

def frequencyCounter(nums: list[int]) -> dict:
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq
print(frequencyCounter([10,20,10,12,13]))