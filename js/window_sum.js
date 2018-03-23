const winSum = function (nums, k) {
  if(!nums || nums.length < k){
      return []
  }
  
  const result = [] 
  let rIndex = k - 1,lIndex = 0
  while(rIndex<nums.length && k > 0){
      let sum;
      if(lIndex === 0){
         sum = 0 
      for(let i =lIndex ;i<=rIndex;i++){
          sum+=nums[i]
         }
      }else{
          sum = result[result.length -1 ]
          sum = sum - nums[lIndex-1] + nums[rIndex]
      }

      result.push(sum)
      lIndex++
      rIndex++
  }
  return result 
}
