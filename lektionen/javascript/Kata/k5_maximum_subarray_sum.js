var maxSequence = function(arr){
  if (arr.length == 0) {
    return 0;
  }
  else if (arr.every(x => x >= 0)) {
    return arr.reduce((a,b) => a + b);
  }
  else if (arr.every(x => x < 0)) {
    return 0;
  }
  else {
    var result = 0;
    for (i = 0; i <= arr.length - 2; i++){
      for(j = arr.length; j >= i + 2 ; j--) {
        if (result == 0 || result < arr.slice(i, j).reduce((a,b) => a + b)) {
          result = arr.slice(i, j).reduce((a, b) => a + b);
        }
      }
    }
    arr.forEach(x => {
      if (x > result) {
        result = x;
      }
    });  
  return result;
  }
}