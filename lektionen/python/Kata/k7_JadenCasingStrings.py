def to_jaden_case(string):
  arr =  string.split(' ')
  for i in range(len(arr)):
    temp1 = arr[i][0].upper()
    temp2 = arr[i][1:]
    arr[i] = temp1 + temp2
  string = ' '.join(arr)
  return string


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))