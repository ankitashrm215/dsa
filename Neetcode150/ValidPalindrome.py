'''
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
'''
def ValidPalindrome(s):
    l = len(s)
    i = 0
    j = l-1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True

print(ValidPalindrome("Was it a car or a cat I saw?")) #expected True
print(ValidPalindrome("race a car")) #expected False
print(ValidPalindrome("A man, a plan, a canal: Panama")) #expected True