#!/usr/local/bin/python
# coding: utf-8
import tkinter as tk
import tkinter.messagebox as mb
import sqlite3


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        
        self.wordTranslate = tk.StringVar()
        self.englishList = tk.StringVar()
        self.arabicList = tk.StringVar()
        self.createForm()
        self.dbs = self.getDatabaseConnection()
    
    def createForm(self):
        toolbar = tk.Frame(root, bd=1, relief=tk.GROOVE, padx=2, pady=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        txt = tk.Entry(toolbar , width=42, bd=3 ,textvariable=self.wordTranslate)
        txt.pack(side=tk.RIGHT, padx = 4, pady = 1, ipady = 4)

        translate = tk.Button(toolbar,width = 20, text="ترجم", command=self.translateWords)
        translate.pack(side=tk.RIGHT, padx=4, pady = 1)

        exit = tk.Button(toolbar, width = 25,text="اغـــلاق", command=self.master.quit)
        exit.pack(side=tk.RIGHT, padx=4, pady = 1)
        # ===========================================
        contents = tk.Frame(root, bd=1, relief=tk.GROOVE, padx=4, pady=4)
        contents.pack(side=tk.BOTTOM, fill=tk.BOTH)
        # ===========================================
        enList = tk.Listbox(contents, width = 42, height=50, bd=3, listvariable=self.englishList)
        enList.pack(side=tk.LEFT, fill=tk.Y)

        arList = tk.Listbox(contents, width = 42, height=50, bd=3, justify=tk.RIGHT, listvariable=self.arabicList)
        arList.pack(side=tk.RIGHT, fill=tk.Y)
        
    def getDatabaseConnection(self):
        try:
            connect = sqlite3.connect('database.db3')
            return connect
        except sqlite3.Error as err:
            print("Database Error: ", err.args[0])
            return
            
    def translateWords(self):
        results = []
        english = ""
        arabic = ""
        try:
            cursor = self.dbs.cursor()
            cursor.execute("select distinct(english),arabic from trans where english='"+
            self.wordTranslate.get().upper() +"' or arabic='"+
            self.wordTranslate.get().upper() +"' ")
            results = cursor.fetchall()

            for row in results:
                english += "\"" + row[0] + "\"\n"
                arabic  += "\"" + row[1] + "\"\n"
            
            self.englishList.set(english)
            self.arabicList.set(arabic)
        except sqlite3.Error as err:
            print("Database Error: ", err.args[0])
            return

root = tk.Tk()
root.title("القامــــــــــــــــــوس")
root.maxsize(550 , 300)
root.minsize(550 , 300)
root.resizable(False, False)

app = Application(root)
root.mainloop()
