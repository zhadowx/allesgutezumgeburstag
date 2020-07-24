//Anonymous functions while creating an object
var santa = {
  say: function() { //property known as a method and not a function
    console.log("ho ho ho");
  }
}
santa.say();

//Anonymous functions while creating a list
var things = [
  function() { alert ("ThingOne") },
  function() { alert ("ThingTwo") },
];
for (var x = 0; x < things.length; x++) {
  things[x]();
}

//Anonymous functions as a parameter to another function
//function statement
function eventHandler(event) {
  event();
}

eventHandler(function() {
  //do a lot of event related things
  console.log("Event fired");
});

//Anonymous functions in conditional logic
var shape;
if (shape_name === "SQUARE") {
  shape = function() {
    return "drawing sqaure";
  }
}
else {
  shape = function() {
    return "drawing square";
  }
}
alert(shape());
