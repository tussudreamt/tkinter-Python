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

# 27-06*2026

#Frame                  Used to Organnise things on window
frame = tk.Frame(bg="blue", width=90, height=90, borderwidth=5, relief="raised")
frame.pack(padx=50, pady=50)
tk.Label(frame, text="Text inside Frame", bg="blue").pack()
tk.Label(frame, text="Text inside Frame", bg="blue").pack()
tk.Label(frame, text="Text inside Frame", bg="blue").pack()
tk.Label(frame, text="Text inside Frame", bg="blue").pack()
tk.Entry(frame).pack(pady=20)


#LabelFrame             Used to at label on frame border
LabelF = tk.LabelFrame(win, text="Login", font=("Arial", 25, "bold"), bg="cyan", labelanchor="w")
LabelF.pack(side="top")
tk.Label(LabelF, text="yo wassup", bg="yellow").pack()

#PanedWindow            used to create a paned window where we can change size 
PanedWIN = tk.PanedWindow(win)
PanedWIN.pack()
left = tk.LabelFrame(PanedWIN, text="hello", fg="white", bg="black", width=50, height=50)
right = tk.Frame(PanedWIN, bg="red", width=50, height=50)
PanedWIN.add(left)
PanedWIN.add(right)                 #used to add pane
#PanedWIN.forget(left)               #used to remove Pane


#NoteBook                           creates new tab
NoteBook = ttk.Notebook(win)
NoteBook.pack()

tab1 = tk.Frame(NoteBook)
tab2 = tk.Frame(NoteBook)

NoteBook.add(tab1, text="Home")
NoteBook.add(tab2, text="About us")
NoteBook.select(tab2)               #used to select a specific tab when open an page
print(NoteBook.tabs())
NoteBook.pack(expand=True, fill="both", side="top")


labelplace = tk.Label(win, text="Place position")
labelplace.place(relx=0.7, y=99.9)                   #used to locate widget at exact position
                                                                #relx rely (0.0 left or top, 0.5 center, 1.0 right or bottom)

win.mainloop()                      #Always at last to show display
