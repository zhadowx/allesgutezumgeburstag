def count7(N:int) -> int:
  '''
  N: a non-negative integer
  returns 0 or a positive integer
  '''
  
  strin = str(N)
  if len(strin) == 1:
    if strin[0] == "7":
      return 1
    else: 
      return 0

  elif strin[-1] != "7":
    return 0 + count7(N//10)
  else: 
    return 1 + count7(N//10)

print(count7(772717))