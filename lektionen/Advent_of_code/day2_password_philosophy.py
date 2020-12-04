rules = []
passwords = []
with open("password_list.txt", "r", encoding ="utf8") as f:
  for line in f:
    (rule, password) = line.split(": ")
    rules.append(rule)
    passwords.append(password)

total = 0
for i in range(len(rules)):
  if len(rules[i]) == 5:
    if passwords[i].count(rules[i][4]) >= int(rules[i][0]) and \
    passwords[i].count(rules[i][4]) <= int (rules[i][2]):
      total+=1
  elif len(rules[i]) == 6:
    if passwords[i].count(rules[i][5]) >= int(rules[i][0]) and \
    passwords[i].count(rules[i][5]) <= int (rules[i][2:4]):
      total+=1
  else:
    if passwords[i].count(rules[i][6]) >= int(rules[i][0:2]) and \
    passwords[i].count(rules[i][6]) <= int (rules[i][3:5]):
      total+=1

total2 = 0
for i in range(len(rules)):
  if len(rules[i]) == 5:
    if rules[i][4] == passwords[i][int(rules[i][0])-1] and not\
    rules[i][4] == passwords[i][int(rules[i][2])-1] or \
    rules[i][4] == passwords[i][int(rules[i][2])-1] and not \
    rules[i][4] == passwords[i][int(rules[i][0])-1]:
      total2+=1
  elif len(rules[i]) == 6:
    if rules[i][5] == passwords[i][int(rules[i][0])-1] and not \
    rules[i][5] == passwords[i][int(rules[i][2:4])-1] or \
    rules[i][5] == passwords[i][int(rules[i][2:4])-1] and not \
    rules[i][5] == passwords[i][int(rules[i][0])-1]:
      total2+=1
  else:
    if rules[i][6] == passwords[i][int(rules[i][0:2])-1] and not \
    rules[i][6] == passwords[i][int(rules[i][3:5])-1] or \
    rules[i][6] == passwords[i][int(rules[i][3:5])-1] and not \
    rules[i][6] == passwords[i][int(rules[i][0:2])-1]:
      total2+=1

print(total, total2)