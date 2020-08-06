//getters are methods to get the value of specific properties
//setters are methods that set the value of a property

var person = {
  firstname: "Albert",
  lastname: "Einstein",
  setLastName: function(_lastname) {
    this.lastname = _lastname;
  },
  setFirstName: function(_firstname) {
    this.firstname = _firstname;
  },
  getFullName: function() {
    return this.firstname + ' ' + this.lastname;
  }
};
person.setLastName('Newton');
person.setFirstName('Isaac');
console.log(person.getFullName()); 

//Using ECMAScript 5:

var person = {
  firstname: "Albert",
  lastname: "Einstein",
  get fullname() {
    return this.firstname + " " + this.lastname;   
  },
  set fullname(_name) {
    var words = _name.toString().split(' ');
    this.firstname = words[0];
    this.lastname = words[1];
  }
};

person.fullname = "Isaac Newton";
console.log(person.firstname); //"Isaac"
console.log(person.lastname); //"Newton"
console.log(person.fullname); //"Isaac Newton"

//Using Object.defineProperty()
var person = {
  firstname: "Albert",
  lastname: "Einstein",
};
Object.defineProperty(person, 'fullname', {
  get: function() {
    return this.firstname + ' ' + this.lastname;
  },
  set: function(name) {
    var words = name.split(' ');
    this.firstname = words[0];
    this.lastname = [1];
  }
});
person.fullname = "Isaac Newton";
console.log(person.firstname); //"Isaac"
console.log(person.lastname); //"Newton"
console.log(person.fullname); //"Isaac Newton"

//Some object methods

//Object.keys() returns an array of a given object's own enumerable
//property names -this function do not traverse up the prototype
//chain

var testobj = {
  name: 'Albert',
  age: 90,
  profession: 'Physicist'
};
console.log(Object.keys(testobj));
//["name", "age", "profession"]

//Object.values() returns an array of a given object's own enumerable
//property values, in the same order that is provided by a for... in loop
//only difference is that a for...in  loop enumerates properties in the prototype
//chain as well

function Scientist() {
  this.name = 'Albert';
}
Scientist.prototype.married = true;
aScientist = new Scientist();
console.log(Object.values(aScientist));
// ["Albert"]
