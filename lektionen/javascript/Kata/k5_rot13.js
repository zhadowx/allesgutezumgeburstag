function rot13(str) {
  let secret = "";
  for (let i = 0; i < str.length; i++) {
    if ((str.charCodeAt(i) >= 65 && str.charCodeAt(i) <= 77) ||
      (str.charCodeAt(i) >= 97 && str.charCodeAt(i) <= 109)) {
      secret += (String.fromCharCode(str.charCodeAt(i) + 13));
    }
    else if ((str.charCodeAt(i) >= 78 && str.charCodeAt(i) <= 90)
      || (str.charCodeAt(i) >= 110 && str.charCodeAt(i) <= 122)) {
      secret += (String.fromCharCode(str.charCodeAt(i) - 13));
    }
    else {
      secret += str[i];
    }
  }
  return secret;
}