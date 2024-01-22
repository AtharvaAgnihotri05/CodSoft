from tkinter import *
from tkinter.ttk import *
def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                scvalue.set("Error")
                screen.update()
                

        scvalue.set(value)
        screen.update()        
    elif text == "C":
        scvalue.set("")
        screen.update
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root_window = Tk()
root_window.geometry("450x400")
root_window.title("Calculator")
p1 = PhotoImage(file="calculator.png")
root_window.iconphoto(False,p1)
scvalue = StringVar()
scvalue.set("")
screen = Entry(root_window,textvar=scvalue,font="Arial")
screen.pack(fill=X,ipadx=20,pady=15,padx=15)

f = Frame(root_window)
b = Button(f,text="%")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
b = Button(f,text="CE")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
b = Button(f,text="C")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
b = Button(f,text="/")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root_window)
b = Button(f,text="7")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
b = Button(f,text="8")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
b = Button(f,text="9")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
b = Button(f,text="*")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root_window)
b = Button(f,text="4")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
b = Button(f,text="5")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
b = Button(f,text="6")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
b = Button(f,text="-")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root_window)
b = Button(f,text="1")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
b = Button(f,text="2")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
b = Button(f,text="3")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
b = Button(f,text="+")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root_window)
b = Button(f,text="+/-")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
b = Button(f,text="0")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
b = Button(f,text=".")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
b = Button(f,text="=")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>", click)
f.pack()

mainloop()