# 2. Um colega criou a janela principal do Tkinter, mas quando executa o programa, ela fecha imediatamente.
# Escreva a linha de código que faz a janela permanecer aberta aguardando interações do usuário.

import tkinter as tk

root = tk.Tk()
root.title("Janela Principal")
root.geometry("700x300")

titulo = tk.Label(root, text="Boas-vindas!")
titulo.pack(pady=15)

btn_fechar = tk.Button(root, text="Fechar", command=root.destroy)
btn_fechar.pack(pady=10)

# Resposta
root.mainloop() 