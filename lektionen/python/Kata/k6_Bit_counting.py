def count_bits(n):
  s = "{0:b}".format(n)
  return s.count("1")

print(count_bits(1234))