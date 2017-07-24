# 字符串相关的问题在各大互联网公司笔试面试中出现的频率极高，
# 比如微软经典的单词翻转题：
# 输入“I am a student.”，则输出“student. a am I”。

str1 = "I am a student."

def reverseStr(str):
    result = ""
    temp  = str.split(" ")
    return ' '.join(temp[::-1])
print(reverseStr(str1))