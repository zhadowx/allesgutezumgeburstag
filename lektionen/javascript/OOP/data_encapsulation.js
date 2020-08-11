//Adding properties to a constructor function
//Defining a constructor function and adding attributes
//as properties of the constructor function

function ScottishFold(name, favoriteToy, energy) {
  this.name = name;
  this.favoriteToy = favoriteToy;
  this.energy = energy;
}

ScottishFold.generalHealth = 3;
ScottishFold.affectionateWithFamily = 5;
ScottishFold.intelligence = 4;
ScottishFold.kidFriendly = 5;
ScottishFold.petFriendly = 4;
//The preceding code assigns a value to properties of the
//ScottishFold constructor function after the definition of 
//the constructor function.

console.log(ScottishFold.generalHealth); //3

//You can assign a value to any constructor function property
ScottishFold.generalHealth = 4;

//Following lines of code create n instance with ScottishFold
//constructor function and the prints the value of generalHealth

var lucifer = new ScottishFold("Lucifer", "Tennis ball", 4,);
console.log(lucifer.constructor.generalHealth); //4

//Hiding data in Javascript with local variables
//Following code shows a new version of the ScottishFold constructor
// function that declares three local variables using var instead of
// this. prefix. In addition, the following code adds a  leading underscore
// (_) to the names

function ScottishFold(name, favoriteToy, energy) {
  var _name = name;
  var _favoriteToy = favoriteToy;
  var _energy = energy;
}
//Constructor function saves the values of all the three arguments in 
//local variables.

var lucifer = new ScottishFold("Lucifer", "Tennis ball", 4);
console.log(lucifer._name); //undefined
console.log(lucifer._favoriteToy); //undefined
console.log(lucifer._energy); //undefined

//Using property getters and setters in Javascript
//If we want a read-only name property; we define a getter method
function ScottishFold(name, favoriteToy, energy) {
  var _name = name;
  var _favoriteToy = favoriteToy;
  var _energy = energy;

Object.defineProperty(this, 'name', {get: function(){ return _name; }
});
}
//The code calls the Object.defineProperty function with the folowwing arguments:
// this: This is the instance.
//'name': This is the desired name for the property as a string.
//This is an object with the getter function code specified in the get property.
//Note that the getter function can access the _name variable defined in the 
//constructor function.

//After we add a getter method to define a read-only name property, we can create
//an instance of the edited constructor function and write code that reads, tries
// to chang, and reads again the value of the name read-only property:

var lucifer = new ScottishFold("Lucifer", "Tennis ball", 4);
console.log(lucifer.name); //"Lucifer"
lucifer.name = "Jerry";
console.log(lucifer.name); //"Lucifer"

//If we want to encapsulate the _favoriteToy local variable with a favoriteToy
//property; we have to define getter and setter methods. The getter method
//returns the value of the related _favoriteToy local variable. The Setter
//method receives the new favorite toy value as a val argument named and assigns 
//this value to the related _favoriteToy local variable.

function ScottishFold(name, favoriteToy, energy) {
  var _name = name;
  var _favoriteToy = favoriteToy;
  var _energy = energy;

  Object.defineProperty(this, 'name', { get: function(){return _name;} });
  Object.defineProperty(this, 'favoriteToy', { get: function() {return _favoriteToy;}, 
    set: function(val){_favoriteToy = val;} });
}

//The energy property requires a setter method with more code to transform values
//lower than 0 to 0 and values higher than 5 to 5.
function ScottishFold(name, favoriteToy, energy) {
  var _name = name;
  var _favoriteToy = favoriteToy;
  var _energy = energy;

  Object.defineProperty(this, 'name', { get: function(){return _name;} });
  Object.defineProperty(this, 'favoriteToy', { get: function() {return _favoriteToy;}, 
    set: function(val){_favoriteToy = val;} });
  Object.defineProperty(
    this,
    'energy', {
    get: function() {return _energy;},
    set: function(val) {
      if (val < 0) {
        _energy = 0;
      } else if (val > 5) {
        _energy = 5;
      } else {
        _energy = val;
      }
    }
  });
}
//We can create an instance of the edited class and try to set different values to this
//property

var garfield = new ScottishFold("Garfield", "Pillow", 1);
garfield.energy = -7;
console.log(garfield.energy);
garfield.energy = 35;
console.log(garfield.energy);
garfield.energy = 3;
console.log(garfield.energy);
