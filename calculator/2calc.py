from tkinter import*
root =Tk()
root.title("Simple Calculator")
root["background"]="#1f4068"
e=Entry(root,width=45, borderwidth=10,font=("Times New Roman","20"))
e.grid(row=0,column=0, columnspan=3, padx=10,pady=10,ipady=15)
def button_click(number):
    currentnumber = e.get()
    e.delete(0,END)
    e.insert(0,str(currentnumber) + str(number))
def button_clear():
    e.delete(0, END)
def buttton_add():
    first_number = e.get()
    global f_num
    global math
    math ="addition"
    f_num = int(first_number)
    e.delete(0,END)
def button_equal():
    second_number=e.get()
    e.delete(0,END)

    if math=="addition":
        e.insert(0,f_num + int(second_number))
    if math=="subraction":
        e.insert(0, f_num - int(second_number))
    if math=="multiplication":
        e.insert(0, f_num * int(second_number))
    if math=="division":
        e.insert(0, f_num / int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subraction"
    f_num = int(first_number)
    e.delete(0, END)
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
#Define buttons
button_1= Button(root,text="1",padx=50,pady=20,command=lambda:button_click(1),highlightbackground="#162447",fg="white",font=("Times New Roman","30"))
button_2= Button(root,text="2",padx=50,pady=20,command=lambda:button_click(2),highlightbackground="#162447",fg="white",font=("Times New Roman","30"))
button_3= Button(root,text="3",padx=50,pady=20,command=lambda:button_click(3),highlightbackground="#162447",fg="white",font=("Times New Roman","30"))
button_4= Button(root,text="4",padx=50,pady=20,command=lambda:button_click(4),highlightbackground="#162447",fg="white",font=("Times New Roman","30"))
button_5= Button(root,text="5",padx=50,pady=20,command=lambda:button_click(5),highlightbackground="#162447",fg="white",font=("Times New Roman","30"))
button_6= Button(root,text="6",padx=50,pady=20,command=lambda:button_click(6),highlightbackground="#162447",fg="white",font=("Times New Roman","30"))
button_7= Button(root,text="7",padx=50,pady=20,command=lambda:button_click(7),highlightbackground="#162447",fg="white",font=("Times New Roman","30"))
button_8= Button(root,text="8",padx=50,pady=20,command=lambda:button_click(8),highlightbackground="#162447",fg="white",font=("Times New Roman","30"))
button_9= Button(root,text="9",padx=50,pady=20,command=lambda:button_click(9),highlightbackground="#162447",fg="white",font=("Times New Roman","30"))
button_0= Button(root,text="0",padx=50,pady=20,command=lambda:button_click(0),highlightbackground="#162447",fg="white",font=("Times New Roman","30"))
button_add=Button(root,text="+",padx=50,pady=20,command=buttton_add,highlightbackground="#162447",fg="white",font=("Times New Roman","30"))
button_equal=Button(root,text="=",padx=130,pady=20,command=button_equal,highlightbackground="#162447",fg="white",font=("Times New Roman","30"))
button_clear=Button(root,text="clear",padx=110,pady=20,command=button_clear,highlightbackground="#162447",fg="white",font=("Times New Roman","30"))
button_subtract=Button(root,text="-",padx=51,pady=20,command=button_subtract,highlightbackground="#162447",fg="white",font=("Times New Roman","30"))
button_multiply=Button(root,text="*",padx=51,pady=20,command=button_multiply,highlightbackground="#162447",fg="white",font=("Times New Roman","30"))
button_divide=Button(root,text="/",padx=52,pady=20,command=button_divide,highlightbackground="#162447",fg="white",font=("Times New Roman","30"))
    #Put Buttons on th screen
button_1.grid(row=3,column=0,padx=10,pady=10)
button_2.grid(row=3,column=1,padx=10,pady=10)
button_3.grid(row=3,column=2,padx=10,pady=10)

button_4.grid(row=2,column=0,padx=10,pady=10)
button_5.grid(row=2,column=1,padx=10,pady=10)
button_6.grid(row=2,column=2,padx=10,pady=10)

button_7.grid(row=1,column=0,padx=10,pady=10)
button_8.grid(row=1,column=1,padx=10,pady=10)
button_9.grid(row=1,column=2,padx=10,pady=10)

button_0.grid(row=4,column=0,padx=10,pady=10)
button_add.grid(row=5,column=0,padx=10,pady=10)
button_equal.grid(row=5,column=1, columnspan=2,padx=10,pady=10)
button_clear.grid(row=4,column=1, columnspan=2,padx=10,pady=10)

button_subtract.grid(row=6,column=0,padx=10,pady=10)
button_multiply.grid(row=6,column=1,padx=10,pady=10)
button_divide.grid(row=6,column=2,padx=10,pady=10)
root.mainloop()