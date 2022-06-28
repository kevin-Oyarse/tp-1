import argparse
from ast import parse
from email import parser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as messagebox


root=Tk()
root.title("Calculadora")
mainFrame=Frame(root)
mainFrame.pack()
mainFrame.config(width=480,height=320)#,bg="lightblue")



#Numeros
boton1=ttk.Button(mainFrame,text="1",command=lambda:get_numeros(1))
boton1.grid(column=1,row=5,ipadx=1,ipady=1,padx=1,pady=1) 

boton2=ttk.Button(mainFrame,text="2",command=lambda:get_numeros(2))
boton2.grid(column=2,row=5,ipadx=1,ipady=1,padx=1,pady=1) 

boton3=ttk.Button(mainFrame,text="3",command=lambda:get_numeros(3))
boton3.grid(column=3,row=5,ipadx=1,ipady=1,padx=1,pady=1) 

boton4=ttk.Button(mainFrame,text="4",command=lambda:get_numeros(4))
boton4.grid(column=1,row=4,ipadx=1,ipady=1,padx=1,pady=1) 

boton5=ttk.Button(mainFrame,text="5",command=lambda:get_numeros(5))
boton5.grid(column=2,row=4,ipadx=1,ipady=1,padx=1,pady=1) 

boton6=ttk.Button(mainFrame,text="6",command=lambda:get_numeros(6))
boton6.grid(column=3,row=4,ipadx=1,ipady=1,padx=1,pady=1)

boton7=ttk.Button(mainFrame,text="7",command=lambda:get_numeros(7))
boton7.grid(column=1,row=3,ipadx=1,ipady=1,padx=1,pady=1)

boton8=ttk.Button(mainFrame,text="8",command=lambda:get_numeros(8))
boton8.grid(column=2,row=3,ipadx=1,ipady=1,padx=1,pady=1) 

boton9=ttk.Button(mainFrame,text="9",command=lambda:get_numeros(9))
boton9.grid(column=3,row=3,ipadx=1,ipady=1,padx=1,pady=1) 

boton0=ttk.Button(mainFrame,text="0",command=lambda:get_numeros(0))
boton0.grid(column=2,row=6,ipadx=1,ipady=1,padx=1,pady=1) 


#Funciones
botondiv=ttk.Button(mainFrame,text="/",command= lambda: get_operation("/"))
botondiv.grid(column=4,row=2,ipadx=1,ipady=1,padx=1,pady=1) 

botonsum=ttk.Button(mainFrame,text="+",command= lambda: get_operation("+"))
botonsum.grid(column=4,row=5,ipadx=1,ipady=1,padx=1,pady=1) 

botonresta=ttk.Button(mainFrame,text="-",command= lambda: get_operation("-"))
botonresta.grid(column=4,row=4,ipadx=1,ipady=1,padx=1,pady=1) 

botonmultiplicar=ttk.Button(mainFrame,text="x",command= lambda: get_operation("*"))
botonmultiplicar.grid(column=4,row=3,ipadx=1,ipady=1,padx=1,pady=1) 

botonmigual=ttk.Button(mainFrame,text="=",command=lambda:calcular())
botonmigual.grid(column=4,row=6,ipadx=1,ipady=1,padx=1,pady=1) 

botonAc=ttk.Button(mainFrame,text="AC",command=lambda:limpiar())
botonAc.grid(column=1,row=2,ipadx=1,ipady=1,padx=1,pady=1) 

botonBorrar=ttk.Button(mainFrame,text="<-",command=lambda:borrar())
botonBorrar.grid(column=2,row=2,ipadx=1,ipady=1,padx=1,pady=1) 

botonPorce=ttk.Button(mainFrame,text="x²",command= lambda: get_operation("**2"))
botonPorce.grid(column=3,row=2,ipadx=1,ipady=1,padx=1,pady=1) 

botonParen1=ttk.Button(mainFrame,text="(",command= lambda: get_operation("("))
botonParen1.grid(column=1,row=6,ipadx=1,ipady=1,padx=1,pady=1) 

botonParen2=ttk.Button(mainFrame,text=")",command= lambda: get_operation(")"))
botonParen2.grid(column=3,row=6,ipadx=0.5,ipady=0.5,padx=0.5,pady=0.5) 


display=Entry(mainFrame)
display.grid (row=1,columnspan=5,sticky=W+E)

i=0
def get_numeros(n):
    global i
    display.insert(i,n)
    i+=1

def get_operation(operador):
    global i
    longitud=len (operador)
    display.insert(i,operador)
    i+=longitud

def limpiar():
    display.delete(0, END)

def borrar():
    display_state=display.get()
    if len(display_state):
        display_new=display_state[:-1]
        limpiar()
        display.insert(0,display_new)
    else:
        limpiar()

def calcular():
    display_state=display.get()
    try:
        math_expression =  compile(display_state, 'app.py', 'eval')
        result = eval(math_expression)
        limpiar()
        display.insert(0,result)
    except:
        limpiar()
        messagebox.showerror("Error","No se puede realizar la operacion deseada")

root.mainloop()