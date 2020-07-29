//A map is a simple key-value map and can iterate its elements
//in the order of their insertion

var founders = new Map();
founders.set("facebook", "mark");
founders.set("google", "larry");
founders.size; //2
founders.get("twitter"); //undefined
founders.has("yahoo"); //false

for (var [key, value] of founders) {
  console.log(key + " founded by " + value);
}
//facebook founded by mark
//google founded by larry

//Sets are collections of values and can be iterated in the
//order of the insertion of their elements
//a value can occur only once!
var mySet = new Set();
mySet.add(1);
mySet.add("Howdy");
mySet.add("foo");
mySet.add("foo");

mySet.has(1); //true
mySet.delete("foo");
mySet.size; //2

for (let item of mySet) console.log(item);
//1
//"Howdy"