"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        
        balance,temp = self.helper(root)
        return balance
        
    def helper(self,root):
        #叶子节点
        if root is None:
            return True,0
        

        leftValidtion,leftCount = self.helper(root.left)
        rightValidtion,rightCount = self.helper(root.right)
        
        if leftValidtion is False:
            return False,0
        
        if rightValidtion is False:
            return False,0
            
        return abs(leftCount - rightCount) <= 1,max(leftCount,rightCount) + 1
        