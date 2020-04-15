import sqlite3

def find_details(id2find):
	db = sqlite3.connect("surfersDB.sdb")
	db.row_factory = sqlite3.Row 
	cursor = db.cursor()
	cursor.execute("select  * from surfers")
	rows = cursor.fetchall()
	for row in rows:
		# print(row.keys())
		if row['id']==id2find:
			print("id is: "+str(row['id']))
			surfer={}
			surfer['id']=str(row['id'])
			surfer['name'] = row['name']
			surfer['country']=row['country']
			surfer['average']=str(row['average'])
			surfer['board']=row['board']
			surfer['age']=str(row['age'])
			cursor.close()
			return(surfer)
	cursor.close()
	return({})

lookup_id=int(input("Enter the id of the surfer: "))
s = find_details(lookup_id)
if s:
	print("ID:           "+ str(s['id']))
	print("Name:         "+ s['name'])
	print("Country:      "+ s['country'])
	print("Average:      "+ str(s['average']))
	print("Board Type:   "+ s['board'])
	print("Age:          "+ str(s['age']))