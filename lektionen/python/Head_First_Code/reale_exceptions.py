from tkinter import *
import tkinter.messagebox
def save_data():
  try:
    file = open("deliveries.txt", "a")
    file.write("Depot:\n")
    file.write("%s\n" % depot.get())
    file.write("Description: \n")
    file.write("%s\n" % description.get())
    file.write("Address:\n")
    file.write("%s\n" % address.get("1.0",END))
    depot.set("---------")
    description.delete(0,END)
    address.delete("1.0",END)
    file.close()
  except Exception as ex:
    tkinter.messagebox.showerror("Error!", "Can't write to the file\n %s" % ex)


def read_depots(file2):
  depots = []
  depots_f = open(file2)
  for line in depots_f:
    depots.append(line.rstrip())
  return depots  


app = Tk()
app.title('Head-Ex Deliveries')

Label(app, text = "Depot:").pack()
depot = StringVar()
depot.set("---------")

options = read_depots("depots.txt")
OptionMenu(app, depot, *options).pack()

Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

Button(app, text = "Save", command = save_data).pack()

app.mainloop()


