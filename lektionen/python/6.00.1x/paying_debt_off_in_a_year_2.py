# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
balance = 320000
annualInterestRate = 0.2
mfp = 0.01

def remainingBalance(b, mfp):
  ub = b - mfp
  for i in range(0, 12):
    b = ub + annualInterestRate / 12 * ub 
    ub = b - mfp
  return b

b = remainingBalance(balance, mfp)

while b > 0:
  mfp += 0.01
  b = remainingBalance(balance, mfp)

print("Lowest Payment:", mfp)
