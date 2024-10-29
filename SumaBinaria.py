import tkinter as tk
from tkinter import messagebox

class TuringMachine:
    # Inicialización del cabezal y la cinta
    def __init__(self, cinta):
        self.cinta = list(cinta)
        self.cabezal = 0
        self.estado = 'inicio'
        self.resultado = 2
    
    def avanzar(self):
        transiciones = {
            'inicio': {'1': ('estado1', '1', 'D')},  
            'estado1': {'0': ('estado2', '0', 'D')}, 
            'estado2': {'=': ('estado3', '=', 'D'), '0': ('estado2', '0', 'D'), '1': ('estado2', '1', 'D')},  
            'estado3': {'0': ('estado3', '0', 'D'), '1': ('estado3', '1', 'D'), 'B': ('final', 'B', 'D')} 
        }
        
        simbolo_actual = self.cinta[self.cabezal]
        
        if self.estado in transiciones and simbolo_actual in transiciones[self.estado]:
            nuevo_estado, simbolo_escribir, direccion = transiciones[self.estado][simbolo_actual]
            self.cinta[self.cabezal] = simbolo_escribir
            self.estado = nuevo_estado
            
            if direccion == 'D':
                self.cabezal += 1
            elif direccion == 'I':
                self.cabezal -= 1
                
            if self.estado == 'estado3' and simbolo_actual == '1':
                self.resultado += 1
                
    def ejecutar(self):
        while self.estado != 'final':
            if self.cabezal < 0 or self.cabezal >= len(self.cinta):
                break
            self.avanzar()
        return self.resultado
    
class InterfazTuring:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Suma Binaria")
        self.ventana.configure(bg="#2E2E2E")  # Cambiado a un gris oscuro
        self.ventana.geometry("400x300")  
        
        self.etiqueta = tk.Label(ventana, text="Ingrese un número binario", bg="#2E2E2E", fg="white", font=("Arial", 12))
        self.etiqueta.pack(pady=10)
        
        self.entrada = tk.Entry(ventana, bg="#4F4F4F", fg="white", font=("Arial", 12))  # Cambiado a un gris medio
        self.entrada.pack(pady=10, padx=20)
        
        self.boton_calcular = tk.Button(ventana, text="Calcular", command=self.calcular_suma, bg="#1C1C1C", fg="white", font=("Arial", 10))  # Cambiado a un gris muy oscuro
        self.boton_calcular.pack(pady=10)
        
        self.etiqueta_resultado_decimal = tk.Label(ventana, text="", bg="#2E2E2E", fg="white", font=("Arial", 12))
        self.etiqueta_resultado_decimal.pack(pady=10)
        
        self.etiqueta_resultado_binario = tk.Label(ventana, text="", bg="#2E2E2E", fg="white", font=("Arial", 12))
        self.etiqueta_resultado_binario.pack(pady=10)

    def calcular_suma(self):
        entrada_binaria = self.entrada.get()
        if not all(c in '01' for c in entrada_binaria):
            messagebox.showerror("Error", "Ingrese solo números binarios (0 y 1)")
            return
        
        cinta_entrada = "10=" + entrada_binaria + "B"
        maquina = TuringMachine(cinta_entrada)
        resultado = maquina.ejecutar()
        
        self.etiqueta_resultado_decimal.config(text=f"El resultado es (Decimal): {resultado}")
        resultado_binario = bin(resultado)[2:] 
        self.etiqueta_resultado_binario.config(text=f"El resultado es (Binario): {resultado_binario}")
        
ventana = tk.Tk()
app = InterfazTuring(ventana)
ventana.mainloop()