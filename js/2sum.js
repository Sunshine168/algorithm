/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  const map = new Map()
  let result = []
  for(let i =0 ;i<nums.length;i++){
        // stored index
        map.set(nums[i],i)
  }
  
  for(let i= 0 ;i<nums.length;i++){
      let value2 = target - nums[i]
      if(map.has(value2) && map.get(value2)!==i){
          return [i,map.get(value2)]
      }
  }
};