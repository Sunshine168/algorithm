class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, S):
        # write your code here
        result = []
        if (S is None):
            return result

        def subSetsHelper(nums, startIndex, temp_list, ret):
            # 生成新对象
            ret.append([] + temp_list)
            for i in range(startIndex, len(nums)):
                # 先添加,再移除
                # 判断跳过的循环
                if (i != 0 and nums[i] == nums[i - 1] and i != startIndex):
                    continue
                temp_list.append(nums[i])
                subSetsHelper(nums, i + 1, temp_list, ret)
                temp_list.pop()

        S.sort()
        subSetsHelper(S, 0, [], result)
        return result
