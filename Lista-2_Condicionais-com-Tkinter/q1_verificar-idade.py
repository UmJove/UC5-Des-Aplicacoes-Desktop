# Atividade 1 - Controle de acesso por idade

import tkinter as tk
from tkinter import messagebox

def verificar_idade():
    try:
        idade = int(entry_idade.get())
        if idade < 18:
            messagebox.showinfo("-18!!", "Usuário menor de idade!")
        elif idade >= 18:
            messagebox.showinfo("+18", "Usuário maior de idade.")
    except:
        messagebox.showinfo("Erro!", "Entrada inválida")
    entry_var.set("") # Limpar a entrada após messagebox


root = tk.Tk()
root.title("Verificação de Idade")
root.geometry("300x150")

tk.Label(root, text="Digite sua idade:").pack(pady=5)
entry_var=tk.StringVar() # Definindo a string de entrada
entry_idade = tk.Entry(root, textvariable=entry_var)
entry_idade.pack(pady=5)

tk.Button(root, text="Verificar", command=verificar_idade).pack(pady=10)

root.mainloop()
