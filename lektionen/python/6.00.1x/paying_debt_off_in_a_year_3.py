balance = 320000
annualInterestRate = 0.2

lb = balance / 12
upb = balance * (1 + annualInterestRate / 12)**12 / 12.0
mb = (lb + upb) / 2.0

def remainingBalance(b, mb):
  ub = b - mb
  for i in range(0, 12):
    b = ub + annualInterestRate / 12 * ub 
    ub = b - mb
  return b

b = remainingBalance(balance, mb)

while abs(b) >= 0.01:
  if b > 0:
    lb = mb
    mb = (lb + upb) / 2.0
    b = remainingBalance(balance, mb)
  else:
    upb = mb
    mb = (lb + upb) / 2.0
    b = remainingBalance(balance, mb)


print("Lowest Payment:", round(mb, 2))