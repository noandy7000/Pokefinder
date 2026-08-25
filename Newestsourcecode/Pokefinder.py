## MADE BY NOANDY7000 :3
## DONT FUCKING JUDGE MY IMPORTS!!!
from time import sleep as wait
## I forgot why i importet it but I might as well leave it
import os as os
from pathlib import Path as path
import tkinter as tk
from tkinter import messagebox as msgbox
import customtkinter as ctk
from PIL import Image as img, ImageTk as imgtk
## Here I define all the Filepaths for easier exporting
filepathEX = path(__file__).resolve().parent / "Database" / "EXCards.txt"
filepathMEGA = path(__file__).resolve().parent / "Database" / "MEGACards.txt"
filepathFONT = path(__file__).resolve().parent / "Database" / "FONT.txt"
## Here I define the Contents of the Files
with open(filepathEX, "r") as f:
    EXnumbers = f.read()
with open(filepathMEGA, "r") as f:
    MEGAnumbers = f.read()
with open(filepathFONT, "r") as f:
    FONT = f.read()
## This is the GUI config (And everything else)
class GUI:
    def __init__(self):
        ##Main Window
        self.window = tk.Tk()
        self.window.title("PokeFinder by Noandy7000")

        self.label = tk.Label(self.window,
                              text="PokeFinder", font=((FONT), 50))
        self.label.pack(padx=10, pady=10)
        ## Menubar (This is copy and pasted into all Windows)
        self.menubar = tk.Menu(self.window)  
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close All", command=self.onclose)
        self.menubar.add_cascade(menu= self.filemenu, label="Close")
        self.window.config(menu=self.menubar)
        ## Creating the Columns for the Buttons of the Main Window
        self.frame = tk.Frame(self.window)
        for i in range(8):
            self.frame.columnconfigure(i, weight=1)
        ## Creating the Main Menu Buttons
        button1 = tk.Button(self.frame, text="1. Find the page of an Index Number",
                             font=((FONT), 18), command=self.inputwindowconfig)
        button1.grid(row=0, column=0, sticky="we")
        button2 = tk.Button(self.frame, text="2. Mark a Pokemon as EX",
                             font=((FONT), 18), command=self.markasex)
        button2.grid(row=1, column=0, sticky="we")
        button3 = tk.Button(self.frame, text="3. Read which Index Numbers are marked as EX Cards",
                             font=((FONT), 18), command=self.readallex)
        button3.grid(row=2, column=0, sticky="we")
        button4 = tk.Button(self.frame, text="4. Reset all EX marked Cards",
                             font=((FONT), 18), command=self.resetallex)
        button4.grid(row=3, column=0, sticky="we")
        button5 = tk.Button(self.frame, text="5. Mark a Pokemon as Mega",
                             font=((FONT), 18), command=self.markasmega)
        button5.grid(row=4, column=0, sticky="we")
        button6 = tk.Button(self.frame, text="6. Read which Index Numbers are marked as Mega",
                             font=((FONT), 18), command=self.readallmega)
        button6.grid(row=5, column=0, sticky="we")

        button7 = tk.Button(self.frame, text="7. Reset all MEGA marked Cards",
                             font=((FONT), 18), command=self.resetallmega)
        button7.grid(row=6, column=0, sticky="we")
        ##Some more Labels
        self.label2 = tk.Label(self.frame, text="If you want to customize the marked Numbers further: simply go into the Database Folder and edit the .txt files",
                                font=((FONT), 18))
        self.label2.grid(row=7, column=0, sticky="we")
        self.frame.pack(padx=20, pady=50, fill='x')
        self.window.mainloop()
        ## Creating the Inputwindow
    def inputwindowconfig(self):
        self.inputwindow = tk.Toplevel(self.window)
        self.inputwindow.geometry("400x200")
        self.inputwindow.title("Input Index Number of the Pokemon you want the location of")
        self.menubar = tk.Menu(self.inputwindow)  
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.onclose)
        self.menubar.add_cascade(menu= self.filemenu, label="Close")
        self.inputwindow.config(menu=self.menubar)
        ## Here I Create the UI of the Input Window and make it so you can export the Input of self.Indexnumerinput
        self.inputwindowchecker = tk.StringVar()
        self.Indexnumberinput = tk.Entry(self.inputwindow,
                                          font=((FONT), 18), textvariable= self.inputwindowchecker)
        self.confirmbutton1 = tk.Button(self.inputwindow, text="Confirm Input",
                                         font=((FONT), 18), command=self.doutputwindow)
        self.Indexnumberinput.pack(padx=10, pady=10)
        self.confirmbutton1.pack(pady=20, fill="x")
        self.inputwindow.mainloop()
        ## The Function that Controls the Quit Menu in the Menubar
    def onclose(self):
        if msgbox.askyesno(title="Quit?", message="Close the Programm?"):
            self.window.destroy()
        ## The output Creator
    def doutputwindow(self):
        pn = self.inputwindowchecker.get()
        ## Checks if the Input is a Int and shows and Error window if not
        try:           
            pn = int(pn)
        except ValueError:
            msgbox.showwarning(title="Output", message="Invalid Input")
            self.inputwindow.destroy()
            return
        ## Checks if the Input is empty and shows and Error window if not
        if pn == "":
            msgbox.showwarning(title="Output", message="Please enter a number")
            return
        pn = int(pn)
        ## Checks if the Input is in Range and shows and Error window if not
        if pn > 1025:
            msgbox.showwarning(title="Output", message="Thats not in the Pokedex")
            self.inputwindow.destroy()
            return
        ## Calculates the Page
        else:
            pns = pn // 9
            pns = pns / 2
        ## Redefines the Content of EXnumbers and MEGAnumber so you don't have to restart for newly marked cards to appear in the Search
            with open(filepathEX, "r") as f:
                EXnumbers = f.read()
            with open(filepathMEGA, "r") as f:
                MEGAnumbers = f.read()
                ## Defines the Functions so the final Message is empty if undefined and doesn't put out an error
            abc = ""
            abe = ""
            abm = ""
            ## Checks if the Card is on the front or back of the Page
            if str(pns).endswith(".5"):
                abc = "(on the backside)"
                pns = pns // 1
                pns += 1
                ## Defines the Functions if the Number is marked as any
            if f"-{pn}-" in EXnumbers:
                abe = "and is an EX Card"
            if f"-{pn}-" in MEGAnumbers:
                abm = "and is an MEGA Card "
                ## Prints the Final Output and leaves non defined Functions empty
            msgbox.showinfo(title="Output",message=f"The Pokemon you're looking for is on page {int(pns)} {abc} {abe} {abm}")
            self.inputwindow.destroy()
        ## Now we get into the EX marking Menus
    def markasex(self):
        ## Creates the EX marker Window (copy of Input Window)
        self.exmarkerwindow = tk.Toplevel(self.window)
        self.exmarkerwindow.geometry("400x200")
        self.exmarkerwindow.title("Input Index Number of the Pokemon you want the location of")
        self.menubar = tk.Menu(self.exmarkerwindow)  
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.onclose)
        self.menubar.add_cascade(menu= self.filemenu, label="Close")
        self.exmarkerwindow.config(menu=self.menubar)  
        ## Creates the GUI for the Inputwindow and makes it so you can export the Input of self.exmarkerinput 
        self.exmarkerwindowchecker = tk.StringVar()
        self.exmarkerinput = tk.Entry(self.exmarkerwindow,
                                       font=((FONT), 18), textvariable=self.exmarkerwindowchecker)
        self.confirmbutton2 = tk.Button(self.exmarkerwindow, text="Confirm Input",
                                         font=((FONT), 18), command=self.exoutputwindow)
        self.exmarkerinput.pack()
        self.confirmbutton2.pack(pady=20, fill="x")
        ## This is the EX output window that checks for all errors and then Display succes
    def exoutputwindow(self):
        ## Defines the Input as "inpute"
        inpute = self.exmarkerwindowchecker.get()
        ## Checks if the Input is an Int and shows and Error window if not
        try:
            inpute = int(inpute)
            pass
        except ValueError:
            msgbox.showwarningq(title="Error", message="Invalid Input")
            self.exmarkerwindow.destroy()
            return
                ## Checks if the Input is empty and shows and Error window if not
        if inpute == "":
            msgbox.showwarning(title="Output", message="Please enter a number")
            return
        ## Redefines the File Contents and Checks if a Index Number is already marked and shows and Error window if not
        with open(filepathEX, "r") as f:
            EXnumbers = f.read()
        if str(inpute) in EXnumbers:
            msgbox.showwarning(title="Error", message="Is already marked. If you want to remove it Edit the txt File")
            return
        ## Writes the Data into the .txt and Displays the Success Message
        with open(filepathEX, "a") as f:
            f.write(f"-{inpute}-")
        msgbox.showinfo(title="success", message=f"{inpute} is now marked as an EX Card")
        self.exmarkerwindow.destroy()
        ## The Def for the Display of all cards marked as EX
    def readallex(self):
        ## Redefines the File contents and Displays them
        with open(filepathEX, "r") as f:
            EXnumbers = f.read()
        msgbox.showinfo(title="info", message=(EXnumbers))
        ## The def for resetting all marked Cards
    def resetallex(slate):
         ## Writes Nothing into the .txt  and shows the Success Message
         with open(filepathEX, "w") as f:
            f.write("")
            msgbox.showinfo(title="info", message="Reset all EX marked Cards")
            ## Now we get into the MEGA marking Menus
    def markasmega(self):
        ## Creates the Mega marker Input Window
        self.megamarkerwindow = tk.Toplevel(self.window)
        self.megamarkerwindow.geometry("400x200")
        self.megamarkerwindow.title("Input Index Number of the Pokemon you want the location of")
        self.menubar = tk.Menu(self.megamarkerwindow)  
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.onclose)
        self.menubar.add_cascade(menu= self.filemenu, label="Close")
        self.megamarkerwindow.config(menu=self.menubar)  
        ## Creates the GUI and makes it so the Input can be exported      
        self.megamarkerwindowchecker = tk.StringVar()
        self.megamarkerinput = tk.Entry(self.megamarkerwindow,
                                         font=((FONT), 18), textvariable=self.megamarkerwindowchecker)
        self.confirmbutton3 = tk.Button(self.megamarkerwindow, text="Confirm Input",
                                         font=((FONT), 18), command=self.megaoutputwindow)
        self.megamarkerinput.pack()
        self.confirmbutton3.pack(pady=20, fill="x")
        ## The def for the Outputwindow
    def megaoutputwindow(self):
        ## Defines the Input as "inputs"
        inputs = self.megamarkerwindowchecker.get()
        ## Checks if the Input is a Number
        try:
            inputs = int(inputs)
            pass
        except ValueError:
            msgbox.showwarning(title="Error", message="Invalid Input")
            self.megamarkerwindow.destroy()
            return
                ## Checks if the Input is empty and shows and Error window if not
        if inputs == "":
            msgbox.showwarning(title="Output", message="Please enter a number")
            return
        ## Redefines the File Content and checks if its already marked and shows and Error window if not showwarning
        with open(filepathMEGA, "r") as f:
            MEGAnumbers = f.read()
        if str(inputs) in MEGAnumbers:
            msgbox.showwarning(title="Error", message="Is already marked. If you want to remove it Edit the txt File") 
            return
        ## Marks the Input and shows the Success Window
        with open(filepathMEGA, "a") as f:
            f.write(f"-{inputs}-")
        msgbox.showinfo(title="Success", message=f"{inputs} is now marked as MEGA")
        self.megamarkerwindow.destroy()
        ## The def for Reading all marked Cards
    def readallmega(self):
        ## Redefines the Content of the Files and Displays them
        with open(filepathMEGA, "r") as f:
            MEGAnumbers = f.read()
        msgbox.showinfo(title="info", message=(MEGAnumbers))
        ## The def for resetting all marked cards
    def resetallmega(self):
        ## Writes Nothing into the .txt and shows the Success message
        with open(filepathMEGA, "w") as f:
            f.write("")
            msgbox.showinfo(title="info", message="Reset all MEGA marked Cards")
## Starts the GUI
GUI()
