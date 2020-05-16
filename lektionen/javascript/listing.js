function arrayToList(arr) {
  let list = {value: arr.pop(), rest: null};
  while (arr.length != 0) {
    let list2 = {value: arr.pop(), rest: list};
    list = list2;
  }
  return list;
}
console.log(arrayToList([10, 20]));


function listToArray(list) {
  let arr = [];
  while (list.rest != null) {
    arr.push(list.value);
    list = list.rest;
  }
  arr.push(list.value);
  return arr;
}
console.log(listToArray(arrayToList([10, 20, 30])));


function prepend(ele, list = {value: ele, rest: null}) {
  let list2 = {value: ele, rest: list};
  list = list2;
  return list;
}
console.log(prepend(10, prepend(20, null)));


function nth(list, index) {
  let arr = listToArray(list);
  if (index <= arr.length -1) {
    return arr[index];
  }
  else {
    return undefined;
  }
} 
console.log(nth(arrayToList([10, 20, 30]), 2));
