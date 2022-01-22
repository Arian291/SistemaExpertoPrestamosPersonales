import tkinter as tk
import sys
from pyswip import Prolog 

class MainWindow:
    def __init__(self, root):
        root.title("Sistema Experto")
        root.geometry("1000x550")
        root.iconbitmap("form.ico")
        root.config(bg="#F4FBAF")
        root.resizable(0,0)
        label1= tk.Label(root,text= "SISTEMA DE EVALUACIÓN DE PRESTAMOS PERSONALES",bg="#F4FBAF",fg="brown",font=('Comic Sans MS',24,),width=50,height=3)
        label1.pack()
        self.imagen=tk.PhotoImage(file ='form.png')
        label2 =tk.Label(root, image=self.imagen, bg="#F4FBAF",width=750,height=250)
        label2.pack()
        texto="Para poder averiguar si eres un candidato para acceder a un préstamo \n del banco presiona el botón consultar"
        label3= tk.Label(root,text= texto,bg="#F4FBAF",font=('Comic Sans MS',14))
        label3.pack()
        button2 = tk.Button(root, text="SALIR", command=self.finalizar,bg="brown",fg="white",font=('Comic Sans MS',17))
        button2.pack(padx=25,pady=25,side=tk.RIGHT)
        button = tk.Button(root, text="CONSULTAR", command=self.consulta,bg="brown",fg="white",font=('Comic Sans MS',17))
        button.pack(padx=25,pady=25,side=tk.RIGHT)
        
    def consulta(self):
        window=Consultar()
    
    
    def finalizar(self):
        sys.exit(0)

class Consultar:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.geometry("600x350")
        self.ventana.iconbitmap("form.ico")
        self.ventana.config(bg="#F4FBAF")
        self.ventana.resizable(0,0)
        self.label1=tk.Label(self.ventana,text= "CONTESTA LAS SIGUIENTES PREGUNTAS",bg="#F4FBAF",fg="brown",font=('Comic Sans MS',18,'bold'))
        self.label1.grid(column=0, row=0,columnspan=4, padx=0,pady=2)
        self.texto ="Selecciona la opcion correcta"
        self.label3= tk.Label(self.ventana, text= self.texto,bg="#F4FBAF",font=('Comic Sans MS',14))
        self.label3.grid(column=0, row=1,columnspan=4, padx=0,pady=2)

        self.radioValue=[]
        self.labels=[]
        self.desitions=[]
        self.rdioSi=[]
        self.rdioNo=[]
        self.pre=[]
        for i in range(6):
            self.rvP=tk.IntVar()
            self.radioValue.append(self.rvP)         
            self.lista = list(prolog.query("pregunta("+str(i+1)+",X)."))
            self.pre.append(self.lista[0]["X"])
            
            self.lbp= tk.Label(self.ventana, text=self.pre[i],bg="#F4FBAF",font=("Arial",12),height=1)
            self.labels.append(self.lbp)
            self.labels[i].grid(column=0, row=i+3, sticky="W",pady=2)
            self.rSi= tk.Radiobutton(self.ventana, text='Si',bg="#F4FBAF",variable=self.radioValue[i], value=1) 
            self.rdioSi.append(self.rSi)
            self.rNo= tk.Radiobutton(self.ventana, text='No',bg="#F4FBAF",variable=self.radioValue[i], value=0) 
            self.rdioNo.append(self.rNo)
            
            self.rdioSi[i].grid(column=1, row=i+3,pady=2)
            self.rdioNo[i].grid(column=2, row=i+3,pady=2)

        self.boton1=tk.Button(self.ventana, text="Salir", command=self.ventana.destroy,bg="brown",fg="white",font=('Comic Sans MS',14))
        self.boton1.grid(column=2, row=14,padx=0,pady=5)
        
        self.boton2=tk.Button(self.ventana, text="Siguiente", command=self.consultar,bg="brown",fg="white",font=('Comic Sans MS',14))
        self.boton2.grid(column=3, row=14,padx=0,pady=5)
        self.ventana.mainloop()

    def consultar(self):
        self.consulta=""
        self.gar=False
        for i in range(6):
            self.labelValue = tk.Label(self.ventana, textvariable=self.radioValue[i])
            self.resp=self.labelValue.cget("text")
            if self.resp==1:
                self.resp="si"
            else:
                self.resp="no"
            if (i==5) &(self.resp=="no"):
                self.gar=True
            self.consulta+=self.resp+","
        self.ventana.destroy()
        
        if self.gar==True:
            ventanasig=Respuesta(self.consulta,1)
        else:
            ventanasig=Consultar2(self.consulta)


