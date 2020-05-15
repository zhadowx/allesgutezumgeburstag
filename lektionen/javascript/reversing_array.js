/*
function reverseArray(arr) {
  let arr2 = [];
  while (arr.length != 0) {
    arr2.push(arr.pop());
  }
  return arr2; 
}
*/

function reverseArray(arr) {
  let arr2 = [];
  for (element of arr) {
    arr2.unshift(element);
  }
  return arr2;
}

function reverseArrayInPlace(arr) {
  for (element of arr.slice()) {
    arr.unshift(element);
  } 
  return arr;
}

let arrayValue = [1, 2, 3, 4, 5];
let arrayLetters = ["A", "B", "C", "D", "E"];

console.log(reverseArray(arrayValue));
console.log(reverseArray(arrayLetters));
console.log(reverseArray(["a", "b", "c", "d"]));

console.log(arrayValue);
console.log(arrayLetters);

console.log(reverseArrayInPlace(arrayValue));
console.log(reverseArrayInPlace(arrayLetters));
console.log(reverseArrayInPlace(["a", "b", "c", "d"]));

console.log(arrayValue);
console.log(arrayLetters);