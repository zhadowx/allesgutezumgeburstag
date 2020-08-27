function validParentheses(parens){
  if (parens.length == 0) {
    return true;
  }
  
  var count = 0;
  var count2 = 0;
  var indexes = [];
  var indexes2 = [];
  var values = [];

  for (let i = 0; i < parens.length; i++) {
    if (parens[i] == "(") {
      count++;
      indexes.push(parens.indexOf("(", i));
      values.push(false);
    }
    else if (parens[i] == ")") {
      count2++;
      indexes2.push(parens.indexOf(")", i));
    }
  }

  for (let i = 0; i < indexes.length; i++) {
    if (indexes2[i] > indexes[i]) {
      values[i] = true;
    }
  }

  if (count == count2) {
    return values.every(x => x == true);
  }

  else {
    return false;
  }
}