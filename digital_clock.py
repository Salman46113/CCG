from time import strftime
from tkinter import Label, Tk
win = Tk()
win.title("Clock")
#win.geometry('200 x 200')
win.configure(bg = 'black')
#win.resizable(False,False)
c_l = Label(win,bg='black',fg = 'white',font=('times',30,'bold'),relief='flat')
c_l.place(x=20,y=20)
def update_lable():
    current_time = strftime('%H %M %S')
    c_l.configure(text = current_time)
    c_l.after(80,update_lable)
update_lable()
win.mainloop()