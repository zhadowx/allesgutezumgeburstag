function range(start, end, step = 1) {
  let arr = [];
  if ((step > 0) && (start <= end)) {
    for (; start <= end; start += step){
      arr.push(start);
    }
   }
  else if ((step > 0) && (start >= end)) {
    for (; start >= end; start -= step) {
      arr.push(start);
    }
   } 
  else if ((step < 0) && (start >= end)) {
    for (; start >= end; start += step) {
      arr.push(start);
    }
   } 
  else {
    for (; start <= end; start -= step) {
      arr.push(start);
    }
   } 
   
  return arr;
}

function sum (arr) {
  let total = 0;
  for (let elem of arr) {
    total += elem;
  }
  return total;
}

console.log(range(1, 10));
console.log(sum(range(1, 10)));
console.log(range(1, 10, 2));
console.log(sum(range(1, 10, 2)));
console.log(range(5, 2, -1));
console.log(sum(range(5, 2, -1)));
console.log(range(1, 10, -1));
console.log(sum(range(1, 10, -1)));
console.log(range(5, 1, -2));
console.log(sum(range(5, 1, 2)));
console.log(range(7, 1));
console.log(sum(range(7, 1)));


