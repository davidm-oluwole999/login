from tkinter import *
root= Tk()
root.geometry('300x300')
root.config(background='midnight blue')
Title=Label(root,text='Login Page', bg='midnight blue', fg='white').place(x= 10, y=10)
entrybox1=Entry(root, text='Enter your username:').place(x=100, y=100)
submit=Button(root, text= 'Submit').place(x=100, y=120)

root.mainloop()