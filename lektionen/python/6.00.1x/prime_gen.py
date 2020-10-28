def genPrimes():
  def isPrime(x:int):
    for p in primes:
      if x % p == 0:
        return False
    return True
  
  primes = [2]
  x = 3
  
  while True:
    next = primes[-1]
    if isPrime(x):
      yield next
      primes.append(x)
    else:
      while not isPrime(x):
        x+=1

# prime = genPrimes()
# print(prime.__next__())

# for n in genPrimes():
#   print(n)
