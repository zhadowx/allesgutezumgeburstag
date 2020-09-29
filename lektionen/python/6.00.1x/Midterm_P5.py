def f(i:int) -> int:
  '''f takes in an integer, applies a function, returns another integer'''
  return i + 2


def g(i:int) -> bool:
  """
  g takes in an integer, applies a Boolean function,
    returns either True or False
  """
  return i > 5


def applyF_filterG(L, f, g):
  ''' 
  Assumes L is a list of integers
  Assume functions f and g are defined for you.
  Mutates L such that, for each element i originally in L, L contains
    i if g(f(i)) returns True, and no other elements
  Returns the largest element in the mutated L or -1 if the list is empty
  '''
  M = L[:]
  for e in M:
    if not g(f(e)):
      L.remove(e)

  if len(L) > 0:
    return max(L)
  else:
    return -1



L = [0, -10, 5, 6, 7, 10, -4]
print(applyF_filterG(L, f, g))
print(L)
