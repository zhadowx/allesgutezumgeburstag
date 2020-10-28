# Write a Python function that creates and returns a list 
# of prime numbers between 2 and N, inclusive, sorted in 
# increasing order. A prime number is a number that is 
# divisible only by 1 and itself. This function takes in 
# an integer and returns a list of integers.

def primes_list(N):
  '''
  N: an integer
  '''
  aList = [2]

  def check(i, aList):
    for e in aList:
      if i % e == 0:
        return False
    return True

  for i in range(3, N+1):
    if check(i, aList):  
      aList.append(i)
  return aList
print(primes_list(74))

# def primes_list(N):
#   '''
#   N: an integer
#   '''
#   aSet = {2}
#   for i in range(2, N+1):
#     for j in range(2, N+1):
#       if i % j == 0:
#         break
#       else:
#         aSet.add(i)
#   aList = []
#   for e in aSet:
#     aList.append(e)
# #   return aList
# print(primes_list(74))


