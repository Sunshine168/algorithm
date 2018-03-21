/**
 * @param {number[]} nums
 * @return {number[][]}
 */


var threeSum = function(nums) {
  const result = [] 
  if(!nums || nums.length < 2){
      return result
  }
  
  nums = nums.sort((a,b)=>a-b)
      
  const twoSum = function(rightIndex,target){
      let j = rightIndex
      for(let i = 0;i<=j ;i++){
          if(i>0 && nums[i-1]===nums[i]) continue;
          
          while(j>i && nums[i]+nums[j]>target){
              j--;
          }
          
          if(i>=j){
              break;
          }
          
          if(nums[i]+nums[j] === target){
              result.push([nums[i],nums[j],-target])
          }
      }
  }


  for(let i=2;i<nums.length;i++){
      if(i+1<nums.length && nums[i]=== nums[i+1]) continue;
      twoSum(i-1,-nums[i])
  }
  
  
  
  return result

  
};