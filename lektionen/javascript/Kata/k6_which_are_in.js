function inArray(array1,array2){
  let arr = [];
  let arr2 = [];
  array1.forEach(str => {arr = arr.concat(array2.join(' ').match(str));});
  arr.forEach(x => {
    if (x != null) {
      arr2.push(x);
    }
  });
  return arr2.sort();
}
