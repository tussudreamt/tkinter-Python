#29-06-2026
#Layout Management

#pack()
#Labelpack = tk.Label(win, text="textOfPack", bg="blue")
#abelpack.pack()

                                                    #sticky= specify specific position in grid cell
tk.Label(win, text="Name").grid(row=2, column=2, sticky="nsew")     #layout using rows and columns
#tk.Entry(win).grid(row=1, column=2)                 #recomment to use grid and pack in sepparate frame
                                #row and colm bot strat from 0
