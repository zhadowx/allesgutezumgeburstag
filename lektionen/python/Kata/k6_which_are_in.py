def in_array(array1, array2):
  arr = []
  for e in array1:
    for i in array2:
      if e in i and e not in arr:
        arr.append(e)
  return sorted(arr)

print(in_array(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))