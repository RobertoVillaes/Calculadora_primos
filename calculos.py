from tkinter import *
import parser
from desplaza1 import *
from math import * # Con esto la calculadora funciona para cualquier expresion correcta escrita con el teclado, sin, cos, tan etc. en DAME N.
raiz =Tk()
raiz.title("O P E R A C I O N E S   C O N   U N O   O   D O S   N U M E R O S   (E N T E R O S)  Y  A L G U NA S   F U N C I O N E S")
raiz.config(bg="#7F7F7F")
raiz.resizable(0,0)
operacion=""
resultado=0
vari=IntVar()
n=StringVar()
m=IntVar()
p=StringVar() #es equivalente a n
q=IntVar() #equi a m
resp=StringVar()
i=0
	
def numeropulsado(n):
    global i
    txtNum.insert(i,n)
    i+=1
def get_operador(operador):
    global i
    long_operador=len(operador)
    txtNum.insert(i,operador)
    i+=long_operador
def limpiar():
    txtNum.delete(0,END)
def borra():
    estado_actual=txtNum.get()
    if len(estado_actual):
        display_nuevo_estado=estado_actual[:-1]
        limpiar()
        txtNum.insert(0,display_nuevo_estado)
    else:
        limpiar()
def calcula():
    estado_actual=txtNum.get()
    try:
        expre_mate = parser.expr(estado_actual).compile()
        resultado=eval(expre_mate)
        limpiar()
        txtNum.insert(0,resultado)
    except:
        limpiar()
        txtNum.insert(0,"ERROR")
def divi():
    vari.set(1)
    consigueN()
def primu():
	vari.set(2)
	consigueN()
def si():
	vari.set(3)
	consigueN()
def lp():
	vari.set(4)
	consigueN()
def fac():
	vari.set(6)
	consigueN()
def ndiv():
    vari.set(7)
    consigueN()
def pd():
	vari.set(8)
	consigueN()
def coc():
	vari.set(5)
	consigueN()
def res():
    vari.set(9)
    consigueN()
def ulti():
	vari.set(10)
	consigueN()
def ult():
    vari.set(11)
    consigueN()
def siPer():
    vari.set(12)
    consigueN()
def lppri():
    vari.set(13)
    consigueN()
def elim():
    vari.set(14)
    consigueN()
def elimina():
    ctxt.delete("1.0",END)  

def consigueN():
    if n !="" and vari.get()==1:
        m=int(n.get())
        resp=str(sorted(divisores(m)))
        ctxt.insert(INSERT, "Los divisores de N son "+resp + "\n")
    elif  n !="" and vari.get()==2:
        m=int(n.get())
        resp=primi(m)
        ctxt.insert(INSERT,  str(resp) + "\n")
    elif n !=""and vari.get()==3:
        m=int(n.get())
        resp=str(sigup(m))
        ctxt.insert(INSERT,  "El siguiente primo al numero N es el " + resp+"\n")
    elif n !="" and p != "" and vari.get()==4:
        q=int(p.get())
        m=int(n.get())
        resp=str(list (listp(q,m)) [0])
        ctxt.insert(INSERT,  "Los "+ str(q)+ " primos a partir de N (incluido N, si es primo) son: " + resp+"\n")
    elif n!="" and vari.get()==5:
        q=int(p.get())
        m=int(n.get())
        resp=str(cociente(m,q))
        ctxt.insert(INSERT, "El cociente de dividir N entre M es: " + resp + "\n")
    elif n!="" and vari.get()==6:
        m=int(n.get())
        resp=str(factores_primos(m))
        ctxt.insert(INSERT,  "Los factores  primos de N son:" + resp+  " (primo,exponente).\n")
    elif n!="" and vari.get()==7:
        m=int(n.get())
        resp=str(n_divisores(m))
        ctxt.insert(INSERT,  "El numero N tiene " + resp + " divisores enteros.(incluidos el 1 y  el)\n")
    elif n!="" and vari.get()==8:
        m=int(n.get())
        resp=str(primer_divisor(m))
        ctxt.insert(INSERT,  "El primer divisor de N es el " + resp+"\n")
    elif n!="" and vari.get()==9:
        q=int(p.get())
        m=int(n.get())
        resp=str(resto(m,q))
        ctxt.insert(INSERT,  "El resto de dividir N entre M es " + resp+"\n")
    elif n!="" and vari.get()==10:
        m=int(n.get())
        resp=str(ultimo_divisor_primo(m))
        ctxt.insert(INSERT,  "El ultimo divisor primo de N es: "  + resp+"\n")
    elif n!="" and vari.get()==11:
        m=int(n.get())
        resp=str(ultimo_divisor(m))
        ctxt.insert(INSERT, "El ultimo divisor de N es: " + resp+"\n")
    elif n!="" and vari.get()==12:
        m=int(n.get())
        resp=str(sigMp(m))
        ctxt.insert(INSERT,"El primo siguiente a N, que genera un numero perfecto es:"+ resp +" y su valor:2**"+str(int(resp)-1)+"*(2**"+resp +"-1)\n")
    elif n !="" and p != "" and vari.get()==13:
        q=int(p.get())
        m=int(n.get())
        resp=str(f_pj(m,q))
        ctxt.insert(INSERT,"Los "+ str(q)+ " primeros factores primos(si tiene tantos) de N son: " + resp +"(primo,exponente)\n")
    elif vari.get()==14:
        resp=str(elimina())
           
