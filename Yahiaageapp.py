from tkinter import *
from tkinter import messagebox
age_app=Tk()
age_app.title("Yahia age units app")
age_app.geometry("400x200")
label1=Label(age_app,text="Enter your age",width=20,font=('Arial',20))
label1.pack()
age=StringVar()
age.set("00")
entry1=Entry(age_app,width=3,font=('Arial',20),textvariable=age)
entry1.pack()

def calculate_age():
    
    ageValue=age.get() # string variable
    ageMonths=int(ageValue)*12 # amgMonths is integer number
    ageweeks=ageMonths*4
    agedays=int(ageValue)*365
    print(ageMonths)
    print(ageweeks)
    print(agedays)
    messagebox.showinfo("Age in time units","your age in months is"+str(ageMonths))    
    messagebox.showinfo("Age in time units","your age in weeks is"+str(ageweeks))    
    messagebox.showinfo("Age in time units","your age in days is"+str(agedays))
button1=Button(age_app,text='Calculate',width=10,bg='green'
               ,command=calculate_age,font=('Arial',20))
button1.pack()
age_app.mainloop()
