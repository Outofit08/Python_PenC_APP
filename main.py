from tkinter import *
import webbrowser


def doNothing():
    print("does nothing")

def quit():
    global  Mwindow
    Mwindow.destroy()

Mwindow = Tk() #is the blank window. -BDH
Mwindow.wm_title("RITAccess_App") # this will give the application the RIta name
Mwindow.wm_iconbitmap("RITAccess.ico") # this sets the application Icon to RIta

#******* Menus *******
menu = Menu(Mwindow)
Mwindow.config(menu=menu) # puts at top and preps for doing drop down stuff
submenu = Menu(menu) # drop down menu
menu.add_cascade(label="File", menu=submenu) #names the submenu
submenu.add_command(label="Load", command=doNothing) # a button in submenu
submenu.add_command(label="Save", command=doNothing)
submenu.add_separator() # creates a seperate line in the drop down menu
submenu.add_command(label="EXIT", command=quit)


editMenu= Menu(menu) # sets edit menu
menu.add_cascade(label= "Edit", menu=editMenu)
editMenu.add_command(label="REDO", command=doNothing)
#******* Frames ********
topFrame = Frame(Mwindow)  # top frame for app
topFrame.pack(side=TOP)
bottomFrame = Frame(Mwindow) # bottom frame for app
bottomFrame.pack(side=BOTTOM)

#******* Buttons *******

def Pencilcode(event):  # THis will launch pencil code in webbrowser
    webbrowser.open_new(r"https://pencilcode.net/edit/first")

button_1 = Button(topFrame,text="Open PencilCode", bg="green") # open pencil code button
button_1.bind("<Button-1>", Pencilcode)  # runs the function to launch pencil code site
button_1.grid(row=0)

button_exit = Button(bottomFrame, text="Quit", bg="red" ,command=quit) # THis button exits the program
#button_exit.bind("<Button-1>", command=quit)  # ends program

button_exit.grid(row=1, column=1)



Mwindow.mainloop() # keeps the window open for infinite loop -BDH