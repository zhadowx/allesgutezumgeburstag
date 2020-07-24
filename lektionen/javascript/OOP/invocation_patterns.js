//Invocation as a function
function add() {}
add();

var substract = function() {

};
substract();

//Invocation as a method
var person = {
  name: 'Albert Einstein',
  age: 66,
  greet: function () {
    console.log(this.name);
  }
};

person.greet();

//Invocation as a Constructor
var Person = function (name) {
  this.name = name;
};
Person.prototype.greet = function() {
  return this.name;
};
var albert = new Person('Albert Einstein');
console.log(albert.greet());

//Also can use apply() and call() methods to invoke functions
