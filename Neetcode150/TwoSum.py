'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.
'''

def twoSumBruteForce(nums, target):
    ''' Time Complexity: O(n^2)
        Space Complexity: O(1)'''

        res = []
        l = len(nums)
        if l == 0:
            return res

        for i in range(0, l-1):
            for j in range(i+1, l):
                if nums[i]+nums[j] == target:
                    return [i, j]
        return res


def twoSumOptimised(nums, target):
    ''' Time Complexity: O(n)
        Space Complexity: O(n)'''

        l = len(nums)
        if l == 0:
            return []

        diffDict = {}
        for index, num in enumerate(nums): #enumerate on a list returns elements index and number
            diff = target - num
            if diff in diffDict: #find diff in the dictionary
                return [diffDict[diff], index]
            else:
                diffDict[num] = index
        return []

print("Result is", twoSumBruteForce([3,4,5,6], 7))
print("Result is", twoSumOptimised([3,4,5,6], 7))