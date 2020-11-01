def valid_parentheses(string):
  if string.count("(") != string.count(")"):
    return False

  string2 = ""
  for c in string:
    if c == "(" or c == ")":
      string2+=c

  length = str(len(string2))
  total = 0
  while string2.count("()") > 0:
    total+= string2.count("()")
    string2 = string2.replace("()", "")

  return 2*total == int(length)  

print(valid_parentheses("tr(iyiai)(zc)dcdjas)ujymacxo(wbzvuqnhjug"))