result_f=open("results.txt")
#surfers={}
scores=[]
names=[]
for line in result_f:	
	(name,score)=line.split()
	scores.append(float(score))
	scores.sort(reverse=True)
result_f.close()
messages= ["The highest score was: ", "The second highest score was: ", "The third highest score was: "]
# print("The highest score was: ",end='')
# print(scores[0])
# print("The second highest score was:")
# print(scores[1])
# print("The third highest score was:")
# print(scores[2])

for i in range(len(messages)):
	print(messages[i]+str(scores[i]))