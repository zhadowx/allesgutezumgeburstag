function Person() {}
Person.prototype.cry = function() {
  console.log("Crying");
}
function Child() {}
Child.prototype = {cry: Person.prototype.cry};
var aChild = new Child();
console.log(aChild instanceof Child); //true
console.log(aChild instanceof Person); //false
console.log(aChild instanceof Object); //true

SubClass.prototype = new SuperClass();
Child.prototype = new Person();

function Person() {}
Person.prototype.cry = function() {
  console.log("Crying");
}

function Child() {}
Child.prototype = new Person();
var aChild = new Child();
console.log(aChild instanceof Child); //true
console.log(aChild instanceof Person); //true
console.log(aChild instanceof Object); //true

function Employee() {
  this.name = '';
  this.dept = 'None';
  this.salary = 0.00;
}

function Manager() {
  Employee.call(this);
  this.reports = [];
}
Manager.prototype = Object.create(Employee.prototype);

function IndividualContributor() {
  Employee.call(this);
  this.active_projects = [];
}
IndividualContributor.prototype = Object.create(Employee.prototype);

function TeamLead() {
  Manager.call(this);
  this.dept = "Software";
  this.salary = 100000;
}
TeamLead.prototype = Object.create(Manager.prototype);

function Engineer() {
  TeamLead.call(this);
  this.dept = "Javascript";
  this.desktop_id = "8822";
  this.salary =  80000;
}
Engineer.prototype = Object.create(TeamLead.prototype);

var genericEmployee = new Employee();
console.log(genericEmployee);

var karen = new Manager();
karen.name = "Karen";
karen.reports = [1,2,3];
console.log(karen);

var jason = new TeamLead();
jason.name = "Json";
console.log(jason);

Employee.prototype.name = "Undefined";
//Slight variation
function Employee() {
  this.dept = 'None';
  this.salary = 0.00;
}
Employee.prototype.name = '';

function Manager() {
  this.reports = [];
}
Manager.prototype = new Employee();
var sandy = new Manager();
var karen = new Manager();
Employee.prototype.name = 'Junk';
console.log(sandy.name); //Junk
console.log(karen.name); //Junk

//Extending properties of native objects

String.prototype.reverse = function() {
  return Array.prototype.reverse.apply(this.split('')).join('');
};
var str = 'Javascript';
console.log(str.reverse()); //'tpircSavaJ'
