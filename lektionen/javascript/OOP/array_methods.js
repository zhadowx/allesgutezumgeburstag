function range(start = 0, end, step = 1) {
  var arr = [];
  for (; start <= end; start+=step) {
    arr.push(start);
  }
  return arr;
}
console.log(range(1,3));

function sum(arr) {
  var total = 0;
  arr.forEach((element) => total+=element);
  return total;
}
console.log(sum(range(1,10)));

//map() function produces a new array of values by mapping
//each value in the list thorugh a transformation function
console.log(range(1,3).map(function () {return 'a'}));
console.log(range(1,3).map(() => {return 'a'}));
console.log([1, 2, 3].map(num => {return num *3}));

//reduce() function reduces a list of values to a single value
var sum = [1, 2, 3].reduce((memo, num) => {
  console.log(memo, num);
  return memo + num}, 0);
console.log(sum);

//filter() iterates through the entire list and returns an array
//of all the elements that pass the condition
var evens = [1, 2, 3, 4, 5, 6].filter(num => {return num % 2 == 0});
console.log(evens);

var odds = [1, 2, 3, 4, 5, 6].filter(num => {return num % 2 !== 0});
console.log(odds);

//includes() determines wether an array includes a certain value
//among its entries; returning true of false as appropiate
console.log([1, 2, 3].includes(3)); //true
