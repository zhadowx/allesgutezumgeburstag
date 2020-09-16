def gcdIter(a, b):
  if a < b  and b % a == 0:
    return a
  elif b < a and a % b == 0:
    return b
  else:
    if a < b:
      for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
          return i
    else:
      for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
          return i

print(gcdIter(2, 12))   # 2
print(gcdIter(6, 12))   # 6
print(gcdIter(9, 12))   # 3
print(gcdIter(17, 12))  # 1


def gcdRecur(a, b):
  if a > b:
    if b == 0:
      return a
  else:
    if a == 0:
      return b
  if a > b:
    return gcdRecur(b, a % b)
  else:
    return gcdRecur(a, b % a)

print(gcdRecur(2, 12))  # 2
print(gcdRecur(6, 12))  # 6
print(gcdRecur(9, 12))  # 3
print(gcdRecur(17, 12)) # 1


