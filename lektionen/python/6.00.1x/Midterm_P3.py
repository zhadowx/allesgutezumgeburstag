def uniqueValues(aDict:dict) -> list:
  '''
  aDict: a dictionary
  returns a list
  '''
  aList = []

  iterator = list(aDict.values())
  iterator2 = aDict.items()

  for e in iterator:
    if iterator.count(e) == 1:
      for kv in iterator2:
        if kv[1] == e:
          aList.append(kv[0])

  return sorted(aList)

print(uniqueValues({"a":1, "b":1, "c":2, "d":3, "e":3, "f": 4, "g": 5}))