var outer = 'I am outer'; //Define a value in global scope
function outerFn() { //Declare a function in global scope
  console.log(outer);
}
outerFn(); // prints -I am outer.

//A bit more complex
var outer = 'Outer'; //Variable declared in global scope
var copy;
function outerFn() { //Function declared in global scope

  var inner = 'Inner'; //Variable has function scope only, can not be 
  // accessed from outside
  function innerFn() { //Inner function within outer function,
    //both global context and outer
    //context are available hence can access
    //'outer' and 'inner'
    console.log(outer);
    console.log(inner);
  }
  copy = innerFn;   //Store reference to inner function,
  //because 'copy' itself is declared
  //in global context, it will be available
  //outside also
}
outerFn();
copy(); //Can't invoke innerFn() directly but can invoke via a
//variable declared in global scope

var outer = 'outer';
var copy;
function outerFn() {
  var inner = 'inner';
  function innerFn(param) {
    console.log(outer);
    console.log(inner);
    console.log(param);
    console.log(magic);
  }
  copy = innerFn;
}
console.log(magic); //ERROR: magic not defined
var magic = "Magic";
outerFn();
copy("copy");