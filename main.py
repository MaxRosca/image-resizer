import tkinter
import PIL
from tkinter import *
from tkinter.filedialog import *
from PIL import Image

img = ""
newWidth = 0
newHeight = 0

def resize():
    global newWidth, newHeight, img
    img2 = ""
    extension = ""
    newWidth = widthEntry.get()
    newHeight = heightEntry.get()
    im = Image.open(img)
    im = im.resize((int(newWidth), int(newHeight)), Image.ANTIALIAS)
    i = len(img) - 1
    splitedImg = list(img)
    while splitedImg[i] != ".":
        extension = extension + splitedImg[i]
        splitedImg[i] = ""
        i -= 1
    splitedImg[i] = ""
    extension += "."
    extension = list(extension)
    extension.reverse()
    extension = "".join(extension)
    img2 = "".join(splitedImg)
    outfile = img2 + "_"  + str(newWidth) + "_" + str(newHeight) + extension
    im.save(outfile)

def openFile():
    global img
    file =  askopenfilename(initialdir = "/",title = "Select file",
                            filetypes = (("Jpg files", "*.jpg"),
                            ("All files","*.*")))
    img = file

root = Tk()

widthEntry = Entry(root)
heightEntry = Entry(root)

selectFileButton = Button(root, text="Select File", command=openFile)
resizeButton = Button(root, text="Resize", command=resize)

widthEntry.pack()
heightEntry.pack()
selectFileButton.pack()
resizeButton.pack()

root.mainloop()
