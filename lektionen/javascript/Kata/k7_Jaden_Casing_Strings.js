String.prototype.toJadenCase = function () {
  var arr = this.split(" ");
  var str_arr;
  var finstr = ""
  while (arr.length > 0) {
    if (arr.length > 1) {
      var re = /^\w/gi;
      var match = arr[0][0].replace(re, arr[0][0].toUpperCase());
      str_arr = arr.shift();
      str_arr = str_arr.substring(1);
      finstr+=(match+str_arr+" ");
    }
    else {
      var re = /^\w/gi;
      var match = arr[0][0].replace(re, arr[0][0].toUpperCase());
      str_arr = arr.shift();
      str_arr = str_arr.substring(1);
      finstr+=(match+str_arr);
    }
  }
  return finstr;
};

var str = "How can mirrors be real if our eyes aren't real";
str.toJadenCase();
//"How Can Mirrors Be Real If Our Eyes Aren't Real"
