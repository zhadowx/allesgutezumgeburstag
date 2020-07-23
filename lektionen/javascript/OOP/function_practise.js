var a = 1;
function foo() {
  var a = 2;
  console.log(a);
}
foo();
console.log(a);


// IIFE: Inmediately Invoked Function Expressions
var a = 1;
(function foo() {
  var a = 2;
  console.log(a);
})();
console.log(a);

(function foo (b) {
    var a = 2;
    console.log(a + b);
}(3));


// Inline Function Expressions
function setActiveTab(activeTabHandler, tab) {
  //set active tab
  //call handler
  activeTabHandler();
}
setActiveTab( function () {
  console.log( "Setting active tab" );
}, 1 );


//Block Scopes
var foo = true;
if (foo) {
  let bar = 42; // variable bar is local in this block { }
  console.log( bar );
}
console.log( bar ); //ReferenceError

//Function Expression
functionOne();
//Error
//"TypeError: functionOne is not a function"
var functionOne = function() {
  console.log("functionOne");
};

//Function Declaration
functionTwo();
//No error
//Prints - functionTwo

function functionTwo() {
  console.log("FunctionTwo");
}

//Arguments Parameter
var sum = function() {
  var i, total = 0;
  for (i = 0; i < arguments.length; i++) {
    total += arguments[i];
  }
  return total;
};
console.log(sum(1,2,3,4,5,6,7,8,9));
console.log(sum(1,2,3,4,5));