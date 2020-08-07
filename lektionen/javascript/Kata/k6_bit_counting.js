var countBits = function(n) {
  var arr = n.toString(2).split('');
  var result = 0;
  for(let i = 0; i <= arr.length; i++) {
    if (arr[i] == "1") {
      result++;
    }
  }
  return result;
};

//Another version

var countBits = n => n.toString(2).split('0').join('').length;