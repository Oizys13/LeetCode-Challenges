class Solution(object):
    def isPalindrome(self, x):
        s = str(x)

        # Reverse the string
        rev_s = s[::-1]

        # Compare the original string with the reversed string
        return s == rev_s   
    

# Test the function
Solutionclass = Solution()
    
print(Solutionclass.isPalindrome(121))  # Output: True
print(Solutionclass.isPalindrome(-121))  # Output: False
print(Solutionclass.isPalindrome(10))  # Output: False    