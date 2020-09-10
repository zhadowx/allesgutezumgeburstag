function convertFrac(lst){
  var num =[];
  var den = []; 
  var lcd;
  var result = [];
  var ans = "";

  for (let element of lst) {
    num.push(element[0]);
    den.push(element[1]);
  }
//If the greatest denominator from the array is also the LCD
  if (den.every(x => Math.max(...den) % x == 0)) {
    lcd = Math.max(...den);
    for (let i = 0; i < den.length; i++) {
      result.push([]);
      result[i].push(lcd / den[i] * num[i]);
      result[i].push(lcd);
    }
    for (let i = 0; i < result.length; i++) {
      ans += "(" + result[i][0].toString() + "," + result[i][1].toString() + ")"
    }
    return ans;
  }
//If not, start from the product of the denominators and try to guess 'g'
//by taking steps of multiples of the greatest denominator until it reaches
//the product of the denominators divided by the greatest denominator, if 
//any multiples are found, then the lowest stays the product of the denominators
 
  else {
    lcd = den.reduce((a, b) => a * b);
    var g = [];

    for (let i = 2; i < lcd / Math.max(...den); i++) {
      g.push(Math.max(...den) * i);
    }

    for (let i = g.length - 1; i >= 0; i--) {
      if (den.every(x =>  g[i] % x == 0)){
        lcd = g[i];
      }
    }

    for (let i = 0; i < den.length; i++) {
      result.push([]);
      result[i].push(lcd / den[i] * num[i]);
      result[i].push(lcd);
    }

    for (let i = 0; i < result.length; i++) {
      ans += "(" + result[i][0].toString() + "," + result[i][1].toString() + ")"
    }

    return ans;
  }
}