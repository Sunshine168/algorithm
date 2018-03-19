class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        disc = {}
        count = 0
        for i in nums:
            disc[i] = True

        index = 0
        for j in disc:
            nums[index] = j
            index+=1
        return index
            