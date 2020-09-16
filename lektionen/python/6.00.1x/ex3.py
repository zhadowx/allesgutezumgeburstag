s = 'azcbobobegghakl'
x = []
s_s = "Longest substring in alphabetical order is: "
for n in range(0, len(s)):
  if n == 0:
    x.append(s[n])
  elif ord(s[n]) >= ord(s[n-1]):
    x[-1] = x[-1] + s[n]
  else:
    x.append(s[n])

for n in range(0, len(x)):
  if n == 0:
    phrase = x[n]
  if len(x[n]) > len(phrase):
    phrase = x[n]
print(s_s + phrase)