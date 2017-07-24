#给定一个字符串，求它的最长回文子串的长度。
#O(N)解法



def sub(str):
   processStr = "#"+  "#".join([x for x in str])+"#"
   id = 0
   max = 0
   p = [0]*len(processStr)
   for i in range(1,len(processStr)):
       p[i] =  min(p[2 * id -i],max - i) if i < max else 1
       #
       while (p[i] + i<len(processStr) and i - p[i]>=0) and (processStr[p[i]+i] == processStr[i-p[i]]):
           p[i] += 1
       if i+p[i] > max :
           id = i
           max = i + p[i]
   print(p)
   return  sorted(p,reverse=bool(1))[0]-1


# p[i] = mx > i ? min(p[2 * id - i], mx - i): 1;
# while (s[i + p[i]] == s[i - p[i]])
print(sub("abaaaaaba"))

