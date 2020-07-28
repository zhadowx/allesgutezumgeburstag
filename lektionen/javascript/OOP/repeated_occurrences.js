//Repeated occurrence
var str = /behaviou?r/;
console.log(str.test("behaviour"));
//true
console.log(str.test("behavior"));
//true

console.log(/'\d+'/.test("'123'")); //true

var heartyLaugh = /Ha+(Ha+)+/i;
console.log(heartyLaugh.test("HaHaHaHaHaHaaaaaaaaa"));
//true

console.log(/cat/.test('a black cat')); //true
console.log(/\bcat/.test('a black cat')); //true
console.log(/\bcat/.test('tomcat')); //false
console.log(/cat\b/.test('tomcat')); //true
console.log(/\bcat\b/.test('a black cat')); //true
console.log(/\bcat\b/.test('concatenate')); //false

var match = /\d+/.exec("There are 100 ways to do this");
console.log(match);
// ["100"]
console.log(match.index);
// 10

//Alternatives -OR
//expressed using | (pipe) character
//Ex /a|b/ matches either the a or b character

//Beginning
// /^test/ -> matches only if substring at the beginning

//End
// /test$/ -> matches on ly if substring at the end

 //Backreferences
 var orig = "1234 5678";
 var re = /(\d{4}) (\d{4})/;
 var modifiedStr = orig.replace(re, "$2 $1");
 console.log(modifiedStr); //outputs "5678 1234"

//Greedy and lazy quantifiers 
 function trim(str) {
  return (str || "").replace(/^\s+|\s+$/g, "");
}
console.log("--"+trim("   test   ")+"--");
//"--test--"

re = /\s+/g;
console.log('There are    a lot    of spaces'.replace(re, ' '));
//"There are a lot of spaces"

