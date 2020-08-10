function calculateArea(width, height) { return width * height;}
typeof(calculateArea)
var rectangleArea = calculateArea(300, 200);
console.log(rectangleArea);

//Working with constructor functions
var myObject = {};
typeof(myObject);
myObject

var myRectangle = {width: 300, height: 200};
typeof(myRectangle);
myRectangle

var myRectangle2 = {width: 500, height: 150};
// doing the previous can generate errors while typing

//Notice capitalized name of Rectangle, usually constructor 
//functions are capitalized
function Rectangle(width, height) {
  console.log("I'm creating a new Rectangle");
  this.width = width;
  this.height = height;
}

var rectangle1 = new Rectangle(293, 117);
var rectangle2 = new Rectangle(293, 137);

console.log(rectangle1);
console.log(rectangle2);
// Creating instances
function Rectangle(width, height) {
  console.log("I'm creating a new Rectangle");
  this.width = width;
  this.height = height;

  this.calculateArea = function() {
    return this.width * this.height;
  }
}
var rectangle3 = new Rectangle(143, 187);
rectangle3.calculateArea();
var rectangle4 = new rectangle3.constructor(300, 200);

function calculateArea(width, height) {
  return new Rectangle(width, height).calculateArea();
}
calculateArea(143, 187);
