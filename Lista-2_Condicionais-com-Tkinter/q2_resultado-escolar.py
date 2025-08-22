# Atividade 2 - Resultado escolar

import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("Resultado Final")
app.geometry("400x200")

def calc_resultado():
    try:
        media_tratada = f"{float(entrada.get()):.1f}"
        media = float(media_tratada)
        if media >= 7 and media <= 10:
            messagebox.showinfo("RESULTADO",f"Aprovado, media {media:.1f}.")
        elif media < 7 and media >= 5:
            messagebox.showinfo("RESULTADO",f"Em recuperação, media {media:.1f}.")
        elif media < 5 and media >= 0:
            messagebox.showinfo("RESULTADO",f"Reprovado, media {media:.1f}.")
        else:
            raise ValueError("Valor inválido") # Se for maior que 10 ou menor que 0
        
    except ValueError as e:
        messagebox.showerror("Erro!", f"{e}!")

titulo = tk.Label(app, text="Resultado Escolar Final", font=("Helvetica", 14))
titulo.pack(pady=10)

rotulo = tk.Label(app, text="Digite a média final do aluno", font=("Helvetica", 12))
rotulo.pack(pady=10)

entrada = tk.Entry(app, width=10)
entrada.pack(pady=10)

btn_resultado = tk.Button(app, text="Resultado", command=calc_resultado)
btn_resultado.pack(pady=5)


app.mainloop()