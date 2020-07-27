//Timers and callbacks
function delay(message) {
  setTimeout (function timerFn() {
    console.log(message);
  }, 1000);
}
delay("Hello World");

//Private variable
function privateTest() {
  var points = 0;
  this.getPoints = function() {
    return points;
  };
  this.score = function() {
    points++;
  };
}

var private = new privateTest();
private.score();
console.log(private.points); //undefined
console.log(private.getPoints());

//Loops and closures
for (var i = 1; i <= 5; i++) {
  setTimeout (function delay() {
    console.log(i);
  }, i * 100);
}

for (var i = 1; i <= 5; i++) {
  (function(j) {
    setTimeout(function delay() {
      console.log(j);
    }, j * 100);
  })(i);
}