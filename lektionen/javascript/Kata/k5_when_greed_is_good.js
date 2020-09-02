/*Greed is a dice game played with five six-sided dice. 
Your mission, should you choose to accept it, is to score a 
throw according to these rules. You will always be given an 
array with five six-sided dice values.
*/

/* Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point*/

/*A single dice can only be counted once in each roll. For example,
 a given "5" can only count as part of a triplet (contributing to 
  the 500 points) or as a single 50 points, but not both in the same roll.
*/

function score(dice) {
  let v_arr = [1000, 200, 300, 400, 500, 600];
  let c_arr = [0, 0, 0, 0, 0, 0];
  let sum = 0;

  for (let i = 0; i < dice.length; i++) {
    if (dice[i] == 1) {
      c_arr[0]++;
    }
    else if (dice[i] == 2) {
      c_arr[1]++;
    }
    else if (dice[i] == 3) {
      c_arr[2]++;
    }
    else if (dice[i] == 4) {
      c_arr[3]++;
    }
    else if (dice[i] == 5) {
      c_arr[4]++;
    }
    else {
      c_arr[5]++;
    }
  }

  if (c_arr[0] > 0) {
    if (c_arr[0] >= 3) {
      sum += v_arr[0];
      c_arr[0] -= 3;
    }
    sum += c_arr[0] * 100;
  }

  if (c_arr[4] > 0) {
    if (c_arr[4] >= 3) {
      sum += v_arr[4];
      c_arr[4] -= 3;
    }
    sum += c_arr[4] * 50;
  }

  for (let i = 1; i < c_arr.length; i++) {
    if (i != 4 && c_arr[i] >= 3) {
      sum += v_arr[i];
    }
  }

  return sum;
}
