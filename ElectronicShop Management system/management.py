# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *
import time
import random
import json

#============main Frame==========================
root=Tk()
root.geometry("1600x800+0+0")
root.title("Braj Electronics")
#root.configure(bg="#c63083")

#===============================Inside Frame=========================
tops=Frame(root,width=1600,height=50,relief=SUNKEN)
tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300,height=700,bg="powder blue",relief=SUNKEN)
f2.pack(side=RIGHT)

#======================for calculating Time==========================
localtime=time.asctime(time.localtime(time.time()))

#=Label(Header)
labelInfo=Label(tops,font=("arial",30,'bold'),text="Braj Electronics",bd=10,
                fg="steel blue",anchor='w')
labelInfo.grid(row=0,column=0)

labelInfo_Time=Label(tops,font=("arial",20,'bold'),text=localtime,bd=10,
                fg="steel blue",anchor='w')
labelInfo_Time.grid(row=1,column=0)
########################################################################################################
#===============================Calculator====================#

#========text_Input
text_Input=StringVar()

txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,
                 insertwidth=4,bg='powder blue',justify="right")
#========txtDisplay.pack(side=TOP)
txtDisplay.grid(columnspan=4)

#DEfine function btnClick(),,btnClearDisp,btnEqualEval
#global operators
operators=""
def btnClick(numbers):
    global operators
    operators=operators+str(numbers)
    text_Input.set(operators)
    
def btnClearDisp():
    global operators
    operators=""
    text_Input.set("") 
    
def btnEqualEval():
    global operators
    op=operators
    sumup=str(eval(op))
    text_Input.set(sumup)
    operators=""    

