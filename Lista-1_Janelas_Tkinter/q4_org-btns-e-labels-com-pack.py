# 4. Você adicionou um rótulo (Label) e um botão, mas eles não aparecem corretamente organizados na tela.
# Mostre como usar o método correto (pack) para posicionar esses widgets dentro da janela principal.

import tkinter as tk

root = tk.Tk()
root.title("Janela Principal")
root.geometry("300x400")

def mostrar_clique1():
    txt_clicado = tk.Label(root, text="Você clicou no botão 1")
    txt_clicado.pack()

def mostrar_clique2():
    txt_clicado2 = tk.Label(root, text="Você clicou no botão 2")
    txt_clicado2.pack()

titulo = tk.Label(root, text="Organizando rótulos e botões", font=("Arial", 12))
titulo.pack(pady=15)

rotulo1 = tk.Label(root, text="Rótulo 1")
rotulo1.pack(pady=10)


btn_1 = tk.Button(root, text="Botão 1", command=mostrar_clique1)
btn_1.pack(pady=10)

rotulo2 = tk.Label(root, text="Rótulo 2")
rotulo2.pack(pady=10)

btn_2 = tk.Button(root, text="Botão 2", command=mostrar_clique2)
btn_2.pack(pady=10)

btn_fechar = tk.Button(root, text="Fechar", command=root.destroy)
btn_fechar.pack(pady=15)

root.mainloop() 