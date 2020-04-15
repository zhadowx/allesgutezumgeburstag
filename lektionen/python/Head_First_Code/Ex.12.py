def find_details(id2find):
	surfers_f=open("surfing_data.csv")
	for each_line in surfers_f:
		surfer={}
		(surfer['id'], surfer['name'], surfer['country'], surfer['average'], surfer['board'], surfer['age'])=each_line.split(";")
		if id2find == int(surfer['id']):
			surfers_f.close()
			return(surfer)
	surfers_f.close()
	return({})
lookup_id=int(input("Enter the id of the surfer: "))
s = find_details(lookup_id)
if s:
	print("ID:           "+ s['id'])
	print("Name:         "+ s['name'])
	print("Country:      "+ s['country'])
	print("Average:      "+ s['average'])
	print("Board Type:   "+ s['board'])
	print("Age:          "+ s['age'])