#=======Buttons
btn7=Button(f2,padx=16,pady=16,bg='powder blue',fg='black',bd=8,
            font=('arial',20,'bold'),text='7',command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bg='powder blue',fg='black',bd=8,
            font=('arial',20,'bold'),text='8',command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bg='powder blue',fg='black',bd=8,
            font=('arial',20,'bold'),text='9',command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=Button(f2,padx=16,pady=16,bg='powder blue',fg='black',bd=8,
            font=('arial',20,'bold'),text='+',command=lambda:btnClick("+")).grid(row=2,column=3)

###############################
btn4=Button(f2,padx=16,pady=16,bg='powder blue',fg='black',bd=8,
            font=('arial',20,'bold'),text='4',command=lambda:btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bg='powder blue',fg='black',bd=8,
            font=('arial',20,'bold'),text='5',command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bg='powder blue',fg='black',bd=8,
            font=('arial',20,'bold'),text='6',command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub=Button(f2,padx=16,pady=16,bg='powder blue',fg='black',bd=8,
            font=('arial',20,'bold'),text='-',command=lambda:btnClick("-")).grid(row=3,column=3)

###############################
btn1=Button(f2,padx=16,pady=16,bg='powder blue',fg='black',bd=8,
            font=('arial',20,'bold'),text='1',command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bg='powder blue',fg='black',bd=8,
            font=('arial',20,'bold'),text='2',command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16,bg='powder blue',fg='black',bd=8,
            font=('arial',20,'bold'),text='3',command=lambda:btnClick(3)).grid(row=4,column=2)
btnMul=Button(f2,padx=16,pady=16,bg='powder blue',fg='black',bd=8,
            font=('arial',20,'bold'),text='x',command=lambda:btnClick("*")).grid(row=4,column=3)

###############################
btn0=Button(f2,padx=16,pady=16,bg='powder blue',fg='black',bd=8,
            font=('arial',20,'bold'),text='0',command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,bg='powder blue',fg='black',bd=8,
            font=('arial',20,'bold'),text='C',command=btnClearDisp).grid(row=5,column=1)
btnEqual=Button(f2,padx=16,pady=16,bg='powder blue',fg='black',bd=8,
            font=('arial',20,'bold'),text='=',command=btnEqualEval).grid(row=5,column=2)
btnDiv=Button(f2,padx=16,pady=16,bg='powder blue',fg='black',bd=8,
            font=('arial',20,'bold'),text='/',command=lambda:btnClick("/")).grid(row=5,column=3)
##################################################################################################################

######################Entries of the product#######################

Rand=StringVar()
Torch=StringVar()
Fan=StringVar()
LED=StringVar()
Mixer=StringVar()
Bulb=StringVar()
AC=StringVar()
Cooler=StringVar()
Cost=StringVar()
Tax=StringVar()
TotalCost=StringVar()

CTorch=600
CFan=1200
CLED=200
CMixer=3000
CBulb=25
CAC=25000
CCooler=10500
CTax=0.05

def Ref():
    x=random.randint(12000,50000)
    refer=str(x)
    Rand.set(refer)
    
    cost=(int(Torch.get())*CTorch)+(int(Fan.get())*CFan)+(int(LED.get())*CLED)+(int(Mixer.get())*CMixer)+(int(Bulb.get())*CBulb)+(int(AC.get())*CAC)+(int(Cooler.get())*CCooler)
    cost1=str(cost)
    Cost.set(cost1)
    
    Tax.set("5%")
    totalcost=CTax*cost+cost
    totalcost1=str(totalcost)
    TotalCost.set(totalcost1)
    dicti={}
    dicti['Torch']=Torch.get()
    dicti['Fan']=Fan.get()
    dicti['LED']=LED.get()
    dicti['Mixer']=Mixer.get()
    dicti['Bulb']=Bulb.get()
    dicti['AC']=AC.get()
    dicti['Cooler']=Cooler.get()
    dicti['Cost']=cost
    dicti['Total Cost']=totalcost
    file=open("data.json",'a')
    data1=json.dumps(dicti)
    print(data1)
    file.write(data1)
    
    
    
def Reset():
    Rand.set("")
    Torch.set("")
    Fan.set("")
    LED.set("")
    Mixer.set("")
    Bulb.set("")
    AC.set("")
    Cooler.set("")
    Cost.set("")
    Tax.set("")
    TotalCost.set("") 
    
def Quit():
    root.destroy()    
    
#Reference
labelRef=Label(f1,font=("arial",16,'bold'),text="Reference",bd=10,
                fg="black",anchor='w')
labelRef.grid(row=0,column=0)
RefDisplay=Entry(f1,font=('arial',16,'bold'),textvariable=Rand,bd=10,
                 insertwidth=4,bg='powder blue',justify="right")
RefDisplay.grid(row=0,column=1)
#Torch
labelTorch=Label(f1,font=("arial",16,'bold'),text="Torch",bd=10,
                fg="black",anchor='w')
labelTorch.grid(row=1,column=0)
TorchDisplay=Entry(f1,font=('arial',16,'bold'),textvariable=Torch,bd=10,
                 insertwidth=4,bg='powder blue',justify="right")
TorchDisplay.grid(row=1,column=1)
#Fan
labelFan=Label(f1,font=("arial",16,'bold'),text="Fan",bd=10,
                fg="black",anchor='w')
labelFan.grid(row=2,column=0)
FanDisplay=Entry(f1,font=('arial',16,'bold'),textvariable=Fan,bd=10,
                 insertwidth=4,bg='powder blue',justify="right")
FanDisplay.grid(row=2,column=1)
#LED
labelLED=Label(f1,font=("arial",16,'bold'),text="LED",bd=10,
                fg="black",anchor='w')
labelLED.grid(row=3,column=0)
LEDDisplay=Entry(f1,font=('arial',16,'bold'),textvariable=LED,bd=10,
                 insertwidth=4,bg='powder blue',justify="right")
LEDDisplay.grid(row=3,column=1)
#Mixer
labelMixer=Label(f1,font=("arial",16,'bold'),text="Mixer",bd=10,
                fg="black",anchor='w')
labelMixer.grid(row=4,column=0)
MixerDisplay=Entry(f1,font=('arial',16,'bold'),textvariable=Mixer,bd=10,
                 insertwidth=4,bg='powder blue',justify="right")
MixerDisplay.grid(row=4,column=1)
#Bulb
labelBulb=Label(f1,font=("arial",16,'bold'),text="Bulb",bd=10,
                fg="black",anchor='w')
labelBulb.grid(row=5,column=0)
BulbDisplay=Entry(f1,font=('arial',16,'bold'),textvariable=Bulb,bd=10,
                 insertwidth=4,bg='powder blue',justify="right")
BulbDisplay.grid(row=5,column=1)
#AC
labelAC=Label(f1,font=("arial",16,'bold'),text="AC",bd=10,
                fg="black",anchor='w')
labelAC.grid(row=0,column=2)
ACDisplay=Entry(f1,font=('arial',16,'bold'),textvariable=AC,bd=10,
                 insertwidth=4,bg='powder blue',justify="right")
ACDisplay.grid(row=0,column=3)
#Cooler
labelCooler=Label(f1,font=("arial",16,'bold'),text="Cooler",bd=10,
                fg="black",anchor='w')
labelCooler.grid(row=1,column=2)
CoolerDisplay=Entry(f1,font=('arial',16,'bold'),textvariable=Cooler,bd=10,
                 insertwidth=4,bg='powder blue',justify="right")
CoolerDisplay.grid(row=1,column=3)
#Cost
labelCost=Label(f1,font=("arial",16,'bold'),text="Cost",bd=10,
                fg="black",anchor='w')
labelCost.grid(row=2,column=2)
CostDisplay=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,
                 insertwidth=4,bg='powder blue',justify="right")
CostDisplay.grid(row=2,column=3)

#tax
labelTax=Label(f1,font=("arial",16,'bold'),text="Tax",bd=10,
                fg="black",anchor='w')
labelTax.grid(row=3,column=2)
TaxDisplay=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,
                 insertwidth=4,bg='powder blue',justify="right")
TaxDisplay.grid(row=3,column=3)
#TotalCost
labelTotalCost=Label(f1,font=("arial",16,'bold'),text="Total Cost",bd=10,
                fg="black",anchor='w')
labelTotalCost.grid(row=4,column=2)
TotalCostDisplay=Entry(f1,font=('arial',16,'bold'),textvariable=TotalCost,bd=10,
                 insertwidth=4,bg='powder blue',justify="right")
TotalCostDisplay.grid(row=4,column=3)

#Buttons
btnTotal=Button(f1,padx=16,pady=8,bg='powder blue',fg='black',bd=10,
            font=('arial',20,'bold'),text='Total',command=Ref).grid(row=7,column=1)
btnReset=Button(f1,padx=16,pady=8,bg='powder blue',fg='black',bd=10,
            font=('arial',20,'bold'),text='Reset',command=Reset).grid(row=7,column=2)
btnQuit=Button(f1,padx=16,pady=8,bg='powder blue',fg='black',bd=10,
            font=('arial',20,'bold'),text='Quit',command=Quit).grid(row=7,column=3)


#for running GUI
root.mainloop()


