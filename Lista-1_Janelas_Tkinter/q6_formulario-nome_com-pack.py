# 6. Você está criando um formulário simples para coletar o nome do usuário.
# Faça um programa em Tkinter com uma janela contendo um rótulo (Label) escrito "Digite seu nome:" e uma caixa de texto (Entry) logo abaixo.

import tkinter as tk

janela = tk.Tk()
janela.title("Formulário")
janela.geometry("400x200")

titulo_janela = tk.Label(janela, text=("Formulário"), font=("Arial", 14))
titulo_janela.pack(pady=10)

rotulo1 = tk.Label(janela, text="Digite seu nome:", font=("Arial", 10))
rotulo1.pack(padx=20)

caixa1 = tk.Entry(janela, width=30)
caixa1.pack(pady=20)

janela.mainloop()