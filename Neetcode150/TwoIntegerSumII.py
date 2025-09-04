'''
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
There will always be exactly one valid solution.
'''

def TwoIntegerSumII(numbers, target):
    l = len(numbers)
    i = 0
    j = l - 1
    while i < j:
        total = numbers[i] + numbers[j]
        if total == target:
            return [i+1, j+1]
        elif total < target:
            i = i + 1
        else:
            j = j - 1
    return []
print(TwoIntegerSumII([1,2,3,4], 3))