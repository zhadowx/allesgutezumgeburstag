def save_details(nombre, numero, descripcion):
	file = open("clientes.txt", "a")
	file.write("%s   %10d   %s\n" % (nombre, numero, descripcion))
	file.close()
items = ["Paquete 1 Habitación", "Paquete 2 Habitaciones", "Paquete especial", "Otros"]
running = True

while running:
	opcion = 1
	for choice in items:
		print(str(opcion) + ". " + choice)
		opcion = opcion + 1
	print(str(opcion) + ". Salir")
	name = str(input("Nombre del cliente: "))
	numero = int(input("Número de contacto: "))
	choice = int(input("Elija una opcion: "))
	if choice == opcion:
		running = False
	else:
		nombre = input("Nombre del cliente: ")
		numero = int(input("Número de contacto: "))
		save_details(nombre, numero, items[choice-1])