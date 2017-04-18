from tkinter import *

mainWindow = Tk()
mainWindow.title("Dictionary")
mainWindow.maxsize(600 , 250)
mainWindow.minsize(600 , 250)
mainWindow.resizable(False, False)

""" ---------------------------- """

topFrame = Frame(mainWindow, bd=1, relief=GROOVE, padx=2, pady=4)
topFrame.pack(side=TOP, fill=X)

value = Entry(topFrame , width=52, bd=3)
value.pack(side=LEFT, padx = 4, pady = 1, ipady = 4)

trans = Button(topFrame, text="Translate ترجم")
trans.pack(side=LEFT, padx=4, pady = 1)

about = Button(topFrame, text="About عن البرنامج")
about.pack(side=LEFT, padx=4, pady = 1)

exit = Button(topFrame, text="Exit خــروج", command=mainWindow.quit)
exit.pack(side=LEFT, padx=4, pady = 1)

""" --------------------------- """

bottomFrame = Frame(mainWindow, bd=1, relief=GROOVE, padx=4, pady=4)
bottomFrame.pack(side=BOTTOM, fill=BOTH)

en = Listbox(bottomFrame, width = 48, height=50, bd=3, relief=SUNKEN)
en.pack(side=LEFT, fill=Y)

ar = Listbox(bottomFrame, width = 48, height=50, bd=3, relief=SUNKEN)
ar.pack(side=RIGHT, fill=Y)

mainWindow.mainloop()

