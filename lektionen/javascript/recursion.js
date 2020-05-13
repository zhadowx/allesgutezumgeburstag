/*
  function isEven(number) {
    if (Math.abs(number) % 2 == 0) {
      return true;
    }
    else {
      return false;
    }
  }
  */

function isEven(n) {
  if (Math.abs(n) == 0) {
    return true;
  }
  else if (Math.abs(n) == 1) {
    return false;
  }
  else {
    return isEven(n-2);
  }
}

console.log(isEven(50));
console.log(isEven(75));
console.log(isEven(-1));

