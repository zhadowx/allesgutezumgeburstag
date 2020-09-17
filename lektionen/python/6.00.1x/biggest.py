animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
  '''
  aDict: A dictionary, where all the values are lists.

  returns: The key with the largest number of values associated with it
  '''
  big = 0
  index = 0
  keys = []
  values = []

  for e in aDict.values():
    values.append(e)

  for k in aDict.keys():
    keys.append(k)

  for i in range(len(values)):
    if len(values[i]) > big:
      big = len(values[i])
      index = i
      
  return keys[index]

print(biggest(animals)) #'d'