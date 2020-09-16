s = 'ocoybob'
x = 0
count = 0

while s[x:len(s)].find("bob") != -1:
  x += s[x:len(s)].find("bob") + 2
  count += 1

print("Number of times bob occurs is: " + str(count))
