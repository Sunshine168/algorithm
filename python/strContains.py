
# 给定两个分别由字母组成的字符串A和字符串B，
# 字符串B的长度比字符串A短。
# 请问，如何最快地判断字符串B中所有字母是否都在字符串A里？
str1 = "ABDDDDEC"
str2 = "ABDAESC"

#
def check(str1,str2):
    str1 = s = ''.join(sorted(list(str1)))
    str2 = "".join(sorted(list(str2)))
    pstr1 = 0
    pstr2 = 0
    while pstr2 < len(str2):
        while (pstr1 > len(str1)) and (str1[pstr1]<str[pstr2]):
           pstr1 += 1
        if pstr1 >= len(str1) or str1[pstr1]>str2[pstr2]:
           return bool(0)
    pstr2 +=1
    return bool(1)
check(str1,str2)

# if "a" > "b":
#     print("hello")
# else:
#     print("world")