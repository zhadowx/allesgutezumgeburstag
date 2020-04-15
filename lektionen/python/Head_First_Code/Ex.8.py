result_f=open("results.txt")
scores=[]
for line in result_f:	
	(name,score)=line.split()
	scores.append(float(score))
	scores.sort(reverse=True)
result_f.close()

print("The highest score was:")
print(scores[0])
print("The second highest score was:")
print(scores[1])
print("The third highest score was:")
print(scores[2])