
import tkinter as tk
from tkinter import PhotoImage, ttk
import math
from tkinter.constants import X
# from PIL import ImageTk, Image

class aplicarFuncionesTriangulo(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label2 = ttk.Label(self)
        self.label3 = ttk.Label(self)
        self.label["text"] = ("Aplicación para calcular elementos en un triángulo rectángulo "
                              "\nSeleccione la opción según sus datos disponibles\n")
        self.label.pack()
        
        
        #op=[('python',0),('C++',1),('C',2),('Java',3)]

       
        # Cateto opuesto
        self.label2["text"] = ("Ingrese el valor del cateto opuesto ")
        self.label2.pack()

        self.catetoOpuesto = ttk.Entry(self)
        self.catetoOpuesto.pack()

        # Cateto adyacente
        self.label3["text"] = ("\nIngrese el valor del cateto adyacente ")
        self.label3.pack()
        
        self.catetoAdyacente = ttk.Entry(self)
        self.catetoAdyacente.pack()

        self.greet_button = ttk.Button(
            self, text="Calcular", command=self.say_hello)
        self.greet_button.pack()
        
        self.greet_label = ttk.Label(self)
        self.greet_label.pack()
    
    def say_hello(self):
        cOp = self.catetoOpuesto.get()
        cAd = self.catetoAdyacente.get()
        cOp = float(cOp)
        cAd = float(cAd)
        hipotenusa = math.sqrt(cOp**2 + cAd**2)
        self.greet_label["text"] = \
            "El valor de la hipotenusa es {}".format(round(hipotenusa,2))
            # "¡Hola, {}!".format(self.name_entry.get())
        
        '''
            c1 = int(input('valor Cateto Adyacente: '))
            c2 = int(input('valor Cateto Opuesto: '))
            valor = math.sqrt((c1*c1) + (c2*c2))
            print("El valor de la hipotenusa es: ", valor, '\n')
            print('La formula es: h^2 = raiz(c1^2 + c2^2)\n')
        '''

    def ang_int():
        x = input('Tiene algun angulo interior?: ')
        if x == 'si' or x=='Si':
            y = input('Cual es ese angulo?: ')
            gvalor = 90-y
            print('El valor del tercer angulo es: ', gvalor)
        elif x == 'no' or x=='No':
            y = input('Que lado no tienes?: ')
            if y == 'ca':
                print('Se usa la funcion Sen(x) = co/h')
                co = int(input("Valor cateto opueto: "))
                h = int(input("Valor hipotenusa: "))
                gvalor = math.asin(co/h)
                print('el valor del angulo es: ',math.degrees(gvalor),'°')
            elif y == 'co':
                print('Se usa la funcion Cos(x) = ca/h')
                ca = int(input("Valor cateto adyacente: "))
                h = int(input("Valor hipotenusa: "))
                gvalor = math.acos(ca/h)
                print('el valor del angulo es: ',math.degrees(gvalor),'°')
            elif y == 'h':
                print('Se usa la funcion Tan(x) = co/ca')
                co = int(input("Valor cateto opuesto: "))
                ca = int(input("Valor cateto adyacente: "))
                gvalor = math.atan(co/ca)
                print('el valor del angulo es: ', math.degrees(gvalor),'°')
            control_ciclo()
            return gvalor

'''
def control_ciclo():
    cicho = input("Desea ingresar otro dato?\nSi/No ")
    while cicho=='si'or cicho=='SI' or cicho=='Si' or cicho=='sI':
        system("cls")
        Hip_cat()
    else:
        system("cls")
        print('Todo bien PA')

def Hip_cat():
    u = input('que necesita hallar? Lados/Angulos: ')

    if u == 'lado':
        x = input('que necesita hallar? Lados/Angulos: ')
        if x=='h' or x=='H':
            c1 = int(input('valor Cateto Adyacente: '))
            c2 = int(input('valor Cateto Opuesto: '))
            valor = math.sqrt((c1*c1) + (c2*c2))
            print("El valor de la hipotenusa es: ", valor, '\n')
            print('La formula es: h^2 = raiz(c1^2 + c2^2)\n')


        elif x=='c1' or x=='C1' or x=='c2' or x=='C2':
            h = int(input('valor hipotenusa: '))
            c2 = int(input('valor Adyacente u Opuesto: '))
            valor = math.sqrt((h*h) - (c2*c2))
            print("El valor del cateto es: ", valor, '\n')
            print('La formula es: c = raiz(h^2 - c^2)\n')
        control_ciclo()
    elif u == 'angulo':
        ang_int()
'''
class Explicar(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)

        self.label["text"] = ("Triángulo rectángulo:\n\nEl triángulo rectángulo es aquel que tiene un ángulo interior que es recto, es decir, mide 90º."
                              "\nEste triángulo tiene varios elementos, a saber:\n\nHipotenusa: Es el lado mayor del triángulo, tiene al frente el ángulo"
                              " de 90° que caracteriza a este tipo de triángulo")
        self.label.pack()
        
        
        '''
        # https://programacionpython80889555.wordpress.com/2018/04/15/visualizando-imagenes-con-python-y-tkinter/
        imagen = PhotoImage(file='trect.jpeg')
        fondo = self.label(ttk.Frame,image=imagen).place(x=0,y=0)
        '''
                
        '''
        path = 'trect.jpeg'
        img = ImageTk.PhotoImage(Image.open(path))
        panel = self.Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        '''

        '''
        self.web_button = ttk.Button(self, text="Visitar web")
        self.web_button.pack(pady=10)
        
        self.forum_button = ttk.Button(self, text="Visitar foro")
        self.forum_button.pack()
        '''

class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        #main_window.title("Panel de pestañas en Tcl/Tk")
        main_window.title("El triángulo rectángulo")
        #main_window.geometry("206x245")
        main_window.geometry("800x600")
        self.notebook = ttk.Notebook(self)
        
        # Pestaña explicación
        self.explicar_frame = Explicar(self.notebook, width = 400, height = 400)
        self.notebook.add(self.explicar_frame, text="Explicación", padding=10)

        # Pestaña aplicación
        self.aplicarFuncionesTriangulo = aplicarFuncionesTriangulo(self.notebook)
        self.notebook.add(self.aplicarFuncionesTriangulo, text="Triángulo rectángulo", padding=10)
        
        
        self.notebook.pack(padx=50, pady=50)
        self.pack()

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()


'''
import math
from os import system

print("Bienvenidos! \nvamos a aprender sobre triangulos rectangulos \nEstas son las partes que componen el triangulo: ")
print("El triángulo rectángulo es aquel que tiene un ángulo interior que es recto, es decir,\nmide 90º. ... La principal característica del triángulo es que, como ampliaremos más adelante, \ntiene un lado de mayor longitud (llamado hipotenusa) y otros dos denominados catetos cuya \nunión forma el ángulo recto\n")
print('h = Hipotenusa\nc1 = Cateto1\nc2=cateto2')

def ang_int():
    x = input('Tiene algun angulo interior?: ')
    if x == 'si' or x=='Si':
        y = input('Cual es ese angulo?: ')
        gvalor = 90-y
        print('El valor del tercer angulo es: ', gvalor)
    elif x == 'no' or x=='No':
        y = input('Que lado no tienes?: ')
        if y == 'ca':
            print('Se usa la funcion Sen(x) = co/h')
            co = int(input("Valor cateto opueto: "))
            h = int(input("Valor hipotenusa: "))
            gvalor = math.asin(co/h)
            print('el valor del angulo es: ',math.degrees(gvalor),'°')
        elif y == 'co':
            print('Se usa la funcion Cos(x) = ca/h')
            ca = int(input("Valor cateto adyacente: "))
            h = int(input("Valor hipotenusa: "))
            gvalor = math.acos(ca/h)
            print('el valor del angulo es: ',math.degrees(gvalor),'°')
        elif y == 'h':
            print('Se usa la funcion Tan(x) = co/ca')
            co = int(input("Valor cateto opuesto: "))
            ca = int(input("Valor cateto adyacente: "))
            gvalor = math.atan(co/ca)
            print('el valor del angulo es: ', math.degrees(gvalor),'°')
        control_ciclo()
        return gvalor


def control_ciclo():
    cicho = input("Desea ingresar otro dato?\nSi/No ")
    while cicho=='si'or cicho=='SI' or cicho=='Si' or cicho=='sI':
        system("cls")
        Hip_cat()
    else:
        system("cls")
        print('Todo bien PA')

def Hip_cat():
    u = input('que necesita hallar? Lados/Angulos: ')

    if u == 'lado':
        x = input('que necesita hallar? Lados/Angulos: ')
        if x=='h' or x=='H':
            c1 = int(input('valor Cateto Adyacente: '))
            c2 = int(input('valor Cateto Opuesto: '))
            valor = math.sqrt((c1*c1) + (c2*c2))
            print("El valor de la hipotenusa es: ", valor, '\n')
            print('La formula es: h^2 = raiz(c1^2 + c2^2)\n')


        elif x=='c1' or x=='C1' or x=='c2' or x=='C2':
            h = int(input('valor hipotenusa: '))
            c2 = int(input('valor Adyacente u Opuesto: '))
            valor = math.sqrt((h*h) - (c2*c2))
            print("El valor del cateto es: ", valor, '\n')
            print('La formula es: c = raiz(h^2 - c^2)\n')
        control_ciclo()
    elif u == 'angulo':
        ang_int()
Hip_cat()

'''