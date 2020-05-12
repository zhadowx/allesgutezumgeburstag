/*for (let size = 8; size >= 1; size--) {
  if (size % 2 == 0) {
    console.log(" " + "#" + " " + "#" + " " + "#" + " " + "#");
  }  
  else {
    console.log("#" + " " + "#" + " " + "#" + " " + "#" + " ");
  }
}
*/

/*
let string = "";
let size = 8;
for (let c_string = (size * size + size) ; c_string >= 0; c_string--) {
  if (string.length % (size+1) == 0) {
    string += "\n"
  }
  else if (string.length % 2 == 0) {
    string += "#";
  }
  else {
    string += " ";
  }
}
console.log(string);*/

let board = "";
let size = 8;
for (let y = 0; y < size; y++){
  for (let x = 0; x < size; x++){
    if((x + y) % 2 == 0) {
      board += " ";
    }
    else {
      board += "#";
    }
  }
  board += "\n";
}
console.log(board);
