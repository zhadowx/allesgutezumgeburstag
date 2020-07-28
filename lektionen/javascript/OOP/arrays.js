//Arrays

var arr = new Array(1,2,3); //Array constructor
var arr = Array(1,2,3); // Array function
var arr = [1,2,3]; //Array literal

var arr = [10];
var arr = Array(10); //Creates an array with no element
//but with length set to 10
//The above code is equivalent to 
var arr = [];
arr.length = 10;

var days =[];
days[0] = "Sunday";
days[1] = "Monday";

var arr_generic = new Array("A string", myCustomValue, 3.14);
var fruits = ["Mango", "Apple", "Orange"];

var arr = [
'string', 42.0, true, false, null, undefined,
['sub', 'array'], {object: true}, NaN
];

var days = ["Sunday", "Monday", "Tuesday"]

var colors = [];
colors[30] = ['Green'];
console.log(colors.length); //31

var colors = ['Red', 'Blue', 'Yellow'];
console.log(colors.length); //3
colors.length = 2;
console.log(colors); //['Red'], 'Blue'] - yellow removed
colors.length = 0;
console.log(colors); // [] the colors array is empty
colors.length = 3;
console.log(colors); //[undefined, undefined, undefined]

//Iterating over the values of an array
var colors = ['red', 'gree', 'blue'];
for (var i = 0; i < colors.length; i++) {
  console.log(colors[i]);
}

var colors = ['red', 'blue', 'green'];
colors.forEach(function(color) {
  console.log(color);
});

var colors = ['red', 'blue', 'green'];
colors.forEach(color => console.log(color));

//concat() method joins two arrays into a new array
var myArray = new Array("33", "44", "55");
myArray = myArray.concat("3", "2", "1");
console.log(myArray);
//["33", "44", "55", "3", "2", "1"]

//join() method joins all elements of an array into a string
var myArray = new Array("Red", "Blue", "Yellow");
var list = myArray.join(" ~ ");
console.log(list);
//"Red ~ Blue ~ Yellow"

//pop() method removes last element from an array and returns it
var myArray = new  Array("1", "2", "3");
var last = myArray.pop();
//myArray = ["1", "2"], last = "3"

//push() method adds one or more elements to the end and returns
//the resulting length of the array
var myArray = new Array("1", "2");
myArray.push("3");
//myArray = ["1", "2", "3"]

//shift() method removes the first element from an array
//and returns it
var myArray = new Array("1", "2", "3");
var first = myArray.shift();
//myArray = ["2", "3"], first = "1"

//unshift() method adds one or more elements to the front
//of any array and returns the new length of the array
var myArray = new Array("1", "2", "3");
myArray.unshift("4", "5");
//myArray = ["4", "5", "1", "2", "3"]

//reverse() method reverses or transposes the elements of an
//array- the first array element becomes the last and the las
//becomes the first
var myArray = new Array("1", "2", "3");
myArray.reverse();
//transposes the array so that myArray = ["3", "2", "1"]

//sort() method sorts the elements of an array
var myArray = new Array("A", "C", "B");
myArray.sort();
//sorts the array so that myArray = ["A", "B", "C"]

// indexOf(searchElement[, fromIndex]) searches the arrayfor searchElement
//and returns the index of the first match
var a = ['a', 'b', 'a', 'b', 'a', 'c', 'a'];
console.log(a.indexOf('b')); //1
//Again, starting from after the last match
console.log(a.indexOf('b', 2)); //3
console.log(a.indexOf('1')); //-1, 'q' is not found

//lastIndexOf(searchElement[, fromIndex]) works like indexOf
//but only searches backwards
var a = ['a', 'b', 'c', 'd', 'a', 'b'];
console.log(a.lastIndexOf('b')); //5
//Again, starting from before the last match
console.log(a.lastIndexOf('b', 4)); //1
console.log(a.lastIndexOf('z')); // -1

