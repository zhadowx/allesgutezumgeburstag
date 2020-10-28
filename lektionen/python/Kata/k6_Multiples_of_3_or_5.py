def solution(number):
  if number < 0:
    return 0
  total = 0

  for i in range(number):
    if i % 3 == 0 and i % 5 == 0:
      total+=i
    elif i % 3 == 0:
      total+=i
    elif i % 5 == 0:
      total+=i
  return total

print(solution(10))