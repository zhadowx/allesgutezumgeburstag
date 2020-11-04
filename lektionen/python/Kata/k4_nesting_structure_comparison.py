def same_structure_as(original,other):
  if type(original) != type(other):
    return False
  if len(original) != len(other):
    return False
  if len(original) == 0 and len(other) == 0:
    return True
  for i in range(len(original)):
    if type(original[i]) == list:
      if type(other[i]) == list:
        return same_structure_as(original[i], other[i])
      else:
        return False
    else:
      if type(other[i]) == list:
        return False
      else:
        continue
  return True

print(same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ]))     