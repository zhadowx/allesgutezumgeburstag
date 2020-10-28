def McNuggets(n):
  """
  n is an int

  Returns True if some integer combination of 6, 9 and 20 equals n
  Otherwise returns False.
  """
  arr = [0, 0, 0]
  cases = {"-1": [-1, -1, -1], "-2":[-1, -1, 0], "-3":[-1, 0, -1], "-4":[0, -1, -1], 
  "-5":[-1, 0, 0], "-6":[0, -1, 0], "-7":[0, 0, -1],"1":[0, 0, 1], "2":[0, 1, 0], 
  "3":[1, 0, 0], "4":[0, 1, 1], "5":[1, 0, 1], "6":[1, 1, 0], "7": [1, 1, 1]}
  
  for i in range(len(arr)):
    arr[i] = n//35

  arr2 = arr[:]
  a = arr2[0]
  b = arr2[1]
  c = arr2[2]
  
  if 6*a + 9*b +20*c == n:
    return True

  for i in cases.keys():
    for j in range(len(arr)):
      arr2[j] += cases[i][j]
      a = arr2[0]
      b = arr2[1]
      c = arr2[2]
    if 6*a + 9*b + 20*c == n:
      return True
    else:
      arr2 = arr[:]
     
  return False

print(McNuggets(75))
