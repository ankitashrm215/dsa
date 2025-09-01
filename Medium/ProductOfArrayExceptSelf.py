'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]
'''
def productExceptSelf(nums):
    
    ''' This is the brute force approach
    Time complexity: O(n*n) where n is the length of nums
    Space complexity: O(n) for allProd
    '''
    l = len(nums)
    allProd = []
    for i in range(0, l):
        j = 0
        prod = 1
        while j < l:
            if i != j:
                prod = prod * nums[j]
            j = j + 1
        allProd.append(prod)
    return allProd

def productExceptSelfOptimised(nums):

    ''' This is tthe prefix/postfix approach
    Time complexity: O(n) where n is the length of nums
    Space complexity: O(1) res doesn't count in the complexity
    '''
    l = len(nums)
        prefix = 1
        res = []
        for i in range(0, l):
            res.append(prefix)
            prefix = prefix * nums[i]
        
        postfix = 1
        for j in range(l-1, -1, -1):
            res[j] = res[j] * postfix
            postfix = postfix * nums[j]
        return res

print(productExceptSelf([1,2,4,6]))
print(productExceptSelfOptimised([1,2,4,6]))