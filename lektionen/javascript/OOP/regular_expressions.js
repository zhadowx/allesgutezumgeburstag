//Regular Expressions or RegEx
var pattern = /test/;
var pattern = new RegExp("test");

var pattern = /orange/;
console.log(pattern.test("orange")); //true

var patternIgnoreCase = /orange/i;
console.log(patternIgnoreCase.test("Orange")); //true

var patternGlobal = /orange/ig;
console.log(patternGlobal.test("Orange Juice")); //true

//Exact match -sometimes refered to as simple patterns

var pattern = /[abc]/;
console.log(pattern.test('a')); //true
console.log(pattern.test('d')); //false

var pattern = /[^abc]/;
console.log(pattern.test('a')); //false
console.log(pattern.test('d')); //true

var pattern = /[0 - 5]/;
console.log(pattern.test(3)); //true
console.log(pattern.test(12345)); //true
console.log(pattern.test(9)); //false
console.log(pattern.test(6789)); //false
console.log(/[0123456789]/.test("This is year 2015")); //true

var strToMatch = 'A toyota: Race fast, safe car: A Toyota!';
var regExAt = /Toy/;
var arrMatches = regExAt.exec(strToMatch);
console.log(arrMatches);

var strToMatch = 'A toyota: Race fast, safe car: A Toyota!';
var regExAt = /Toy/g;
var arrMatches = regExAt.exec(strToMatch);
console.log(arrMatches);

var strToMatch = 'A toyota: Race fast, safe car: A Toyota!';
var regExAt = /Toy/;
var arrMatches = strToMatch.match(regExAt);
console.log(arrMatches);

var strToMatch = 'Blue is your favorite color?';
var regExAt = /Blue/;
console.log(strToMatch.replace(regExAt, "Red"));
//output- "Red is your favorite color?"

var sColor = 'sun, moon, stars';
var reComma = /\,/;
console.log(sColor.split(reComma));
//Output - ["sun", "moon", "stars"]

var strToMatch = 'wooden bat, smelly Cat, a fat cat';
var re = /[bcf]at/gi;
var arrMatches = strToMatch.match(re);
console.log(arrMatches);
//["bat", "Cat", "fat", "cat"]

var strToMatch = 'i1,i2,i3,i4,i5,i6,i7,i8,i9';
var re = /i[0-5]/gi;
var arrMatches = strToMatch.match(re);
console.log(arrMatches);
//["i1", "i2", "i3", "i4", "i5"]

var strToMatch = 'i1,i2,i3,i4,i5,i6,i7,i8,i9';
var re = /i[^0-5]/gi;
var arrMatches = strToMatch.match(re);
console.log(arrMatches);
//["i6", "i7", "i8", "i9"]

