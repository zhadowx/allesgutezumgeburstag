import sqlite3
def find_details(id2find):
	db = sqlite3.connect("surfersDB.sdb")
	db.row_factory = sqlite3.Row 
	cursor = db.cursor()
	cursor.execute("select  * from surfers")
	rows = cursor.fetchall()
	for row in rows:
		if id2find == row['id']:
			cursor.close()
			return(row)
	cursor.close()
	return({})

lookup_id = int(input("Enter the id of the surfer: "))
surfer = find_details(lookup_id)
if surfer:
	print("ID: 		" + str(surfer['id']))
	print("Name: 		" + surfer['name'])
	print("Country: 	" + surfer['country'])
	print("Average: 	" + str(surfer['average']))
	print("Board type: 	" + surfer['board'])
	print("Age: 		" + str(surfer['age']))
