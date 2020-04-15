from tkinter import *

def save_data():
  file = open("deliveries.txt", "a")
  file.write("Depot:\n")
  file.write("%s\n" % depot.get())
  file.write("Description: \n")
  file.write("%s\n" % description.get())
  file.write("Address:\n")
  file.write("%s\n" % address.get("1.0",END))
  depot.delete(0,END)
  description.delete(0,END)
  address.delete("1.0",END)
  file.close()
  
app = Tk()
app.title('Head-Ex Deliveries')

Label(app, text = "Depot:").pack()
depot = Entry(app)
depot.pack()

Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

Button(app, text = "Save", command = save_data).pack()

app.mainloop()


