import tkinter as tk
from tkinter import ttk
import math
# from PIL import ImageTk, Image

class HallarHipotenusa(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label2 = ttk.Label(self)
        self.label3 = ttk.Label(self)
        self.label["text"] = ("La hipotenusa se halla con los dos catetos del triangulo, siguiendo la siguiente formula."
                            "\n\n                                                                   h² = C₁² + C₂²\n")
        self.label.pack()
        
        # Cateto opuesto
        self.label2["text"] = ("Ingrese el valor del primer cateto ")
        self.label2.pack()

        self.catetoOpuesto = ttk.Entry(self)
        self.catetoOpuesto.pack()

        # Cateto adyacente
        self.label3["text"] = ("\nIngrese el valor del segundo cateto ")
        self.label3.pack()
        
        self.catetoAdyacente = ttk.Entry(self)
        self.catetoAdyacente.pack()

        self.greet_button = ttk.Button(
            self, text="Calcular", command=self.calcularHipotenusa)
        self.greet_button.pack()
        
        self.greet_label = ttk.Label(self)
        self.greet_label.pack()
    
    def calcularHipotenusa(self):
        cOp = self.catetoOpuesto.get()
        cAd = self.catetoAdyacente.get()
        cOp = float(cOp)
        cAd = float(cAd)
        hipotenusa = math.sqrt(cOp**2 + cAd**2)
        self.greet_label["text"] = \
            "El valor de la hipotenusa es {}".format(round(hipotenusa,2))
            # "¡Hola, {}!".format(self.name_entry.get())
        
class HallarCateto(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label2 = ttk.Label(self)
        self.label3 = ttk.Label(self)
        self.label["text"] = ("Para hallar un cateto se debe usar el valor de la hipotenusa y el del cateto restante."
                            "\n\n                                                                   C = h² - C²\n")
        self.label.pack()

        # Cateto opuesto
        self.label2["text"] = ("Ingrese el valor de la hipotenusa ")
        self.label2.pack()

        self.hipotenusa = ttk.Entry(self)
        self.hipotenusa.pack()

        # Cateto adyacente
        self.label3["text"] = ("\nIngrese el valor del cateto ")
        self.label3.pack()
        
        self.cateto = ttk.Entry(self)
        self.cateto.pack()

        self.greet_button = ttk.Button(
            self, text="Calcular", command=self.calcularCateto1)
        self.greet_button.pack()
        
        self.greet_label = ttk.Label(self)
        self.greet_label.pack()
    
    def calcularCateto1(self):
        hPt = self.hipotenusa.get()
        cAd = self.cateto.get()
        hPt = float(hPt)
        cAd = float(cAd)
        cat = math.sqrt((hPt**2)-(cAd**2))
        self.greet_label["text"] = \
            "El valor del cateto es {}".format(round(cat,2))

class Explicar(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Bienvenido! \n\nEl siguiente programa fue desarrollado con el fin de ayudar a hallar ciertos datos de los triángulos rectángulos como \nla hipotenusa o catetos. "
                            "\nTodo esto explicando los conceptos y las formulas aplicadas para llevar acabo cada procedimiento.")
        self.label.pack()
       
class Conceptos(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Triángulo rectángulo: El triángulo rectángulo es aquel que tiene un ángulo interior que es recto, es decir, mide 90º."
                            "\nEste triángulo tiene varios elementos, a conocer como lo son.\n\nHipotenusa: Es el lado opuesto al ángulo recto en "
                            "un triángulo rectángulo, resultando ser su lado de mayor \nlongitud. \n\nCateto adyacente: "
                            "Es uno de los dos lados de menor longitud del triángulo rectángulo. Se define como el \nsegmento que es contiguo al ángulo de referencia \n\nCateto opuesto: "
                            "Es el otro lado de menor longitud. Se define como aquel que se encuentra al lado contrario \ndel ángulo de referencia.")
        self.label.pack()
        
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        #main_window.title("Panel de pestañas en Tcl/Tk")
        main_window.title("El triángulo rectángulo")
        
        self.notebook = ttk.Notebook(self)
        
        # Pestaña explicación
        self.explicar_frame = Explicar(self.notebook)
        self.notebook.add(
            self.explicar_frame, text="Explicación", padding=10)
        
        #Conceptos
        self.conceptos = Conceptos(self.notebook)
        self.notebook.add(
            self.conceptos, text="Conceptos", padding=10)
        
        #Hallar Hipotenusa
        self.HallarHipotenusa = HallarHipotenusa(self.notebook)
        self.notebook.add(
            self.HallarHipotenusa, text="Hallar la hipotenusa", padding=10)
        
        #Hallar Cateto
        self.HallarCateto = HallarCateto(self.notebook)
        self.notebook.add(
        self.HallarCateto, text="Hallar un cateto", padding=10)
        
        self.notebook.pack(padx=50, pady=50)
        self.pack()

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
