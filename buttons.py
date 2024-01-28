from tkinter import*
window=Tk()
window.geometry("500x500")

lbl1=Label(window,text="First Number",font=("calibri",10))
lbl1.pack()

text1=Text(window,height=2,width=20,font=("calibri",10))
text1.pack()

lbl2=Label(window,text="Second Number",font=("calibri",10))
lbl2.pack()

text2=Text(window,height=2,width=20,font=("calibri",10))
text2.pack()

# Output label
output = Label(window, text="Output", font=("calibri",10))
output.pack()

output=Text(window,height=2,width=20,font=("calibri",10))
output.pack()

def add():
    x=int(text1.get("1.0","end-1c"))
    y=int(text2.get("1.0","end-1c"))
    result=x+y
    output.delete('1.0', END)
    output.insert(END, str(result))

def substract():
    x=int(text1.get("1.0","end-1c"))
    y=int(text2.get("1.0","end-1c"))
    result=x-y
    output.delete('1.0', END)
    output.insert(END, str(result))

def multiply():
    x=int(text1.get("1.0","end-1c"))
    y=int(text2.get("1.0","end-1c"))
    result=x*y
    output.delete('1.0', END)
    output.insert(END, str(result))

def devide():
    x=int(text1.get("1.0","end-1c"))
    y=int(text2.get("1.0","end-1c"))
    result=x/y
    output.delete('1.0', END)
    output.insert(END, str(result))

btn1=Button(window,command=add,text="Add",font=("calibri",10))
btn1.pack()

btn1=Button(window,command=substract,text="Substract",font=("calibri",10))
btn1.pack()

btn1=Button(window,command=multiply,text="Multiply",font=("calibri",10))
btn1.pack()

btn1=Button(window,command=devide,text="Devide",font=("calibri",10))
btn1.pack()

window.mainloop()
