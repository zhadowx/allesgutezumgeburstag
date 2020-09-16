import math

def polysum(n, s):
  '''
    Input:  n = # of sides (a positive float or int)
            s = length of side (a positive float or int)
    Output: returns a float rounded to 4 decimal places
  ''' 
  
  area =  (0.25 * n * s**2)/math.tan(math.pi/n)
  perimeter = n * s
  total = area + perimeter**2
  
  return round(total, 4)
