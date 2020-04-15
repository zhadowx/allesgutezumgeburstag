
highest_score =0
scores = []
result_f = open("results.txt")
for line in result_f:
	(name, score) = line.split()
	scores.append(float(score))
result_f.close()
scores.sort(reverse = True)
print("The highest score was:")
print(scores[0])
print("The second highest score was:")
print(scores[1])
print("The third highest score was:")
print(scores[2])