var countChange = function(money, coins) {
  //Create a counter 
  var c = 0
  for (let num of coins) {
    if (money % num == 0) {
      c++;
    }
  }
  if (coins.reduce((a, b) => a + b) == money) {
    c++;
  }
  if (coins.includes(1)) {
    for (let num of coins) {
      if (num != 1) {
        c++;
      }
    }
  }
  for (let i = 0; i < coins.length; i++) {
  
  }
};