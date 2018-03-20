const sortColors2 = function (colors, k) {
  let pl = 0,
      pr = colors.length -1,
      min = 1,
      max = k,
      i = 0;
      
      while(min<max){
         // i是浮标
          while(i<=pr){
              if(colors[i]===min){
                  // 左边一定是最小的
                  const temp = colors[i]
                  colors[i] =  colors[pl]
                  colors[pl] = temp
                  pl++;
                  i++;
              } else if(colors[i]===max){
                  // 右边一定是最大的
                  const temp = colors[i]
                  colors[i] = colors[pr]
                  colors[pr] = temp;
                  pr--;
              }else{
                  i++
              }
          }
          i=pl
          max--
          min++
      }
}

