/**
 * @param nums: The integer array you should partition
 * @param k: An integer
 * @return: The index after partition
 */
const partitionArray = function (nums, k) {
       
  if(!nums || nums.length ===0){
      return 0
  }
  
  let start = 0 ,
      end = nums.length - 1
    
   while(start<=end){
       while(start <= end && nums[start]<k){
           start++
       }
       while(start <= end && nums[end]>=k){
           end --
       }
       if(start<=end){
           let temp = nums[end]
           nums[end] = nums[start]
           nums[start] = temp
           start++
           end--
       }
   }
   return start
}

