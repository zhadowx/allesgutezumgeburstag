def f(a, b):
  return a > b


def dict_interdiff(d1, d2):
  '''
  d1, d2: dicts whose keys and values are integers
  Returns a tuple of dictionaries according to the instructions above
  '''
  intersect = {}
  difference = {}

  for k in d1.keys():
    if k in d2.keys():
      intersect[k] = f(d1.get(k), d2.get(k))
    else:
      difference[k] = d1.get(k)
  for k in d2.keys():
    if k not in d1.keys():
      difference[k] = d2.get(k)

  return tuple((intersect, difference))


print(dict_interdiff({1:30, 2:20, 3:30}, {1:40, 2:50, 3:60}))