#解决subSets模板
# 先判断输入的list是否存在与长度是否大于0
# 使用一个subSetsHelper
# params依次 是字符串本身,起始坐标,深度遍历临时存储的temp_list ret是结果
# https://www.kancloud.cn/kancloud/data-structure-and-algorithm-notes/73049


class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """

    def subsets(self, S):
        result = []
        if(S is None ):
            return result
        def subSetsHelper(nums,startIndex,temp_list,ret):
            #生成新对象
            ret.append([]+temp_list)
            for i in range(startIndex,len(nums)):
                #先添加,再移除
                temp_list.append(nums[i])
                subSetsHelper(nums,i+1,temp_list,ret)
                temp_list.pop()
        S.sort()
        subSetsHelper(S,0,[],result)
        return result



solution = Solution()
b=solution.subsets([1,2,3])
print(b)