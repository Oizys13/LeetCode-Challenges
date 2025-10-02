"""
Given a string s, find the length of the longest substring without duplicate characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        substring = str(s[0])
        lengthOfLongestSubstring = 1

        while right < len(s)-1:
            if(s[right] not in substring[:-1]):
                right +=1
                substring = s[left:right+1]

            if(s[right] in substring[:-1]):
                left += 1
                substring = s[left:right+1]
            
            if len(substring ) > lengthOfLongestSubstring :
                lengthOfLongestSubstring = len(substring )

        return lengthOfLongestSubstring          

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring(""))
print(sol.lengthOfLongestSubstring(" "))
print(sol.lengthOfLongestSubstring("au"))
print(sol.lengthOfLongestSubstring("dvdf"))