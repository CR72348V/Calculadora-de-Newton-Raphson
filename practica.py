import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def ejecutar_metodo():
    try:
        texto_f = entry_funcion.get()
        def f(x): return eval(texto_f, {"x": x, "np": np})
        def df(x): 
            h = 0.000001
            return (f(x + h) - f(x)) / h

        r0 = float(entry_x0.get())
        error_permitido = float(entry_error.get())
        
        error_absoluto = 100 
        iteraciones = 0
        
        txt_resultados.delete('1.0', tk.END)

        if iteraciones <= 30:
            while error_absoluto > error_permitido and iteraciones < 30:
                ra = r0 - (f(r0) / df(r0))
                
                error_absoluto = abs(ra - r0)
                
                r0 = ra
                iteraciones += 1
                
                txt_resultados.insert(tk.END, f"Iter {iteraciones}: ra = {ra:.6f}\n")
            
            txt_resultados.insert(tk.END, f"\nRaíz final: {r0:.6f}")
            dibujar_grafica(f, r0)
        else:
            txt_resultados.insert(tk.END, "El método no converge")

    except Exception as e:
        messagebox.showerror("Error", "Verifica la entrada (ej: usar 'x' y '*' para multiplicar)")

        

def dibujar_grafica(func_usuario, raiz):
    ax.clear()
    x_eje = np.linspace(raiz - 3, raiz + 3, 100)
    ax.plot(x_eje, func_usuario(x_eje), label="f(x)", color="blue")
    ax.axhline(0, color='black', linewidth=1)
    ax.scatter(raiz, 0, color='red', label=f"Raíz: {raiz:.4f}")
    ax.legend(); ax.grid(True)
    canvas.draw()

ventana = tk.Tk()
ventana.title("Newton Raphson")
ventana.geometry("950x550")
ventana.configure(bg="#fdfde0")

frame_controles = tk.Frame(ventana, bg="#fdfde0")
frame_controles.pack(side=tk.LEFT, padx=20)

tk.Label(frame_controles, text="Expresión f(x) (ej: x**3 - 2*x - 5):", bg="#fdfde0", font=("Arial", 10, "bold")).pack()
entry_funcion = tk.Entry(frame_controles, width=35, font=("Arial", 11))
entry_funcion.pack(pady=5)

tk.Label(frame_controles, text="Aproximación inicial (r0):", bg="#fdfde0").pack()
entry_x0 = tk.Entry(frame_controles, width=15); entry_x0.pack(pady=5)

tk.Label(frame_controles, text="Error (tolerancia):", bg="#fdfde0").pack()
entry_error = tk.Entry(frame_controles, width=15); entry_error.pack(pady=5)

tk.Button(frame_controles, text="CALCULAR", bg="#98fb98", font=("Arial", 10, "bold"), command=ejecutar_metodo, width=20).pack(pady=10)
tk.Button(frame_controles, text="LIMPIAR", bg="orange", font=("Arial", 10, "bold"), command=lambda: txt_resultados.delete('1.0', tk.END), width=20).pack(pady=5)

txt_resultados = tk.Text(frame_controles, height=10, width=35, font=("Courier New", 10))
txt_resultados.pack(pady=10)

fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

ventana.mainloop()