def solution(s):
  arr = []
  if len(s) % 2 == 0:
    for i in range(0, len(s), 2):
      arr.append(s[i:i+2])
  else:
    s+="_"
    for i in range(0, len(s), 2):
      arr.append(s[i:i+2])

  return arr

print(solution('abcdefg'))