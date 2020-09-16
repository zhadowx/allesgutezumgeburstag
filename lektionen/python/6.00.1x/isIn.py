def isIn(char, aStr):
  if len(aStr) == 0 or len(aStr) == 1:
    return False

  elif char == aStr[len(aStr)//2]:
    return True

  else:
    if char > aStr[len(aStr)//2]:
      return isIn(char, aStr[len(aStr)//2:len(aStr)])
    else:
      return isIn(char, aStr[0:len(aStr)//2])
