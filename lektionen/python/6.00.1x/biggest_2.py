animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
  '''
  aDict: A dictionary, where all the values are lists.

  returns: The key with the largest number of values associated with it
  '''
  max_big = 0
  for e in aDict:
    temp = aDict[e]
    if len(temp) > max_big:
      max_big = len(temp)
      max_key = e
  return max_key

print(biggest(animals)) #'d'