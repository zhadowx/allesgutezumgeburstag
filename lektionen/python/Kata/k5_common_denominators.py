def convertFracts(lst:list) -> list:
  if len(lst) == 0: return []
  def isCommonDivisor(n:int,denoms:list) -> bool:
    """Checks whether an integer is a common divisor among a list of denominators"""
    c = 0
    for i in denoms: 
      if n % i == 0:
        c+=1
    if c == len(denoms):
      return True
    return False
    
  #check within denominators
  denoms = [x[1] for x in lst]
  hd = max(denoms)
  if isCommonDivisor(hd, denoms):
    lcd = hd
  #check multiples of highest denominator:
  else:
    um = 1
    for i in denoms:
      if i != hd:
        um*=i 
    for j in range(um*hd, 1, -hd):
      if isCommonDivisor(j, denoms):
        lcd = j

  return [[lcd//x[1]*x[0],lcd] for x in lst]

print(convertFracts([[1, 3], [1, 6], [1, 15]]))