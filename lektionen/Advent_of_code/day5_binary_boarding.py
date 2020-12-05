boarding_passes = []
with open("boarding_passes.txt", "r", encoding = "utf8") as f:
  for line in f:
    boarding_passes.append(line.strip("\n"))
def pass_id(p):
  lower = 0
  upper = 127
  ml = (lower + upper) // 2
  mu = (lower + upper) // 2 + 1
  
  lower2 = 0
  upper2 = 7
  ml2 = (lower2 + upper2) // 2
  mu2 = (lower2 + upper2) // 2 + 1

  for i in range(10):
    if p[i] == "F":
      if i == 6:
        row = ml
      upper = ml 
      ml = (lower + upper) // 2
      mu = (lower + upper) // 2 + 1
     
    elif p[i] == "B":
      if i == 6:
        row = mu
      lower = mu
      ml = (lower + upper) // 2
      mu = (lower + upper) // 2 + 1
      
    elif p[i] == "L":
      if i == 9:
        column = ml2
      upper2 = ml2  
      ml2 = (lower2 + upper2) // 2
      mu2 = (lower2 + upper2) // 2 + 1
      
    elif p[i] == "R":
      if i == 9:
        column = mu2
      lower2 = mu2
      ml2 = (lower2 + upper2) // 2
      mu2 = (lower2 + upper2) // 2 + 1  
  return row*8+column
highest = 0
pass_ids = []
for e in boarding_passes:
  pass_ids.append(pass_id(e))
  if pass_id(e) > highest:
    highest =  pass_id(e)
missin_ids = []
for i in range(829):
  if i not in pass_ids:
    missin_ids.append(i)
print(highest, missin_ids)