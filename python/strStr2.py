class Solution(object):
    def strStr(self, source, target):
     BASE = 10000000
     if source is None or target is None :
         return
     m = len(source)
     n = len(target)
     source = list(source)
     target = list(target)
     if m == 0 or n == 0 :
         return

     # 算出减去时候基准的幂
     power = 1
     for i in range(0,len(target)):
         power = ( power * 31 ) % BASE

     # 算出 targetcCode
     targetCode = 0
     for i in range(0,len(target)):
         targetCode = (targetCode * 31 + ord(target[i])) % BASE

     # hashCode
     hashCode = 0
     for i in range(0,len(source)):
         hashCode = ( hashCode * 31 + ord(source[i])) % BASE
         if i < n - 1:
             continue

         #abcd - a
         if n <= i:
             hashCode  = hashCode - ( ord(source[i - n]) * power ) % BASE
             if hashCode < 0:
                hashCode = BASE + hashCode

         if hashCode == targetCode :
             # print(source[i-n+1:i+1])
             if(source[i-n+1:i+1] == target):
                 return i - n + 1
     return -1




solution = Solution()

a = solution.strStr("abcdabcdefg","bcd")
print(a)
