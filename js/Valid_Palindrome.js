/**
 * @param s: A string
 * @return: Whether the string is a valid palindrome
 */
const isPalindrome = function (s) {
  if(s === null){
      return false
  }
  if(s.length === 0 || s.length ===1){
      return true
  }
  
  let start = 0,
      end = s.length -1
  
  while(start<=end){
      let left = s[start].toLowerCase(),
          right = s[end].toLowerCase()
      if(!/[0-9a-z]/.test(left)){
          start++
      }
      if(!/[0-9a-z]/.test(right)){
          end--
      }
      if(right===left){
          start++
          end--
      }else{
          break
      }
  }
  
  if(start >= end ){
      return true
  }
  return false
}

