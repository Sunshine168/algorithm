/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
  const result = []
  if(!root){
      return result
  }
  const queue = []
  queue.push(root)
  
  while(queue.length>0){
      const arr = []
      const { length } = queue
      for(let i = 0 ;i< length;i++){
          const head = queue.shift()
          if(head.left){
              queue.push(head.left)
          }
          if(head.right){
              queue.push(head.right)
          }
          arr.push(head.val)
      }
      result.push(arr)
  }
  return result
};