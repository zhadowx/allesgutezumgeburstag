var recoverSecret = function(triplets) {
  var secret = "";
  var set = new Set();
  var arr = [];
  var triparr = [];
  var c = 0;
  var index_sum_arr = [];

  triplets.forEach(x => x.forEach(y => set.add(y)));
  set.forEach(x => arr.push(x));
  triplets.forEach(x => triparr.push(x));

  while (secret.length < arr.length) {
    for (let i = 0; i < arr.length; i++) {
      index_sum_arr.push(0);
      for (let j = 0; j < triparr.length; j++) {
        if (triparr[j].includes(arr[i])) {
          index_sum_arr[i] += triparr[j].indexOf(arr[i]);
        } 
      }
    }

    for (let i = 0; i < index_sum_arr.length; i++) {
      if (index_sum_arr[i] == 0 && secret.indexOf(arr[i]) == -1) {
        secret += arr[i];
      }
    }

    index_sum_arr = [];

    for (let element of triparr) {
      if (element.includes(secret[c])) {
        element.shift();
      }
    }

    c++;
  }
  return secret;
};