class Consultar2:
    def __init__(self, consulta):
        self.consulta=consulta
        self.ventana = tk.Toplevel()
        self.ventana.geometry("600x350")
        self.ventana.iconbitmap("form.ico")
        self.ventana.config(bg="#F4FBAF")
        self.ventana.resizable(0,0)
        self.label1=tk.Label(self.ventana,text= "CONTESTA LAS SIGUIENTES PREGUNTAS",bg="#F4FBAF",fg="brown",font=('Comic Sans MS',18,'bold'))
        self.label1.grid(column=0, row=0,columnspan=4, padx=0,pady=2)
        self.texto ="Selecciona la opcion correcta \n sobre el garante"
        self.label3= tk.Label(self.ventana, text= self.texto,bg="#F4FBAF",font=('Comic Sans MS',14))
        self.label3.grid(column=0, row=1,columnspan=4, padx=0,pady=2)

        self.radioValue=[]
        self.labels=[]
        self.desitions=[]
        self.rdioSi=[]
        self.rdioNo=[]
        self.pre=[]
        for i in range(6):
            self.rvP=tk.IntVar()
            self.radioValue.append(self.rvP)
            self.lista = list(prolog.query("pregunta("+str(i+7)+",X)."))
            self.pre.append(self.lista[0]["X"])
            self.lbp= tk.Label(self.ventana, text=self.pre[i],bg="#F4FBAF",font=("Arial",12),height=1)
            self.labels.append(self.lbp)
            self.labels[i].grid(column=0, row=i+3, sticky="W",pady=2)
            self.rSi= tk.Radiobutton(self.ventana, text='Si',bg="#F4FBAF",variable=self.radioValue[i], value=1) 
            self.rdioSi.append(self.rSi)
            self.rNo= tk.Radiobutton(self.ventana, text='No',bg="#F4FBAF",variable=self.radioValue[i], value=0) 
            self.rdioNo.append(self.rNo)
            
            self.rdioSi[i].grid(column=1, row=i+3,pady=2)
            self.rdioNo[i].grid(column=2, row=i+3,pady=2)
        
        self.boton1=tk.Button(self.ventana, text="Salir", command=self.ventana.destroy,bg="brown",fg="white",font=('Comic Sans MS',14))
        self.boton1.grid(column=2, row=14,padx=0,pady=5)
        
        self.boton2=tk.Button(self.ventana, text="Aceptar", command=self.consultar,bg="brown",fg="white",font=('Comic Sans MS',14))
        self.boton2.grid(column=3, row=14,padx=0,pady=5)
        self.ventana.mainloop()
        
    def consultar(self):
        for i in range(6):
            self.labelValue = tk.Label(self.ventana, textvariable=self.radioValue[i])
            self.resp=self.labelValue.cget("text")
            if self.resp==1:
                self.resp="si"
            else:
                self.resp="no"
            
            self.consulta+=self.resp+","

        self.ventana.destroy()
        ventanasig=Respuesta(self.consulta,2)
        

class Respuesta:
    def __init__(self, respuesta,nivel):
        self.ventana = tk.Toplevel()
        self.ventana.iconbitmap("form.ico")
        self.ventana.config(bg="#F4FBAF")
        self.ventana.resizable(0,0)
        self.label1=tk.Label(self.ventana,text= "RESPUESTA",bg="#F4FBAF",fg="brown",font=('Comic Sans MS',18,'bold'))
        self.label1.pack()
        self.imagen2=tk.PhotoImage(file ='form.png')
        label2 =tk.Label(self.ventana, image=self.imagen2, bg="#F4FBAF",width=50,height=50)
        label2.pack()
        self.texto="Candidato rechazado"
        self.lon=0
        if nivel==2:
            self.q1 = list(prolog.query("obprestamo("+respuesta+"R)."))
            self.texto ="Candidato "+self.q1[0]["R"]
            
        self.vec=respuesta.split(",")
        self.lon=len(self.vec)-1
        self.texto1=""
        cont=0
        for i in range(self.lon):
            self.resp=self.vec[i]
            if (i==2) | (i==8) :
                if self.resp=="si":
                    self.resp= list(prolog.query("problema("+str(i+1)+",R),!."))
                    self.texto1+="\n"+self.resp[0]["R"]
                    cont=cont+1
            else:
                if self.resp=="no":
                    self.resp= list(prolog.query("problema("+str(i+1)+",R),!."))
                    self.texto1+="\n"+self.resp[0]["R"]
                    cont=cont+1
        if cont>0:
            self.texto=self.texto+"\n"+ "Por las siguientes razones:"+"\n"+self.texto1

        self.label3= tk.Label(self.ventana, text= self.texto,bg="#F4FBAF",font=('Arial',14))
        self.label3.pack()
        self.boton2=tk.Button(self.ventana, text="Aceptar", command=self.ventana.destroy,bg="brown",fg="white",font=('Comic Sans MS',14))
        self.boton2.pack(pady=25, padx=25)
        self.ventana.mainloop()
        

# Aplicacion
prolog=Prolog()
prolog.consult("hechos.pl")
app = tk.Tk()
window = MainWindow(app)
app.mainloop()