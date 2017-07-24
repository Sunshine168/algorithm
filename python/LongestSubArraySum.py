#
# #此方法的时间复杂度为O(n^3)。
# def sum(arr):
#     maxSum = arr[0]
#     currentSum = 0
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             for k in range(i,j):
#                 currentSum+=arr[k]
#                 if(currentSum>maxSum):
#                     maxSum=currentSum
#             #求[i,j]中的和完毕后清空当前求和
#             currentSum = 0
#
#     return maxSum
#
# test = [1, -2, 3, 10, -4, 7, 2, -5]
# print(sum(test))
#
# def sum2(arr):
#     maxSum = 0
#     currentSum = arr[0]
#     #理解如果加上元素arr[i]后当前和仍小于元素arr[i] 说明从arr[i]可以开始一个新的子列了
#     for i in range(len(arr)):
#         currentSum =  currentSum+arr[i] if arr[i]+currentSum > arr[i] else arr[i]
#         maxSum = currentSum if currentSum > maxSum else maxSum
#     return maxSum
#
#
# print(sum2(test))

#拓展
# 如果数组是二维数组，同样要你求最大子数组的和列?
# 如果是要你求子数组的最大乘积列?
# 如果同时要求输出子段的开始和结束列?

test2 = [[1, -2, 3, 10, -4, 7, 2, -5],[1, -2, 3, 10, -4, 7, 2, -5]]
def sum3(arr):
    currentSum = arr[0][0]
    maxSum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            currentSum = currentSum + arr[i][j] if currentSum + arr[i][j]>arr[i][j] else arr[i][j]
            maxSum = currentSum if currentSum > maxSum else maxSum
    return maxSum

print(sum3(test2))

#子列最大乘积(同理)
# 如果同时要求输出子段的开始和结束列?
# 默认开始是第一个元素,每次触发 currentSum = arr[i][j] /重制起点
# 终点元素是 currentSum if currentSum > maxSum else maxSum 记录结束点

