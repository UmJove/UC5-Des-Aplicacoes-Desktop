# 1. Você está criando um programa em Python e precisa abrir a janela principal onde os botões e rótulos serão exibidos.
# Escreva o código necessário para criar a janela principal usando Tkinter.

import tkinter as tk

root = tk.Tk()
root.title("Janela Principal")
root.geometry("200x200")

rotulo_1 = tk.Label(root, text="Rótulo 1")
rotulo_1.pack(pady=15)

btn_1 = tk.Button(root, text="Botão 1")
btn_1.pack(pady=10)

rotulo_2 = tk.Label(root, text="Rótulo 2")
rotulo_2.pack(pady=10)

btn_2 = tk.Button(root, text="Botão 2")
btn_2.pack(pady=10)

root.mainloop()