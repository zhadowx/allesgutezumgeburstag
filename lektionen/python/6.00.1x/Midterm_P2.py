def getSublists(L:list, n:int) -> list:
  """
  L =  a list of integers, assume L not empty
  n = an integer, assume 0 < n <= len(L)
  returns a list of all possible sublists in L of 
  length n without skipping elements in L
  """
  sublists = []
  while len(L) >= n:
    sublists.append(L[:n])
    L = L[1:]
  return sublists

print(getSublists([1, 1, 1, 1, 4], 2))