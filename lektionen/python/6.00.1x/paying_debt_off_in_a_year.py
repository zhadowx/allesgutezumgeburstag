
# balance -the outstanding balanceon the credit card
# annualInterestRate -annual interest  rate as decimal
# monthlyPaymentRate -minimum monthly payment rate as decimal
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Result Your Code Should Generate Below:
# Remaining balance: 31.38
b = balance
mmp = monthlyPaymentRate * b
ub = b - mmp

for i in range(1, 13):
  b = ub + annualInterestRate / 12 * ub 
  mmp = monthlyPaymentRate * b
  ub = b - mmp

print("Remaining balance:", round(b, 2))
