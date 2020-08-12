//Using methods to add behavior to constructor functions
//Generating a constructor function to represent the mutable version
//of a 3D vector

function MutableVector3D(x, y, z) {
  var _x = x;
  var _y = y;
  var _z = z;

  Object.defineProperty(this, 'x', {
    get: function() {return _x;},
    set: function(val) {_x = val;}
  });

  Object.defineProperty(this, 'y', {
    get: function() {return _y;},
    set: function(val) {_y = val;}
  });
  
  Object.defineProperty(this, 'z', {
    get: function() {return _z;},
    set: function(val) {_z = val;}
  });
  
  this.sum = function(deltaX, deltaY, deltaZ) {
    _x += deltaX;
    _y += deltaY;
    _z += deltaZ;
  }
}
//We can add a function named originVector to generate a new instance
//of a class with all the values initialized to 0.

MutableVector3D.originVector = function() {
  return new MutableVector3D(0, 0, 0);
};

//Following code calls the originVector function to generate a 3D vector,
//calls the sum method for the generated instance, and prints all the values
var mutableVector3D = MutableVector3D.originVector();
mutableVector3D.sum(5, 10, 15);
console.log(mutableVector3D.x, mutableVector3D.y, mutableVector3D.z);

//Now we want to represent the inmutable version of a 3D vector
//we weill use  read-only properties for x, y and z.

function InmutableVector3D(x, y, z) {
  var _x = x;
  var _y = y;
  var _z = z;

  Object.defineProperty(this, 'x', {
    get: function() {return _x;}
  });

  Object.defineProperty(this, 'y', {
    get: function() {return _y;}
  });
  
  Object.defineProperty(this, 'z', {
    get: function() {return _z;}
  });
}

InmutableVector3D.prototype.sum = function(deltaX, deltaY, deltaZ) {
  return new InmutableVector3D(
    this.x + deltaX,
    this.y + deltaY,
    this.z + deltaZ);
};

InmutableVector3D.equalElementsVector = function(initialValue) {
  return new InmutableVector3D(initialValue, initialValue,
initialValue);
};

InmutableVector3D.originVector = function() {
  return InmutableVector3D.equalElementsVector(0);
};

//Following code calls the originVector method to generate a 3D vector,
//calls the sum method for the generated instance, and prints the values 

var vector0 = InmutableVector3D.originVector();
var vector1 = vector0.sum(5, 10, 15);
console.log(vector1.x, vector1.y, vector1.z);
