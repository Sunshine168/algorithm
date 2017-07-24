# class Solution(object):
#     #判断是否为回文是返回长度,否返回0
#     def isPalindromic(self, s):
#         lastIndex = len(s)-1
#         count = 0
#
#         for x in range(0,len(s)):
#             if(s[x]!= s[lastIndex]):
#                 break
#             else:
#                 count+=1
#                 lastIndex-=1
#         return count if count==len(s) else 0
#
#     def longestPalindrome(self, s):
#        maxLength = 1;
#        maxStr = ""
#        if len(s) == 1:
#            return s
#        for x in range(0,len(s)):
#            for y in range(x+1,len(s)+1):
#                subStr = s[x:y]
#                nowLength = self.isPalindromic(subStr)
#                if nowLength>maxLength:
#                   maxLength = nowLength
#                   maxStr = subStr
#         #头尾子串
#        if s[0]==s[len(s)-1] and maxStr == "":
#            return s[0]
#        return maxStr
#

import math

class Solution(object):
    # Python O(N^2)常数比较大的话会TLE
    def longestPalindrome(self, s):
        ansl, ansr, maxx = 0, 1, 0
        length = len(s)
        for i in range(1, length * 2):
            if i & 1 :
                left = int(i / 2)
                right = left
            else :
                left = int(i / 2 - 1)
                right = left + 1
            while (left >= 0) and (right < length) and (s[left] == s[right]):
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left > maxx:
                maxx = right - left
                ansl = left
                ansr = right
        return s[ansl: ansr + 1]

solution =Solution()
temp = solution.longestPalindrome("abcda")
print(temp)

