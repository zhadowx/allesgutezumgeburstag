let map = {one: true, two: true, hasOwnProperty: true};
/*let hasOwnPropertySymbol = Symbol("hasOwnProperty");
// console.log(map.hasOwnProperty("one"));
Object.prototype[hasOwnPropertySymbol] = function() {
  return this.hasOwnProperty;
};*/

// Fix this call
// console.log(map[hasOwnPropertySymbol]("one"));

Object.prototype.hasOwnProperty.call(map, "one");
// → true