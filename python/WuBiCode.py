def wubi(str):
  codeArr = [1+25+25*25+25*25*25,25+1+25*25,25+1,1]
  sum = 0
  for x in range(0,len(str)):
      sum+=codeArr[x]*( ord(str[x])-ord('a'))
  return len(str)-1+sum
print(wubi('aaaa'))