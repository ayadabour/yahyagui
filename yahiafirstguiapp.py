from tkinter import *
window=Tk()
window.geometry('300x300')
window.title("Printer")
def printing():
    print("Hello Yahia")




    
button1=Button(window,text='Print',bg='green',
               fg='white',font=20,width=10,height=2,command=printing)
button1.pack()
#button1.grid(row=1,column=1)
#button2=Button(window,text='text')
#button1.pack()
#button2.grid(row=2,column=2)
#button2.place(x=150,y=150)
