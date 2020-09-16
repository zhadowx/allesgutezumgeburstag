def oddTuples(aTup):
  '''
  aTup: a tuple
  returns: tuple, every other element of aTup. 
  '''
  oddTup = ()

  for i in range(0, len(aTup)):
    if i % 2 == 0:
      oddTup += (aTup[i],)

  return oddTup
