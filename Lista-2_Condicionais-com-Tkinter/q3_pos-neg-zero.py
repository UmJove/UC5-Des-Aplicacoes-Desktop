# Atividade 3 – Identificador de números

import tkinter as tk
from tkinter import messagebox

# Configurando janela
app = tk.Tk()
app.title("Números")
app.geometry("300x300")

# Função de classificação de números (+, - ou 0)
def classificar_num():
    try:
        numero = float(entry_num.get())
        if numero > 0:
            messagebox.showinfo("Resultado", f"Número digitado ({numero}) é positivo")
        elif numero < 0:
            messagebox.showinfo("Resultado", f"Número digitado ({numero}) é negativo")
        elif numero == 0:
            messagebox.showinfo("Resultado", f"Número digitado ({numero}) é zero")
    except ValueError as e:
        messagebox.showerror("Erro:",f"{e}")
# Título do corpo da página
titulo_janela = tk.Label(app, text="Identificador de números", font=("Arial", 14))
titulo_janela.pack(pady=15)

# Entrada de número
entry_num = tk.Entry(app, width=10)
entry_num.pack(pady=5)

btn_resultado = tk.Button(app, text="Classificar", command=classificar_num)
btn_resultado.pack(pady=5)

# Ativação da aplicação
app.mainloop()