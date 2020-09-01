/*Assume that the board comes in the form of a 3x3 array, 
where the value is 0 if a spot is empty, 1 if it is an 
"X", or 2 if it is an "O", like so:
*/

function isSolved(board) {
  let c0_1 = 0;
  let c0_2 = 0;
  let c1_1 = 0;
  let c1_2 = 0;
  let c2_1 = 0;
  let c2_2 = 0;

  for (let i = 0; i < board.length; i++) {
    if (board[i].every(x => x == 1)) {
      return 1;
    }
    if (board[i].every(x => x == 2)) {
      return 2;
    }

    if (board[i][0] == 1 ) {
      c0_1++;
    }
    if (board[i][0] == 2) {
      c0_2++;
    }
    if (board[i][1] == 1) {
      c1_1++;
    }
    if (board[i][1] == 2) {
      c1_2++;
    }
    if (board[i][2] == 1) {
      c2_1++;
    }
    if (board[i][2] == 2) {
      c2_2++;
    }
  }

  if((board[0][0] == 1 && board[1][1] == 1 && board[2][2] == 1) || 
    (board[0][2] == 1 && board[1][1] == 1 && board[2][0] == 1) ||
    c0_1 == 3 || c1_1 == 3 || c2_1 == 3) {
    return 1;
  }
  if((board[0][0] == 2 && board[1][1] == 2 && board[2][2] == 2) ||
  (board[0][2] == 2 && board[1][1] == 2 && board[2][0] == 2) ||
  c0_2 == 3 || c1_2 == 3 || c2_2 == 3) {
    return 2;
  }
  else {
    for (let i = 0; i < board.length; i++) {
      if (board[i].includes(0)) {
        return -1;
      }
    }
    return 0;
  }
}
