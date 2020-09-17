animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
  '''
  aDict: A dictionary, where all the values are lists.

  returns: int, how many values are in the dictionary.
  '''
  total = 0
  for e in aDict.values():
    if type(e) == list:
      total+= len(e)
    else:
      total+= 1
  return total

print(how_many(animals))

