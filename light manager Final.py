from tkinter import*
from boltiot import Bolt
import conf
q=False

def turn(a):
    global q
    global counter
    if a==False:
        q=1
        response = mybolt.digitalWrite("0","HIGH")
        print(response)
        b2['text']="Turn OFF"
        plus['state']="active"
        minus['state']="active"
        slider['state']="active"
    else:
        q=0
        response = mybolt.digitalWrite("0","LOW")
        print(response)
        counter.set(0)
        slider.set(0)
        b2['text']="Turn ON"
        plus['state']="disabled"
        minus['state']="disabled"
        slider['state']="disabled"

def getslider(event):
    response=mybolt.analogWrite("0",slider.get())
    print(slider.get())

mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)#Bolt initial
root = Tk()#Tkinter window
root.geometry("400x400+0+0")
root.title("Awesome")
counter = IntVar()
lab=Label(root,width=400,height=400,background="#9999FF")
lab.pack()
title=Label(lab,width=48,height=2,background="#9999FF",text="Light intensity controller",anchor="center",font=("Courier", 10 ,"bold"))
title.place(x=0,y=0)
b2 = Button(lab, text = "Turn ON", width=10, height=2, background="#9966ff", command=lambda:turn(q))
b2.place(x = 150 , y = 50)
title1=Label(lab,width=48,height=2,background="#9999FF",text="Or use the slider to control the intensity",anchor="center",font=("Courier", 10 ,"bold"))
title1.place(x=0,y=110)
slider = Scale(lab, from_=0, to=200, orient=HORIZONTAL, background="#9966ff", command=getslider)
slider.place(x=135,y=160)

title1=Label(lab,width=48,height=2,background="#9999FF",text="Or use the incrementer",anchor="center",font=("Courier", 10 ,"bold"))
title1.place(x=0,y=210)

setter=Label(lab,width=14,height=3,background="#9999FF")
setter.place(x=136,y=250)


def add(event=None):
    counter.set(counter.get() + 1)
    response=mybolt.analogWrite("0",counter.get())

def subtract(event=None):
    counter.set(counter.get() - 1)
    response=mybolt.analogWrite("0",counter.get())
    

val=Label(setter, textvariable=counter, width=5, height=2, background="#9999FF")
val.place(x=30,y=0)
plus=Button(setter, text="-", command=subtract, fg="dark green", bg = "#9966ff")
plus.place(x=5,y=5)
minus=Button(setter, text="+", command=add, fg="dark green", bg = "#9966ff")
minus.place(x=79,y=5)
plus['state']="disabled"
minus['state']="disabled"
slider['state']="disabled"

def destroy():
    root.destroy()

out=Button(lab, text = "EXIT", width=10, height=2, background="#9966ff",command=destroy)
out.place(x=149,y=310)


root.mainloop()