ventana=Frame(raiz)
ventana.pack(side="top")
ventana.config(bg="#32501C", width=1650,bd=35,relief=SUNKEN)
#Creamos el campo  para introducir el N
lblNum=Label(ventana,text="DAME N:", font=("Garuda", 14),fg="#D0C8C8",bg="#32501C",pady=5)
lblNum.grid(row=1,column=0,sticky=E)
txtNum=Entry(ventana,  font=("Arial", 15),textvariable=n, width=100,bg="#000000",fg="#5EEB20")
txtNum.grid(row=1,column=1,sticky=W)
#Creamos el campo  para introducir el M
lblNum=Label(ventana,text="DAME M:", font=("Garuda", 15),fg="#D0C8C8",bg="#32501C",pady=5)
lblNum.grid(row=2,column=0,sticky=E)
txtPum=Entry(ventana,  font=("Garuda", 15),textvariable=p, width=100,bg="#000000",fg="#5EEB20")
txtPum.grid(row=2,column=1,sticky=W)
#Definimos el cuadro de texto, para que nos presente las respuestas.
ctxt=Text(ventana, bg="#473313", fg="#FFFFFF", font=("Arial",14))
ctxt.grid(row=0, column=0, columnspan=2)
ctxt.config(width=120, height=14,cursor="hand2")#Ah si, aqui he dado el alto 13 lineas.
#Ahora el scrollbar
scrollVert=Scrollbar(ventana, command=ctxt.yview)
scrollVert.grid(row =0,column=2,sticky="nsew")
ctxt.config(yscrollcommand=scrollVert.set)
#Creamos la ventana2 para poner las botones de las funciones
ventana2=Frame()
ventana2.pack(side="left")
ventana2.config(bg="#7F7F7F")
#CReamos el boton para terminar el programa (Salir)
btnSalir=Button(ventana2, text="SALIR",command=raiz.destroy,relief=RAISED,bd=15,bg="#FF3313",fg="#0000FF",font=("Garuda", 15))
btnSalir.grid(row=1,column=0,padx=65,pady=0)
#Colocamos los botones de Primalidad 
btnPrimo=Button (ventana2, text="¿Es Primo(N)?",bd=8,relief=RAISED,bg="#1E90FF",fg="#ffffff",font=("Garuda",12),command=primu)
btnPrimo.grid(row=0,column=1)
btnDivisores=Button (ventana2, text=" Divisores(N)",bd=8,relief=RAISED,bg="#1E90FF",fg="#ffffff",font=("Garuda",12),command=divi)
btnDivisores.grid(row=0,column=2)
btnFact_Primos=Button (ventana2, text="Factores_Primos(N)",bd=8,relief=RAISED,bg="#1E90FF",fg="#ffffff",font=("Garuda",12),command=fac)
btnFact_Primos.grid(row=0,column=3)
btnSigup=Button (ventana2, text=" Siguiente_Primo(N)",bd=8,relief=RAISED,bg="#1E90FF",fg="#ffffff",font=("Garuda",12),command=si)
btnSigup.grid(row=0,column=4)
btnLpriN_M=Button (ventana2, text=" Lista_Primos[N-M]",bd=8,relief=RAISED,bg="#1E90FF",fg="#ffffff",font=("Garuda",12),command=lp)
btnLpriN_M.grid(row=1,column=4)
btnPrimer_D=Button (ventana2, text=" Primer Divisor(N)    ",bd=8,relief=RAISED,bg="#1E90FF",fg="#ffffff",font=("Garuda",12),command=pd)
btnPrimer_D.grid(row=1,column=3)
btnN_Divisores=Button (ventana2, text="Número de Divisores(N)",bd=8,relief=RAISED,bg="#1E90FF",fg="#ffffff",font=("Garuda",12),command=ndiv)
btnN_Divisores.grid(row=0,column=5)
btnCoci=Button (ventana2, text="Cociente(N//M)",bd=8,relief=RAISED,bg="#1E90FF",fg="#ffffff",font=("Garuda",12),command=coc)
btnCoci.grid(row=1,column=1)
btnResto=Button (ventana2, text="Resto(N%M)",bd=8,relief=RAISED,bg="#1E90FF",fg="#ffffff",font=("Garuda",12),command=res)
btnResto.grid(row=1,column=2)
btnUltDivp=Button (ventana2, text="  Último divisor Primo(N)",bd=8,relief=RAISED,bg="#1E90FF",fg="#ffffff",font=("Garuda",12),command=ulti)
btnUltDivp.grid(row=1,column=5)
btnUltDiv=Button (ventana2, text="  Último divisor(N)   ",bd=8,relief=RAISED,bg="#1E90FF",fg="#ffffff",font=("Garuda",12),command=ult)
btnUltDiv.grid(row=2,column=3)
btnSigPerf=Button (ventana2, text=" Siguiente_Perfecto(N)",bd=8,relief=RAISED,bg="#1E90FF",fg="#ffffff",font=("Garuda",12),command=siPer)
btnSigPerf.grid(row=2,column=5)
btnPPrimos=Button (ventana2, text="M 1ºs F_Pri(N)",bd=8,relief=RAISED,bg="#1E90FF",fg="#ffffff",font=("Garuda",12),command=lppri)
btnPPrimos.grid(row=2,column=1)
btnBorrar=Button(ventana2,text="Borrar Pantalla",bd=8,relief=RAISED,bg="#FF3313",fg="#0000FF",font=("Garuda",12),command=elim)   
btnBorrar.grid(row=2,column=2)
#Creamos la ventana3 para las teclas de la calculadora
ventana3=Frame(raiz)
ventana3.pack()#side="left")
ventana3.config(bg="#7F7F7F")
#Creamos la fila numero 1 donde van 7,8,9 y + borrar1.
btn7=Button(ventana3,text="7",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:numeropulsado("7"))
btn7.grid(row =0,column=0,sticky=W+E)
btn8=Button(ventana3,text="8",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:numeropulsado("8"))
btn8.grid(row =0,column=1,sticky=W+E)
btn9=Button(ventana3,text="9",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:numeropulsado("9"))
btn9.grid(row =0,column=2,sticky=W+E)
btnMas=Button(ventana3,text="+",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:get_operador("+"))
btnMas.grid(row=0,column=3,sticky=W+E)
btnBorr1=Button(ventana3,text="⇽",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:borra())
btnBorr1.grid(row =0,column=4,sticky=W+E,columnspan=2)
#Creamos la fila numero 2 donde van 4,5,6 ,-,Expt y Raiz.
btn4=Button(ventana3,text="4",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:numeropulsado("4"))
btn4.grid(row =1,column=0,sticky=W+E)
btn5=Button(ventana3,text="5",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:numeropulsado("5"))
btn5.grid(row =1,column=1,sticky=W+E)
btn6=Button(ventana3,text="6",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:numeropulsado("6"))
btn6.grid(row =1,column=2,sticky=W+E)
btnMenos=Button(ventana3,text="-",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:get_operador("-"))
btnMenos.grid(row =1,column=3,sticky=W+E)
btnExp=Button(ventana3,text="Exp",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:get_operador("**"))
btnExp.grid(row =1,column=4,sticky=W+E)
btnRaiz=Button(ventana3,text="√",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:get_operador("**0.5"))
btnRaiz.grid(row=1,column=5,sticky=W+E)
#Creamos la fila numero 3 donde van 1,2,3 ,x ( y ).
btn1=Button(ventana3,text="1",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:numeropulsado("1"))
btn1.grid(row =2,column=0,sticky=W+E)
btn2=Button(ventana3,text="2",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:numeropulsado("2"))
btn2.grid(row =2,column=1)
btn3=Button(ventana3,text="3",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:numeropulsado("3"))
btn3.grid(row=2,column=2,sticky=W+E)
btnPor=Button(ventana3,text="*",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:get_operador("*"))
btnPor.grid(row =2,column=3,sticky=W+E)
btnParea=Button(ventana3,text="(",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:get_operador("("))
btnParea.grid(row =2,column=4,sticky=W+E)
btnParec=Button(ventana3,text=")",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:get_operador(")"))
btnParec.grid(row =2,column=5,sticky=W+E)
#Creamos la fila numero 4 donde van AC,0,.,/,=.
btnAC=Button(ventana3,text="AC",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:limpiar())
btnAC.grid(row =3,column=0,sticky=W+E)
btn0=Button(ventana3,text="0",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:numeropulsado("0"))
btn0.grid(row =3,column=1,sticky=W+E)
btnComa=Button(ventana3,text=".",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:get_operador("."))
btnComa.grid(row =3,column=2,sticky=W+E)
btnDiv=Button(ventana3,text="/",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:get_operador("/"))
btnDiv.grid(row =3,column=3,sticky=W+E)
btnIgual=Button(ventana3,text=" = ",bd=8,relief=RAISED,bg="#8B6914",fg="#ffffff",font=("Garuda",12),command=lambda:calcula())
btnIgual.grid(row =3,column=4,sticky=W+E,columnspan=2)

raiz.mainloop()
