def array_diff(a, b):
  result = []
  for e in a:
    if e not in b:
      result.append(e)
  return result

print(array_diff([1,2],[1]))
print(array_diff([1,2,2,2,3],[2]))