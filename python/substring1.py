class Solution(object):
    def strStr(self, source, target):
        # write your code here
        if target == "" :
                return 0
        if source is None or target is None:
            return -1
        if source == target :
            return 0
        current = 0
        for i in range(0, len(source)):
            flag = 0
            if (len(target)>0 and source[i] == target[0] ):
                # 进一步判断
                current = i
                flag += 1
                start = current + 1
                for j in range(1, len(target)):
                    if (len(source) - start <len(target) - j):break;
                    #print(source[start], target[j])
                    if source[start] == target[j]:
                     flag += 1
                     start+=1
                    else:
                        break
            if (flag == len(target)): return current

        return -1
a = Solution()
print(a.strStr("tartarget" , "target"))