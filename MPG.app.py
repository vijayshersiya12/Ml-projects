import tkinter as tk
import pickle
#Loading the mpg predicting model......................................
with open("mpg_model.pkl",'rb') as fp:
    model=pickle.load(fp)
    fp.close()
#Predict function to predict mpg......................................
def predict():
    h=hor.get()
    w=wei.get()
    d=dis.get()
    clear()
    pre=model.predict([[h,w,d]])[0]
    win=tk.Toplevel(root)
    win.grab_set()
    text=f"""
    __________________
    Horsepowr={h}
    Weight={w}
    Displacement={d}
    ___________________
    mpg={pre:.2f}"""
    msg=tk.Message(win,text=text)
    msg.config(bg="#eeeeee",fg="#000000",font=("Times",20,"bold"))
    msg.pack()
    eb=tk.Button(win,text="EXIT",bg="red",fg="#000000",command=win.destroy)
    eb.pack(fill=tk.X,expand=tk.YES)
#creating tkinter window..........................................................
root=tk.Tk()
#variables.........................................................
hor=tk.DoubleVar()
wei=tk.DoubleVar()
dis=tk.DoubleVar()
#clar function to clear variable values..............................
def clear():
    hor.set("")
    wei.set("")
    dis.set("")
clear()
#Labels and entry boxes.............................................
#Frame 1
f1=tk.Frame(root)
l1=tk.Label(f1,bg="#eeeeee",fg="#000000",text="Horsepower".center(20)+":")
l1.config(font=("Times",20,"bold"))
l1.pack(side=tk.LEFT,fill=tk.X,expand=tk.YES)
e1=tk.Entry(f1,textvariable=hor)
e1.config(bg="#eeeeee",fg="#000000",font=("Times",20,"bold"))
e1.focus()
e1.pack(side=tk.LEFT,fill=tk.X,expand=tk.YES)
f1.pack(fill=tk.BOTH,expand=tk.YES,padx=20,pady=20)
#Frame 2
f2=tk.Frame(root)
l2=tk.Label(f2,bg="#eeeeee",fg="#000000",text="Weight".center(20)+":")
l2.config(font=("Times",20,"bold"))
l2.pack(side=tk.LEFT,fill=tk.X,expand=tk.YES)
e2=tk.Entry(f2,textvariable=wei)
e2.config(bg="#eeeeee",fg="#000000",font=("Times",20,"bold"))
e2.pack(side=tk.LEFT,fill=tk.X,expand=tk.YES)
f2.pack(fill=tk.BOTH,expand=tk.YES,padx=20,pady=20)
#Frame 3
f3=tk.Frame(root)
l3=tk.Label(f3,bg="#eeeeee",fg="#000000",text="Displacement".center(20)+":")
l3.config(font=("Times",20,"bold"))
l3.pack(side=tk.LEFT,fill=tk.X,expand=tk.YES)
e3=tk.Entry(f3,textvariable=dis)
e3.config(bg="#eeeeee",fg="#000000",font=("Times",20,"bold"))
e3.pack(side=tk.LEFT,fill=tk.X,expand=tk.YES)
f3.pack(fill=tk.BOTH,expand=tk.YES,padx=20,pady=20)
#Buttons.............................................................
b1=tk.Button(root,bg="cyan",fg="#000000",text='Predict Mileage',command=predict)
b1.config(font=("Times",20,"bold"))
b1.pack(fill=tk.X,expand=tk.YES)
b2=tk.Button(root,bg="cyan",fg="#000000",text='EXIT',command=root.quit)
b2.config(font=("Times",20,"bold"))
b2.pack(fill=tk.X,expand=tk.YES)

root.title("Predict MPG")
root.mainloop()
