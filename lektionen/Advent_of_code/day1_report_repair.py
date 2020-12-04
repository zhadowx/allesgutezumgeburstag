lst = []
with open("numbers.txt", "r", encoding ="utf8") as f:
  for line in f:
    lst.append(int(line))

for i in range(len(lst) - 2):
  for j in range(i+1, len(lst) - 1):
    for k in range(j+1, len(lst)):
      if lst[i]+lst[j]+lst[k] == 2020:
        ans = lst[i]*lst[j]*lst[k]
        print(lst[i], lst[j], lst[k])
        break

print(ans)