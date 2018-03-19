class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        restul = []
        if nums is None or len(nums)<2:
            return None
        
        start, end = 0 , len(nums) - 1
        
        while(start < end):
            if(nums[start] + nums[end] == target):
                return [start + 1,end + 1]
            
            if(nums[start] + nums[end] < target):
                start += 1
            else:
                end -=1
        
        return None