from tkinter import *
import tkinter.messagebox as mb
import sqlite3

def aboutApp():
    mb.showinfo("About", "Dictionary 1.0 2017")

def connectDB():
    try:
        myconnection = sqlite3.connect('sqlite_test.db3')
        return myconnection
    except sqlite3.Error as e:
        print("Database Error: ", e.args[0])
        return

def translate():
    resultset = []
    enText = ""
    arText = ""
    try:
        cursor = conn.cursor()
        cursor.execute("select * from results limit 100")
        resultset = cursor.fetchall()
        for row in resultset:
            enText += " " + row[1] 
            arText += " " + row[1] 
        
        enValues.set(enText)
        arValues.set(arText)
    except sqlite3.Error as e:
        print("Database Error: ", e.args[0])
        return

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

trans = Button(topFrame, text="Translate ترجم", command=translate)
trans.pack(side=LEFT, padx=4, pady = 1)

about = Button(topFrame, text="About عن البرنامج", command=aboutApp)
about.pack(side=LEFT, padx=4, pady = 1)

exit = Button(topFrame, text="Exit خــروج", command=mainWindow.quit)
exit.pack(side=LEFT, padx=4, pady = 1)

""" --------------------------- """

bottomFrame = Frame(mainWindow, bd=1, relief=GROOVE, padx=4, pady=4)
bottomFrame.pack(side=BOTTOM, fill=BOTH)

""" --------------------------- """
enValues = StringVar()
en = Listbox(bottomFrame, width = 48, height=50, bd=3, listvariable=enValues)
en.pack(side=LEFT, fill=Y)

enValues.set("test test2 test3")

arValues = StringVar()
ar = Listbox(bottomFrame, width = 48, height=50, bd=3, justify=RIGHT, listvariable=arValues)
ar.pack(side=RIGHT, fill=Y)

arValues.set("محمد أحمد علي")

enValues.set("\"test test2\" test3")

""" --------------------------- """

conn = connectDB()

mainWindow.mainloop()

