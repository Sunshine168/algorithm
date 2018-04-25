var longestPrefix = function(s) {
  let maxLength = 0;
  if (!s || s.length === 0) {
    return maxLength;
  }
  for (let i = 0; i < s.length - 1; i++) {
    if (s.charCodeAt(i) <= s.charCodeAt(i + 1)) {
      maxLength += 1;
    } else {
      break;
    }
  }
  return maxLength > 0 ? maxLength + 1 : maxLength;
};

console.log(longestPrefix("knotty"));