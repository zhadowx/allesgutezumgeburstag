def max_sequence(arr):
  if len(arr) == 0:
    return 0
    
  def all_neg(arr):
    for e in arr:
      if e > 0:
        return False
    return True

  if all_neg(arr):
    return 0

  total = 0
  for i in range(len(arr)):
    for j in range(i+1, len(arr) + 1):
      if sum(arr[i:j]) > total:
        total = sum(arr[i:j])

  return total


print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))