function solution(str){
  let re = /(\w{2})/ig
  let arr = str.split(re).filter(x => x != "");
  if (str.length % 2 == 0) {
    return arr;
  }
  else {
    arr[arr.length - 1] =  arr[arr.length - 1] + "_";
    return arr;
  }  
}

function solution(str){
  let re = /(\w{2})/ig
  let arr = str.split(re).filter(x => x != "");
  if (str.length % 2 == 0) {
    return arr;
  }
  else {
    arr.push(arr.pop() + "_");
    return arr;
  }  
}
