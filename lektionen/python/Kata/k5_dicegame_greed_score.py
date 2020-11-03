def score(dice:list) -> int:
  s = 0
  copy = dice[:]
  values = [1, 2, 3, 4, 5, 6]
  threes = [1000, 200, 300, 400, 500, 600]
  ones = [100, 0, 0, 0, 50, 0]
  for n in values:
    if dice.count(n) >= 3:
      s+=threes[values.index(n)]
      for i in range(3):
        copy.remove(n)
      break
  for n in copy:
    s+=ones[n-1]
  return s

print(score([2, 4, 4, 5, 4]))