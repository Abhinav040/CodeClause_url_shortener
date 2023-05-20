from tkinter import *
from tkinter import messagebox
import pyshorteners
import validators

root=Tk()
root.geometry("400x300")
root.title("Url Shortener")

output=StringVar()
link=StringVar()

#storing data from clipboard
cliptext = root.clipboard_get()

def paste():
    link.set(cliptext)

def clearB():
    link.set("")

def short():
    finalUrl=link.get()
    if(validators.url(finalUrl)):
        output1=pyshorteners.Shortener().tinyurl.short(finalUrl)
        output.set(output1)
    else:
        messagebox.showerror('Invalid url','Entered url is invalid, try again..')

def copy():
    res=output.get()
    root.clipboard_append(res)


Label(root, text="Enter Url:", font="Arial 13").grid(row=0, column=0, sticky=W, padx=10, pady=10)
linkbox = Entry(root, textvariable=link, width=60).grid(row=1, column=0, padx=10, pady=10)

pastebutton = Button(root, text='Paste', command=paste, padx=10,bg="magenta").grid(row=2, column=0, sticky=W, padx=10)
clear = Button(root, text='Clear', command=clearB,bg="magenta").grid(row=2, column=0, sticky=E, padx=10)

shortButton = Button(root, text="Shorten...", command=short, padx=30, bg="yellow", fg="black").grid(row=3, column=0, padx=10, pady=10)

Entry(root, textvariable=output, width=60).grid(row=4, column=0, padx=10, pady=10)
copybutton = Button(root, text="Copy", command=copy,bg="green").grid(row=5, column=0, padx=10)


root.mainloop()

