from tkinter import filedialog
from tkinter import *

def askDirectory():
    global window
    window.directory =  filedialog.askdirectory()
    print (window.directory)

def click_exitButton():
    exit()

window = Tk()
window.title("VCU Parser")

folderButton = Button(window, text="open folder", command=askDirectory)
folderButton.place(x=500, y=350)

exitButton = Button(window, text="exit", command=click_exitButton)
exitButton.place(x=450, y=350)

window.geometry("600x400")

window.mainloop()

