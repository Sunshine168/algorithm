/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let arr = []
    for(let i = 0 ;i< nums.length;i++){
        let color = nums[i]
           console.log(color)
           if(!arr[color] ){
               arr[color] = 1 
           }else{
                arr[color] += 1
           }
           
    } 
    let index= 0 
    for(let i =0 ;i<arr.length;i++){
        let count = arr[i]
        while(count>0){
            nums[index++] = i
            count--
        }
    }

};