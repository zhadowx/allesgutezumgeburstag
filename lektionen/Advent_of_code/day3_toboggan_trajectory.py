lines = []

with open("trajectory_1.txt", "r", encoding = "utf8") as f:
  for line in f:
    lines.append(73*line.strip("\n"))

def calc_trees(start, mult, step):
  trees = 0
  for i in range(start, 323, step):
    if lines[i][mult*i] == "#":
      trees+=1
  return trees

t1 = calc_trees(1, 1, 1)
t2 = calc_trees(1, 3, 1)
t3 = calc_trees(1, 5, 1)
t4 = calc_trees(1, 7, 1)

t5 = 0
j = 1
for i in range(2, 323, 2):
  if lines[i][j] == "#":
    t5+=1
  j+=1

print(t1, t2, t3, t4, t5, t1*t2*t3*t4*t5)