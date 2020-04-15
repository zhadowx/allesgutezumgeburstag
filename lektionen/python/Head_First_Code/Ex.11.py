line="101;Jonny 'wave-boy' Jones;USA;8.32;Fish;21"
surfer={}
(surfer['id'], surfer['name'], surfer['country'], surfer['average'], surfer['board'], surfer['age'])=line.split(";")
print("ID:           "+ surfer['id'])
print("Name:         "+ surfer['name'])
print("Country:      "+ surfer['country'])
print("Average:      "+ surfer['average'])
print("Board Type:   "+ surfer['board'])
print("Age:          "+ surfer['age'])

