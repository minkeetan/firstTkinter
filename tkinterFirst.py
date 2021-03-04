from tkinter import filedialog
from tkinter import *

def askDirectory():
    global window
    window.directory =  filedialog.askdirectory()
    print (window.directory)

window = Tk()
window.title("VCU Parser")

B = Button(window, text="open folder", command=askDirectory)

B.pack()
window.mainloop()

