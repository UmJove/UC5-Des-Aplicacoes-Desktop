# 7. Em uma aplicação de calculadora, você precisa adicionar dois botões, um chamado "Somar" e outro chamado "Subtrair".
# Crie uma janela com esses dois botões lado a lado.
import tkinter as tk


janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x450")

titulo = tk.Label(janela, text="Calculadora", font=("Arial", 12))
titulo.grid(row=0, column=0, columnspan=4, pady=10)



btn_somar = tk.Button(janela, text="Somar")
btn_somar.grid(row=10, column=0)

btn_subritrair = tk.Button(janela, text="Subtrair")
btn_subritrair.grid(row=10, column=1)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.grid_columnconfigure(3, weight=1)



janela.mainloop()