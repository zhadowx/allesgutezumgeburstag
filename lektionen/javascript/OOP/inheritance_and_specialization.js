// Inheritance and specialization

//When a class inherits from another class, it inherits all the elements
//that compose the parent class, also known as superclass. The class tha 
//inherits all the elements of the parent class is known as the subclass.

//Method overloading: define a method with the same name multiple times by 
//passsing different arguments.

//Method overriding: when a subclass provides a different implementation of
//a method defined in a superclass with the same name, same arguments, and 
//same return type

//Polymorphism: the use of the same method, the same name, and the same 
//arguments to cause different things to happen according to the class in 
//which we invoke a method

//Creating objects that specialize behavior in Javascript

function Animal() {}

Animal.prototype.numberOfLegs = 0;
Animal.prototype.pairsOfEyes = 0;
Animal.prototype.age = 0;

Animal.prototype.printLegsAndEyes = function() {
  console.log("I have " + this.numberOfLegs + " legs and " + this.pairsOfEyes * 2 + " eyes.");  
}

Animal.prototype.printAge = function() {
  console.log("I am " + this.age + " years old.");
}

//Using the prototype-based inheritance in Javascript

function Mammal() {}
Mammal.prototype = new Animal();
Mammal.prototype.constructor = Mammal;
Mammal.prototype.isPregnant = false;
Mammal.prototype.pairsOfEyes = 1;
//After we change the value of the Mammal.prototype property, we will assign  the Mammal
//constructor function to the Mammal.constructor property in order to clean up the side
//effects on the constructor property when you change the value of a prototype.
//We override the value of the pairsOfEyes propertywith 1

//Overriding methods in Javascript
function DomesticMammal() {}
DomesticMammal.prototype = new Mammal();
DomesticMammal.prototype.constructor = DomesticMammal;
DomesticMammal.prototype.name = "";
DomesticMammal.prototype.favoriteToy = "";

DomesticMammal.prototype.talk = function() {
  console.log(this.name + ": talks");
}

function Dog() {}
Dog.prototype = new DomesticMammal();
Dog.prototype.constructor = Dog;
Dog.prototype.numberOfLegs = 4;
Dog.prototype.breed = "Just a dog";
Dog.prototype.breedFamily = "Dog";

Dog.prototype.printBreed = function() {
  console.log(this.breed);
}

Dog.prototype.printBreedFamily = function() {
  console.log(this.breedFamily);
}

Dog.prototype.bark = function(times, otherDomesticMammal, isAngry) {
  var message = this.name;
  if (otherDomesticMammal) {
    message += " to " + otherDomesticMammal.name + ": ";
  }
  else {
    message += ": ";
  }
  if (isAngry) {
    message += "Grr ";
  }
  if (!times) {
    times = 1;
  }
  message += new Array(times + 1).join("Woof ");
  console.log(message);  
}

Dog.prototype.talk = function() {
  this.bark(1);
}
//the talk method overriden in the Dog prototype invokes the bark method
//without parameters because dogs bark and don't talk.

function TerrierDog() {}
TerrierDog.prototype = new Dog();
TerrierDog.prototype.constructor = TerrierDog;
TerrierDog.prototype.breed = "Terrier dog";
TerrierDog.prototype.breedFamily = "Terrier";

function SmoothFoxTerrier() {}
SmoothFoxTerrier.prototype = new TerrierDog();
SmoothFoxTerrier.prototype.constructor = SmoothFoxTerrier;
SmoothFoxTerrier.prototype.breed = "Smooth Fox Terrier";

SmoothFoxTerrier.create = function(name, age, favoriteToy, isPregnant) {
  var dog = new SmoothFoxTerrier();
  dog.name = name;
  dog.age = age;
  dog.favoriteToy = favoriteToy;
  dog.isPregnant = isPregnant;
  return dog;
}
//The preceding code declares a create funciton for the SmoothFoxTerrier construction
//function.

//Overloading operators in Javascript
//JavaScript doesn't allow you to overload operators; therefore
//we can create methods to achive our goal

Animal.prototype.lessThan =  function(other) {
  return this.age < other.age;
}

Animal.prototype.lessOrEqualThan = function(other) {
  return this.age <= other.age;
}

Animal.prototype.greaterThan = function(other) {
  return this.age > other.age;
}

Animal.prototype.greaterOrEqualThan = function(other) {
  return this.age >= other.age;
}

//Understanding polymorphism in JavaScript
var tom = SmoothFoxTerrier.create("Tom", 5, "Sneakers");
tom.printBreed();
tom.printBreedFamily();
var pluto = SmoothFoxTerrier.create("Pluto", 6, "Tennis ball");
var goofy = SmoothFoxTerrier.create("Goofy", 8, "Soda bottle");

console.log(tom.greaterThan(pluto));
console.log(tom.lessThan(pluto));
console.log(goofy.greaterOrEqualThan(tom));
console.log(tom.lessOrEqualThan(goofy));

tom.bark();
tom.bark(2);
tom.bark(2, pluto);
tom.bark(3, pluto, true);



