import tkinter as tk
from tkinter import ttk
#25-06-2026

win = tk.Tk()                       #create object
win.title("Tkinter window")         #windows Title
win.geometry("800x800+600+10")      #window size    (widthxheight+Xpos+Ypos)
#win.iconbitmap("crown.ico")        #windows Icon

label = tk.Label(win, text="Hello World", font=("Arial", 25, "bold"), fg="red", bg="yellow")
label.pack(side="left")                 #To print or show text

def greet():
    text = entry.get()
    print("Hello this function is used to execute 'command' attribute")
varButton = tk.Button(win, text="click Me!", fg="red", bg="cyan", command=greet)
varButton.pack()                    #pack() specifies when the widgets come accordingly                     


entry = tk.Entry(win, width="50", show="$", justify="right")
def entrygreet():
    print(entry.get())              #entry.get() to get input

entry.pack()
buttonEntry = tk.Button(text="Enter Button", command=entrygreet)
buttonEntry.pack()

textbox = tk.Text(win, width="25", height="5")      #Text is used to get multiple line input
textbox.pack()

def getcontent():
    print(textbox.get("1.5", tk.END))
button2 = tk.Button(text="Getcontent!", command=getcontent)
button2.pack()

MSGbox = tk.Message(win, text="Python executes code from top to bottom. You must instantiate your widgets before referencing them in layouts or functions.", font=("Arial TM", 15, "italic"), width="250", fg="black", bg="grey", )
MSGbox.pack()

#26-06-2026

#Checkbutton
checkValue = ["Python", "java", "C++"]                      #For multiple checkBox Automatically
checkbox_vars = {}
for item in checkValue:
    # Each checkbox gets its own separate variable
    var = tk.BooleanVar(value=False)
    checkbox_vars[item] = var
    cb = tk.Checkbutton(win, text=item, variable=var)
    cb.pack()


def showStatus():
    print("current status :", strin_var.get())
strin_var = tk.StringVar(win, value="No")
checbutton = tk.Checkbutton(win, text="hello hiii", variable=strin_var, onvalue="Yes", offvalue="No", command=showStatus)        #Multiple checkbox manually
checbutton.pack()

#Radiobutton
def show_gender():
    print("Gender: ", gender.get())
labelGender = tk.Label(text="Select Gender").pack()
gender = tk.StringVar(value="idk")
tk.Radiobutton(win, text="Female", variable=gender, value="Female", command=show_gender).pack()
tk.Radiobutton(win, text="Male", variable=gender, value="Male", command=show_gender).pack()
tk.Radiobutton(win, text="Others", variable=gender, value="Others", command=show_gender).pack()

#Listbox
listbox = tk.Listbox(win)
listbox.insert(1, "Python")          #Index start from 0
listbox.insert(2, "Java")            #Inser item in listBox
listbox.insert(3, "C++")
listbox.insert(4, "hello")
listbox.pack()
listbox.delete(3)                    #Delete accn to index
ind = listbox.curselection()         #Retrieve the item currently selected by user inside listbox
if ind:
    print(listbox.get(ind[0]))

#Spinbox
def spin_Value():
    print("selected Number: ", spinBox.get())
spinBox = tk.Spinbox(win, from_=1, to=10, increment=1, command=spin_Value, width=50)   #Increment only 1 value at a time
spinBox.pack()

#Scale
scaleVal = tk.Scale(win, from_=0, to=100, orient="horizontal", length=500)
scaleVal.pack()                       #Volume button DRag select

#Combobox      ttk                     #Dropdown box where user select one option
combo = ttk.Combobox(win)
combo["values"] = ("Python", "Java", "Javascript", "Bootstrap")
combo.current(0)                         #Automatically select value at 0
combo.set("hello")                     #set the combobox value to mention value
combo.pack()



win.mainloop()                      #Always at last to show display
