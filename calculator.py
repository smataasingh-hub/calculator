from tkinter import *
def click(event):
    text = event.widget["text"]
    if text == "=":
        try:
            result = eval(e.get())
            e.delete(0, END)
            e.insert(END, str(result))
        except:
            e.delete(0, END)
            e.insert(END, "Error")
    elif text == "AC":
        e.delete(0, END)
    elif text == "del":
        current = e.get()
        e.delete(0, END)
        e.insert(END, current[:-1])
    else:
        e.insert(END, text)

a=Tk()
a.title("CALCULATOR")
a.geometry("1300x700")
a.configure(bg="grey")
e=Entry(a,width=50,borderwidth=5,font=('Arial',16))
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10,ipady=15)

for i in range(5):
    a.grid_columnconfigure(i, weight=1) 
for i in range(1, 5): 
    a.grid_rowconfigure(i, weight=1) 

buttons=[
    ('1',1,0) , ('2',1,1) , ('3',1,2), ('del',1,3),('AC',1,4),
    ('4',2,0) , ('5',2,1) , ('6',2,2), ('+',2,3),('*',2,4),
    ('7',3,0) , ('8',3,1) , ('9',3,2), ('-',3,3), ('/',3,4),
    ('.',4,0) , ('0',4,1) , ('=',4,2)
]
for (text, row, col) in buttons:
    btn = Button(a, text=text, font=('Arial',24))
    btn.grid(row=row, column=col,padx=5, pady=5, sticky="nsew")
    btn.bind("<Button-1>", click)
    if text in {'=', 'AC', 'del'}:
      btn.configure(bg="light green", fg="white", borderwidth=3)
    else:
        btn.configure(bg="light grey", fg="black", borderwidth=3)
    if text == '=':
        btn.grid(columnspan=3, sticky="nsew")


a.mainloop()