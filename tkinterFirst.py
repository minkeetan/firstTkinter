from tkinter import filedialog
from tkinter import *

def askDirectory():
    global window
    window.directory =  filedialog.askdirectory()
    folderLabel.config(text=window.directory)
    print (window.directory)

def click_exitButton():
    exit()

window = Tk()
window.title("VCU Parser")

resultPathLabel = Label(window, text = "Results path : ", width = 10) 
resultPathLabel.grid(row = 0, column = 0, pady = 20, padx=10) 

folderLabel = Label(window, width=80, anchor='w', bd=1, relief='sunken') 
folderLabel.grid(row = 0, column = 1, pady = 20) 

folderButton = Button(window, text="open folder", command=askDirectory)
folderButton.grid(row = 0, column = 2, pady = 20, padx=20, ipadx=2)

exitButton = Button(window, text="exit", command=click_exitButton)
exitButton.grid(row = 1, column = 0, sticky = W, padx=10, ipadx=2, pady=300)

window.geometry("800x400")

window.mainloop()

