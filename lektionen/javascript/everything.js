function every(array, test) {
  if (array == 0) {
    return null;
  }
  for (let i of array) {
    if (!test(i)) {
      return false;
    }
  }
  return true;
}

console.log(every([1, 3, 5], n => n < 10));
console.log(every([2, 4, 16], n => n < 10));
console.log(every([], n => n < 10));


function every2(array, test) {
  if (array == 0) {
    return null;
  }
  return !array.some(element => !test(element));
}

console.log(every2([1, 3, 5], n => n < 10));
console.log(every2([2, 4, 16], n => n < 10));
console.log(every2([], n => n < 10));
