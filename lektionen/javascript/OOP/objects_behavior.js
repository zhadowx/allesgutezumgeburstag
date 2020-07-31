//Behavior of Objects 

//name of properties
var nothing = {};
var author = {
  "first-name": "Douglas",
  "last-name": "Crockford"
};

var author = {
  firstname : "Douglas",
  lastname : "Crockford",
  book : {
    title: "Javascript- The Good Parts",
    pages: "172"
  }
};

//Accessing properties
console.log(author['firstname']); //Douglas
console.log(author.lastname); //Crockford
console.log(author.book.title); //Javascript- The Good Parts
console.log(author.age); //undefined
console.log(author.age || "No Age Found"); //No Age Found
author.book.pages = 190;
console.log(author.book.pages); //190

//Methods
var meetingRoom = {};
meetingRoom.book = function(roomId) {
  console.log("booked meeting room -"+roomId);
}
meetingRoom.book("VL");

//Prototypes, default property for almost all objects
//Object.getPrototypeOf() returns the prototype of an object

//A function that returns nothing and creates nothing
function Player () {}
//Add a function to the prototype property of the function
Player.prototype.usesBat = function() {
  return true;
}

//We call player() as a function and prove that nothing 
//happens 
var crazyBob = Player();
if (crazyBob === undefined) {
  console.log("CrazyBob is not defined");
}

//Now we call player() as a constructor along with 'new'
//1. The instance is created
//2. method usesBat() is derived from the prototype of the function
var swingJay = new Player();
if (swingJay && swingJay.usesBat && swingJay.usesBat()) {
  console.log("swingJay exists and can use bat");
}

//Instance properties vs Prototype properties

//Instance Properties
function Player() {
  this.isAvailable = function() {
    return "Instance method says - he is hired";
  };
}
Player.prototype.isAvailable = function() {
  return "Prototype method says - he is Not hired";
};
var crazyBob = new Player();
console.log(crazyBob.isAvailable());

//Use of this
//this is used in a global context
function globalAlias() {
  return this;
}
console.log(globalAlias()); //[object window]
// this is used in an object method
var f = {
  name: "f",
  func: function() {
    return this;
  }
};
console.log(f.func());
//prints -
//[object Object] {
//  func: function() {
//    return this;
//  },
//  name: "f"
//}

//this is used in a constructor function
var member = "global";
function f()
{
  this.member = "f";
}

var o = new f();
console.log(o.member); // f

// instance properties take precedence to prototype properties

function Player() {
  isAvailable = false;
}
var crazyBob = new Player();
Player.prototype.isAvailable = function() {
  return isAvailable;
}
console.log(crazyBob.isAvailable()); //false
//object is checked for the existence of the property
//if found, property is returned, if not
//associated prototype is checked, if found, it is returned
//if not, an undefined error is returned
