from tkinter import filedialog
from tkinter import *

def askDirectory():
    global window
    window.directory =  filedialog.askdirectory()
    folderLabel.delete(1.0, END)
    folderLabel.insert(1.0, window.directory)
    # folderLabel.configure(state="disabled")
    print (window.directory)

def click_exitButton():
    exit()

window = Tk()
window.title("VCU Parser")

resultPathLabel = Label(window, text = "Results path : ", width = 10) 
resultPathLabel.grid(row = 0, column = 0, pady = 20, padx=10) 

folderLabel = Text(window, height=1, width=75)
folderLabel.insert(1.0, "Please choose a folder that contain Logs")
folderLabel.grid(row = 0, column = 1, pady = 20) 

folderButton = Button(window, text="open folder", command=askDirectory)
folderButton.grid(row = 0, column = 2, pady = 20, padx=5, ipadx=2)

exitButton = Button(window, text="exit", command=click_exitButton)
exitButton.grid(row = 1, column = 0, sticky = W, padx=10, ipadx=2, pady=300)


window.geometry("800x400")

window.mainloop()

