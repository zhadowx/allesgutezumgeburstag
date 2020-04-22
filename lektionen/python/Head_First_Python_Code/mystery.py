def double(arg):
  """Old object reference still exists in the calling code and its value hasn't changed >>by-value argument passing<<"""
  print('Before: ', arg)
  arg = arg * 2
  print('After: ', arg)

def change(arg):
  """As there's no assignment, there's no overwriting of the object references, so the value changes >>by-address argument passing<<"""
  print('Before: ', arg)
  arg.append('More data')
  print('After: ', arg)

num = 10
double (num) 
print('Origin: ', num)

saying = 'Hello'
double(saying)
print('Origin: ', saying)

numbers = [42, 256, 16]
double(numbers)
print('Origin: ', numbers)

change(numbers)
print('Origin: ', numbers)