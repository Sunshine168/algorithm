class Solution(object):
    def reverse(self, x):
        temp_x = x
        flag = 1
        temp = ""
        if temp_x < 0:
           flag = 1
           temp_x = -temp_x
           flag = -1
        temp_str = str(temp_x)
        for x in range(0,len(temp_str))[::-1]:
            temp+=temp_str[x]
        if int(temp) > 2 ** 31 - 1:
            return 0
        else:
            return flag * int(temp)


solution = Solution()
print(solution.reverse(-123))